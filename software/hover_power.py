#!/usr/bin/env python3
from __future__ import annotations
import argparse, math
RHO = 1.225

def induced_power_w(thrust_n, area_total_m2):
    if area_total_m2 <= 0 or thrust_n <= 0:
        raise ValueError("thrust and area must be > 0")
    return thrust_n ** 1.5 / math.sqrt(2 * RHO * area_total_m2)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--thrust-g", type=float, default=497.0)
    p.add_argument("--disk-cm", type=float, default=12.7)
    p.add_argument("--fom", type=float, default=0.65)
    args = p.parse_args()
    t = args.thrust_g / 1000.0 * 9.80665
    r = (args.disk_cm / 100.0) / 2.0
    area = 4 * math.pi * r * r
    p_i = induced_power_w(t, area)
    p_elec = p_i / args.fom
    print(f"AUW           {args.thrust_g:.0f} g  ({t:.2f} N)")
    print(f"4 × disk area {area:.4f} m^2")
    print(f"P_induced     {p_i:.1f} W")
    print(f"P_electrical  {p_elec:.1f} W   (FOM={args.fom})")
    print(f"4S current ~  {p_elec / 14.8:.1f} A   (pack at 14.8 V)")

if __name__ == "__main__":
    main()
