def mix(throttle, roll, pitch, yaw):
    raw = [
        throttle - roll + pitch + yaw,
        throttle - roll - pitch - yaw,
        throttle + roll - pitch + yaw,
        throttle + roll + pitch - yaw,
    ]
    hi = max(raw)
    if hi > 1.0:
        raw = [x / hi for x in raw]
    return {f"m{i+1}": max(0.0, min(1.0, x)) for i, x in enumerate(raw)}
