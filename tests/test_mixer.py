from kite5.mixer import mix


def test_mixer_idle():
    m = mix(0.1, 0, 0, 0)
    assert all(0 <= v <= 1 for v in m.values())


def test_pure_roll_favours_left_motors():
    m = mix(0.5, 0.2, 0.0, 0.0)
    assert m["m3"] > m["m1"]
    assert m["m4"] > m["m2"]


def test_pure_pitch_favours_rear_motors():
    m = mix(0.5, 0.0, 0.2, 0.0)
    assert m["m1"] > m["m2"]
    assert m["m3"] > m["m4"]


def test_pure_yaw_favours_ccw_motors():
    m = mix(0.5, 0.0, 0.0, 0.2)
    assert m["m2"] > m["m1"]
    assert m["m3"] > m["m4"]


def test_mixer_clips_to_unit_range():
    m = mix(1.5, 1.0, 1.0, 1.0)
    assert all(0.0 <= v <= 1.0 for v in m.values())
    m2 = mix(-1.0, 0.0, 0.0, 0.0)
    assert all(0.0 <= v <= 1.0 for v in m2.values())
