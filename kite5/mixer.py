from __future__ import annotations


def mix(throttle: float, roll: float, pitch: float, yaw: float) -> dict:
    raw = [
        throttle - roll + pitch - yaw,  # M1 rear-right,  CW
        throttle - roll - pitch + yaw,  # M2 front-right, CCW
        throttle + roll + pitch + yaw,  # M3 rear-left,   CCW
        throttle + roll - pitch - yaw,  # M4 front-left,  CW
    ]
    hi = max(raw)
    if hi > 1.0:
        raw = [x / hi for x in raw]
    return {f"m{i + 1}": max(0.0, min(1.0, x)) for i, x in enumerate(raw)}
