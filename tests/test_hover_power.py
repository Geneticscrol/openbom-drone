import pytest

from kite5.hover_power import induced_power_w, report


def test_hover_power_positive():
    assert 20 < induced_power_w(6.5, 0.05) < 400


def test_hover_power_rejects_non_positive_inputs():
    with pytest.raises(ValueError):
        induced_power_w(0, 0.05)
    with pytest.raises(ValueError):
        induced_power_w(6.5, 0)


def test_induced_power_increases_with_thrust():
    low = induced_power_w(4.0, 0.05)
    high = induced_power_w(8.0, 0.05)
    assert high > low


def test_report_shape():
    r = report(497.0, 12.7)
    assert r["thrust_g"] == 497.0
    assert r["p_electrical_w"] > r["p_induced_w"] > 0
    assert r["current_4s_a"] == pytest.approx(r["p_electrical_w"] / 14.8)
