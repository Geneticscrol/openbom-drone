from __future__ import annotations

from kite5.bom import load


def summarise(doc: dict) -> dict:
    grams = sum(i["grams"] * i["qty"] for i in doc["items"])
    inr = sum(i["inr_example"] * i["qty"] for i in doc["items"])
    return {
        "name": doc["name"],
        "grams": grams,
        "inr_example": inr,
        "target_g": doc["target_g"],
        "margin_g": doc["target_g"] - grams,
    }


def print_report(doc: dict, s: dict) -> None:
    print(f"{s['name']}  {s['grams']} g   margin {s['margin_g']} g to {s['target_g']} g")
    print(f"example INR  {s['inr_example']}\n")
    print(f"{'item':<28} {'qty':>3} {'g':>6} {'INR':>8}")
    for i in doc["items"]:
        g, inr = i["grams"] * i["qty"], i["inr_example"] * i["qty"]
        print(f"{i['name']:<28} {i['qty']:>3} {g:>6} {inr:>8}")


def main() -> None:
    doc = load()
    print_report(doc, summarise(doc))


if __name__ == "__main__":
    main()
