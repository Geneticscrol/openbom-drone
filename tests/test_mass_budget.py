from kite5.bom import load
from kite5.mass_budget import summarise


def test_kite5_under_target():
    s = summarise(load())
    assert s["grams"] < s["target_g"]
    assert s["grams"] > 400


def test_summarise_synthetic_doc():
    doc = {
        "name": "Test",
        "target_g": 100,
        "items": [
            {"id": "a", "name": "A", "qty": 2, "grams": 10, "inr_example": 5},
            {"id": "b", "name": "B", "qty": 1, "grams": 20, "inr_example": 15},
        ],
    }
    s = summarise(doc)
    assert s["grams"] == 40
    assert s["inr_example"] == 25
    assert s["margin_g"] == 60


def test_summarise_empty_items():
    doc = {"name": "Empty", "target_g": 100, "items": []}
    s = summarise(doc)
    assert s["grams"] == 0
    assert s["margin_g"] == 100


def test_summarise_over_target_gives_negative_margin():
    doc = {
        "name": "Overweight",
        "target_g": 10,
        "items": [{"id": "a", "name": "A", "qty": 1, "grams": 50, "inr_example": 0}],
    }
    s = summarise(doc)
    assert s["margin_g"] == -40
