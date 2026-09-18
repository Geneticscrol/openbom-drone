from kite5.bom import load, validate


def test_kite5_bom_is_valid():
    assert validate(load()) == []


def test_validate_flags_missing_key():
    doc = {"target_g": 650, "items": [{"id": "x", "name": "x", "qty": 1, "grams": 10}]}
    errors = validate(doc)
    assert any("inr_example" in e for e in errors)


def test_validate_flags_duplicate_id():
    item = {"id": "dupe", "name": "x", "qty": 1, "grams": 10, "inr_example": 0}
    doc = {"target_g": 650, "items": [item, dict(item)]}
    errors = validate(doc)
    assert any("duplicate id" in e for e in errors)


def test_validate_flags_non_positive_grams():
    doc = {
        "target_g": 650,
        "items": [{"id": "x", "name": "x", "qty": 1, "grams": 0, "inr_example": 0}],
    }
    errors = validate(doc)
    assert any("grams must be > 0" in e for e in errors)


def test_validate_flags_empty_items():
    assert validate({"target_g": 650, "items": []}) != []
