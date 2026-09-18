from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "software"))
from hover_power import induced_power_w
from mass_budget import load, summarise
from mixer import mix

def test_kite5_under_target():
    s = summarise(load())
    assert s["grams"] < s["target_g"]
    assert s["grams"] > 400

def test_hover_power_positive():
    assert 20 < induced_power_w(6.5, 0.05) < 400

def test_mixer_idle():
    m = mix(0.1, 0, 0, 0)
    assert all(0 <= v <= 1 for v in m.values())
