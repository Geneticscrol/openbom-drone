from __future__ import annotations

import json
from pathlib import Path

BOM_PATH = Path(__file__).resolve().parents[1] / "6_BOM" / "kite5.json"

REQUIRED_ITEM_KEYS = ("id", "name", "qty", "grams", "inr_example")


def load(path: Path = BOM_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(doc: dict) -> list[str]:
    errors: list[str] = []

    if doc.get("target_g", 0) <= 0:
        errors.append("target_g must be present and > 0")

    items = doc.get("items")
    if not isinstance(items, list) or not items:
        errors.append("items must be a non-empty list")
        return errors

    seen_ids: set[str] = set()
    for i, item in enumerate(items):
        for key in REQUIRED_ITEM_KEYS:
            if key not in item:
                errors.append(f"item {i}: missing '{key}'")
        item_id = item.get("id")
        if item_id in seen_ids:
            errors.append(f"item {i}: duplicate id '{item_id}'")
        seen_ids.add(item_id)
        if item.get("grams", 0) <= 0:
            errors.append(f"item {i} ({item_id}): grams must be > 0")
        if item.get("qty", 0) < 1:
            errors.append(f"item {i} ({item_id}): qty must be >= 1")
        if item.get("inr_example", 0) < 0:
            errors.append(f"item {i} ({item_id}): inr_example must be >= 0")

    return errors
