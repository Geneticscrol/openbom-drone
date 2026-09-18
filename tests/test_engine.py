from openbom.engine import load_catalog, part_by_id, tally

def test_default_5in_has_motors():
    cat = load_catalog()
    picks = [(p, p["qty_default"]) for p in cat["parts"]]
    t = tally(picks)
    assert t["grams"] > 300
    assert t["inr"] > 10000
    motors = [l for l in t["lines"] if l["category"] == "motors"]
    assert motors[0]["qty"] == 4

def test_empty_missing_categories():
    t = tally([])
    assert "frame" in t["missing"]

def test_lookup():
    cat = load_catalog()
    assert part_by_id(cat, "rx-elrs-24")["grams"] == 1
