let ALL_PLANS = [];
let PROVIDERS = {};

function calculateTrueCost(plan, months, websites, monthlyOnly) {
  const maxSites = plan.max_websites;
  const plansNeeded = maxSites === "unlimited" ? 1 : Math.ceil(websites / Number(maxSites));
  const setupFee = Number(plan.setup_fee_usd || 0);

  let promoRate, renewalRate, promoTotal, renewalTotal;

  if (monthlyOnly) {
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

function render() {
  const workload = document.getElementById("workload").value;
  const budgetVal = document.getElementById("budget").value;
  const maxBudget = budgetVal === "all" ? Infinity : Number(budgetVal);
  const months = Number(document.getElementById("horizon").value);
  const websites = Math.max(1, Number(document.getElementById("websites").value || 1));
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
    if (cost.effectiveMonthly > maxBudget) continue;

    rows.push({ plan, cost });
  }

  rows.sort((a, b) => a.cost.effectiveMonthly - b.cost.effectiveMonthly);

  const countEl = document.getElementById("resultCount");
  countEl.textContent = `Showing ${rows.length} compatible plan(s) over ${months} months for ${websites} site(s)`;

  const tbody = document.getElementById("resultsBody");
  if (rows.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" style="text-align:center;color:var(--muted);padding:32px;">No plans match all selected filters. Try increasing your budget or unchecking a filter.</td></tr>`;
    return;
  }

  tbody.innerHTML = rows
    .map(({ plan, cost }) => {
      const provider = PROVIDERS[plan.provider_id] || {};
      const spikeClass =
        cost.spikePct === 0 ? "spike-zero" : cost.spikePct < 150 ? "spike-mid" : "spike-high";
      const spikeLabel = cost.spikePct === 0 ? "0% (Flat)" : `+${cost.spikePct.toFixed(0)}%`;
      const siteInfo =
        plan.max_websites === "unlimited"
          ? "Unlimited sites"
          : `${plan.max_websites} site(s)${cost.plansNeeded > 1 ? ` · ${cost.plansNeeded}x plans` : ""}`;
      const specs = `${plan.vcpu} vCPU · ${plan.ram_gb} GB RAM · ${plan.storage_gb} GB`;

      return `
        <tr>
          <td>
            <div class="plan-name">${plan.name}</div>
            <div class="plan-meta">${specs} · ${plan.control_panel} · ${siteInfo}</div>
          </td>
          <td><span class="badge badge-${plan.category}">${plan.category.toUpperCase()}</span></td>
          <td class="mono">$${cost.promoRate.toFixed(2)}/mo<div class="plan-meta">${monthlyOnly ? "Month-to-month" : `${plan.promo_term_months}m promo`}</div></td>
          <td class="mono">$${cost.renewalRate.toFixed(2)}/mo</td>
          <td class="mono ${spikeClass}">${spikeLabel}</td>
          <td class="mono">$${cost.totalCost.toFixed(2)}</td>
          <td class="mono eff-price">$${cost.effectiveMonthly.toFixed(2)}/mo</td>
        </tr>
      `;
    })
    .join("");
}

async function init() {
  const [plansRes, providersRes] = await Promise.all([
    fetch("./data/plans.json"),
    fetch("./data/providers.json")
  ]);
  const plansData = await plansRes.json();
  const providersData = await providersRes.json();

  ALL_PLANS = plansData.plans || [];
  PROVIDERS = Object.fromEntries((providersData.providers || []).map((p) => [p.id, p]));

  for (const id of ["workload", "budget", "horizon", "websites", "usOnly", "monthlyOnly", "cpanelOnly"]) {
    document.getElementById(id).addEventListener("change", render);
    document.getElementById(id).addEventListener("input", render);
  }
  render();
}

init();
