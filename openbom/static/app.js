let catalog = { parts: [] };
function picks() {
  return [...document.querySelectorAll(".qty")].map((el) => el.dataset.id + ":" + (el.value || "0"));
}
async function refresh() {
  const target = document.getElementById("target").value || 650;
  const t = await (await fetch("/api/tally?target=" + target + "&p=" + picks().join("&p="))).json();
  document.getElementById("inr").textContent = "₹" + t.inr.toLocaleString("en-IN");
  document.getElementById("grams").textContent = t.grams + " g";
  const st = document.getElementById("status");
  st.textContent = t.over_weight ? "over target" : "under target";
  st.className = t.over_weight ? "over" : "ok";
  document.getElementById("missing").textContent = t.missing.length ? "Still empty: " + t.missing.join(", ") : "Every category has something.";
}
function render() {
  const root = document.getElementById("list");
  const cats = [...new Set(catalog.parts.map((p) => p.category))];
  root.innerHTML = cats.map((c) => {
    const rows = catalog.parts.filter((p) => p.category === c).map((p) => `<div class="row"><input class="qty" type="number" min="0" max="20" value="${p.qty_default}" data-id="${p.id}" /><div>${p.name}<div style="color:#8ea08a;font-size:.8rem">${p.notes || ""}</div></div><div>${p.grams} g · ₹${p.inr_example}</div><a href="${p.shop}" target="_blank" rel="noopener">shop</a></div>`).join("");
    return `<section class="cat"><h2>${c}</h2>${rows}</section>`;
  }).join("");
  root.querySelectorAll(".qty").forEach((el) => el.addEventListener("input", refresh));
  refresh();
}
document.getElementById("target").addEventListener("input", refresh);
document.getElementById("csv").addEventListener("click", () => {
  const rows = [["id", "qty"]];
  document.querySelectorAll(".qty").forEach((el) => rows.push([el.dataset.id, el.value]));
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([rows.map((r) => r.join(",")).join("\n")], { type: "text/csv" }));
  a.download = "build.csv";
  a.click();
});
fetch("/api/catalog").then((r) => r.json()).then((c) => { catalog = c; render(); });
