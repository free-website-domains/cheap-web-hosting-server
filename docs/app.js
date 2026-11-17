let ALL_PLANS = [];
let PROVIDERS = {};

const CATEGORY_LABELS = {
  shared: "Shared",
  vps: "VPS",
  wordpress: "WordPress",
  paas: "PaaS"
};

function calculateTrueCost(plan, months, websites, monthlyOnly) {
  const maxSites = plan.max_websites;
  const plansNeeded = maxSites === "unlimited" ? 1 : Math.ceil(websites / Number(maxSites));
  const setupFee = Number(plan.setup_fee_usd || 0);

  let promoRate, renewalRate, promoTotal, renewalTotal;

  if (monthlyOnly && plan.monthly_no_contract_usd !== null) {
    const rate = Number(plan.monthly_no_contract_usd);
    promoRate = rate;
    renewalRate = rate;
    promoTotal = 0;
    renewalTotal = months * rate;
  } else {
    promoRate = Number(plan.promo_monthly_usd);
    renewalRate = Number(plan.renewal_monthly_usd);
    const promoMonths = Math.min(months, Number(plan.promo_term_months));
    const renewalMonths = Math.max(0, months - promoMonths);
    promoTotal = promoMonths * promoRate;
    renewalTotal = renewalMonths * renewalRate;
  }

  const totalCost = (promoTotal + renewalTotal + setupFee) * plansNeeded;
  const effectiveMonthly = totalCost / months;
  const spikePct = promoRate > 0 ? ((renewalRate - promoRate) / promoRate) * 100 : 0;

  return {
    plansNeeded,
    promoRate,
    renewalRate,
    totalCost,
    effectiveMonthly,
    spikePct
  };
}

function matchesWorkload(plan, workload) {
  const f = plan.features || {};
  switch (workload) {
    case "wordpress":
      return Boolean(f.wordpress && f.php && f.mysql);
    case "php_mysql":
      return Boolean(f.php && f.mysql);
    case "nodejs_python":
      return Boolean(f.nodejs || f.python || f.docker);
    case "vps":
      return plan.category === "vps" && Boolean(f.root_access);
    case "shared":
      return plan.category === "shared" || plan.category === "wordpress";
    default:
      return true;
  }
}

function renderReadings(rows, months) {
  const lowestEl = document.getElementById("readingLowest");
  const lowestPlanEl = document.getElementById("readingLowestPlan");
  const flatCountEl = document.getElementById("readingFlatCount");
  const flatNoteEl = document.getElementById("readingFlatNote");
  const spikeEl = document.getElementById("readingSpike");
  const spikePlanEl = document.getElementById("readingSpikePlan");

  if (rows.length === 0) {
    lowestEl.textContent = "—";
    lowestPlanEl.textContent = "No matching plans";
    flatCountEl.textContent = "0";
    flatNoteEl.textContent = "Adjust filters";
    spikeEl.textContent = "—";
    spikePlanEl.textContent = "No matching plans";
    return;
  }

  const lowest = rows[0];
  lowestEl.textContent = `$${lowest.cost.effectiveMonthly.toFixed(2)}/mo`;
  lowestPlanEl.textContent = `${lowest.plan.name} (${months}m)`;

  const flatPlans = rows.filter((r) => r.cost.spikePct === 0);
  flatCountEl.textContent = `${flatPlans.length} of ${rows.length}`;
  flatNoteEl.textContent = "0% renewal increase";

  const steepest = [...rows].sort((a, b) => b.cost.spikePct - a.cost.spikePct)[0];
  spikeEl.textContent =
    steepest.cost.spikePct === 0 ? "0%" : `+${steepest.cost.spikePct.toFixed(0)}%`;
  spikePlanEl.textContent = steepest.plan.name;
}

function renderDiff(months, websites, monthlyOnly) {
  const idA = document.getElementById("compareA").value;
  const idB = document.getElementById("compareB").value;
  const planA = ALL_PLANS.find((p) => p.id === idA);
  const planB = ALL_PLANS.find((p) => p.id === idB);
  const container = document.getElementById("diffBody");

  if (!planA || !planB) {
    container.innerHTML = "";
    return;
  }

  const costA = calculateTrueCost(planA, months, websites, monthlyOnly);
  const costB = calculateTrueCost(planB, months, websites, monthlyOnly);
  const diffTotal = Math.abs(costA.totalCost - costB.totalCost);
  const cheaper = costA.totalCost <= costB.totalCost ? planA.name : planB.name;

  const aClass = costA.totalCost <= costB.totalCost ? "diff-card diff-plus" : "diff-card diff-minus";
  const bClass = costB.totalCost <= costA.totalCost ? "diff-card diff-plus" : "diff-card diff-minus";

  container.innerHTML = `
    <div class="${aClass}">
      <div class="diff-title">${planA.name}</div>
      <div class="diff-figure">$${costA.totalCost.toFixed(2)} <span class="diff-unit">over ${months}m</span></div>
      <div class="diff-meta">
        <span>Promo $${costA.promoRate.toFixed(2)}/mo</span>
        <span>Renewal $${costA.renewalRate.toFixed(2)}/mo</span>
        <span>Effective $${costA.effectiveMonthly.toFixed(2)}/mo</span>
      </div>
    </div>
    <div class="${bClass}">
      <div class="diff-title">${planB.name}</div>
      <div class="diff-figure">$${costB.totalCost.toFixed(2)} <span class="diff-unit">over ${months}m</span></div>
      <div class="diff-meta">
        <span>Promo $${costB.promoRate.toFixed(2)}/mo</span>
        <span>Renewal $${costB.renewalRate.toFixed(2)}/mo</span>
        <span>Effective $${costB.effectiveMonthly.toFixed(2)}/mo</span>
      </div>
    </div>
    <div class="diff-verdict">
      <span class="diff-verdict-label">Net ${months}-month savings</span>
      <span class="diff-verdict-amount">$${diffTotal.toFixed(2)}</span>
      <span class="diff-verdict-winner">${cheaper} is lower total cost</span>
    </div>
  `;
}

function render() {
  const workload = document.getElementById("workload").value;
  const budgetVal = document.getElementById("budget").value;
  const maxBudget = budgetVal === "all" ? Infinity : Number(budgetVal);
  const months = Number(document.getElementById("horizon").value);
  const websites = Math.max(1, Number(document.getElementById("websites").value || 1));
  const noSpikeOnly = document.getElementById("noSpikeOnly").checked;
  const usOnly = document.getElementById("usOnly").checked;
  const monthlyOnly = document.getElementById("monthlyOnly").checked;
  const cpanelOnly = document.getElementById("cpanelOnly").checked;

  const rows = [];
  for (const plan of ALL_PLANS) {
    if (!matchesWorkload(plan, workload)) continue;
    if (usOnly && !plan.us_datacenters) continue;
    if (monthlyOnly && plan.monthly_no_contract_usd === null) continue;
    if (cpanelOnly && plan.control_panel !== "cPanel") continue;

    const cost = calculateTrueCost(plan, months, websites, monthlyOnly);
    if (noSpikeOnly && cost.spikePct > 0) continue;
    if (cost.effectiveMonthly > maxBudget) continue;

    rows.push({ plan, cost });
  }

  rows.sort((a, b) => a.cost.effectiveMonthly - b.cost.effectiveMonthly);

  renderReadings(rows, months);
  renderDiff(months, websites, monthlyOnly);

  const countEl = document.getElementById("resultCount");
  countEl.textContent = `Showing ${rows.length} compatible plan(s) over ${months} months for ${websites} site(s)`;

  const tbody = document.getElementById("resultsBody");
  if (rows.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" class="empty-row">No plans match all selected filters. Try increasing your budget or unchecking a filter.</td></tr>`;
    return;
  }

  tbody.innerHTML = rows
    .map(({ plan, cost }) => {
      const spikeClass =
        cost.spikePct === 0 ? "spike-zero" : cost.spikePct < 150 ? "spike-mid" : "spike-high";
      const spikeLabel = cost.spikePct === 0 ? "0% (Flat)" : `+${cost.spikePct.toFixed(0)}%`;
      const siteInfo =
        plan.max_websites === "unlimited"
          ? "Unlimited sites"
          : `${plan.max_websites} site(s)${cost.plansNeeded > 1 ? ` (${cost.plansNeeded}x plans)` : ""}`;
      const catLabel = CATEGORY_LABELS[plan.category] || plan.category;

      return `
        <tr>
          <td data-label="Plan">
            <div class="plan-name">${plan.name}</div>
            <div class="plan-meta-list">
              <span>${plan.vcpu} vCPU</span>
              <span>${plan.ram_gb} GB RAM</span>
              <span>${plan.storage_gb} GB</span>
              <span>${plan.control_panel}</span>
              <span>${siteInfo}</span>
            </div>
          </td>
          <td data-label="Type"><span class="badge badge-${plan.category}">${catLabel}</span></td>
          <td data-label="Promo Rate" class="mono">
            $${cost.promoRate.toFixed(2)}/mo
            <div class="plan-term">${monthlyOnly ? "Month-to-month" : `${plan.promo_term_months}m promo`}</div>
          </td>
          <td data-label="Renewal Rate" class="mono">$${cost.renewalRate.toFixed(2)}/mo</td>
          <td data-label="Renewal Spike" class="mono ${spikeClass}">${spikeLabel}</td>
          <td data-label="Total Cost" class="mono">$${cost.totalCost.toFixed(2)}</td>
          <td data-label="Effective / mo" class="mono eff-price">$${cost.effectiveMonthly.toFixed(2)}/mo</td>
        </tr>
      `;
    })
    .join("");
}

function populateDiffSelects() {
  const selectA = document.getElementById("compareA");
  const selectB = document.getElementById("compareB");
  const optionsHtml = ALL_PLANS.map(
    (p) => `<option value="${p.id}">${p.name}</option>`
  ).join("");
  selectA.innerHTML = optionsHtml;
  selectB.innerHTML = optionsHtml;
  selectA.value = "racknerd-1gb-kvm";
  selectB.value = "interserver-standard";
}

async function loadHostingData() {
  try {
    const [plansRes, providersRes] = await Promise.all([
      fetch("./data/plans.json"),
      fetch("./data/providers.json")
    ]);
    if (!plansRes.ok || !providersRes.ok) throw new Error("HTTP error");
    const plansData = await plansRes.json();
    const providersData = await providersRes.json();
    return { plans: plansData.plans || [], providers: providersData.providers || [] };
  } catch {
    if (window.__HOSTING_DATA__) {
      return window.__HOSTING_DATA__;
    }
    throw new Error("Unable to load hosting data");
  }
}

async function init() {
  const data = await loadHostingData();
  ALL_PLANS = data.plans || [];
  PROVIDERS = Object.fromEntries((data.providers || []).map((p) => [p.id, p]));

  populateDiffSelects();

  for (const id of [
    "workload",
    "budget",
    "horizon",
    "websites",
    "noSpikeOnly",
    "usOnly",
    "monthlyOnly",
    "cpanelOnly",
    "compareA",
    "compareB"
  ]) {
    document.getElementById(id).addEventListener("change", render);
    document.getElementById(id).addEventListener("input", render);
  }
  render();
}

init();
