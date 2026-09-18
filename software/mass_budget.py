#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

BOM = Path(__file__).resolve().parents[1] / "6_BOM" / "kite5.json"

def load(path=BOM):
    return json.loads(path.read_text(encoding="utf-8"))

def summarise(doc):
    grams = sum(i["grams"] * i["qty"] for i in doc["items"])
    inr = sum(i["inr_example"] * i["qty"] for i in doc["items"])
    return {"name": doc["name"], "grams": grams, "inr_example": inr, "target_g": doc["target_g"], "margin_g": doc["target_g"] - grams}

def main():
    doc = load()
    s = summarise(doc)
    print(f"{s['name']}  {s['grams']} g   margin {s['margin_g']} g to {s['target_g']} g")
    print(f"example INR  {s['inr_example']}\n")
    print(f"{'item':<28} {'qty':>3} {'g':>6} {'INR':>8}")
    for i in doc["items"]:
        print(f"{i['name']:<28} {i['qty']:>3} {i['grams']*i['qty']:>6} {i['inr_example']*i['qty']:>8}")

if __name__ == "__main__":
    main()
