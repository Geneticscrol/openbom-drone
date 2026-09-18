from __future__ import annotations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data" / "catalog.json"
CATEGORIES = ("frame", "motors", "props", "fc_esc", "rx", "vtx", "camera", "battery", "charger", "hardware")

def load_catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))

def line_total(part, qty):
    qty = max(0, int(qty))
    return {"id": part["id"], "name": part["name"], "category": part["category"], "qty": qty, "grams": part["grams"] * qty, "inr": part["inr_example"] * qty, "shop": part.get("shop", ""), "notes": part.get("notes", "")}

def tally(picks, target_g=650):
    lines = [line_total(p, q) for p, q in picks if q]
    grams = sum(l["grams"] for l in lines)
    inr = sum(l["inr"] for l in lines)
    missing = [c for c in CATEGORIES if not any(l["category"] == c for l in lines)]
    return {"lines": lines, "grams": grams, "inr": inr, "target_g": target_g, "over_weight": grams > target_g, "missing": missing}

def part_by_id(catalog, pid):
    for p in catalog["parts"]:
        if p["id"] == pid:
            return p
    raise KeyError(pid)
