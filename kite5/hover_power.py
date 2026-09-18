from __future__ import annotations

import argparse
import math

RHO = 1.225


def induced_power_w(thrust_n: float, area_total_m2: float) -> float:
    if area_total_m2 <= 0 or thrust_n <= 0:
        raise ValueError("thrust and area must be > 0")
    return thrust_n**1.5 / math.sqrt(2 * RHO * area_total_m2)


def report(thrust_g: float, disk_cm: float, fom: float = 0.65) -> dict:
    thrust_n = thrust_g / 1000.0 * 9.80665
    radius_m = (disk_cm / 100.0) / 2.0
    area_m2 = 4 * math.pi * radius_m * radius_m
    p_induced_w = induced_power_w(thrust_n, area_m2)
    p_electrical_w = p_induced_w / fom
    return {
        "thrust_g": thrust_g,
        "thrust_n": thrust_n,
        "area_m2": area_m2,
        "p_induced_w": p_induced_w,
        "p_electrical_w": p_electrical_w,
        "current_4s_a": p_electrical_w / 14.8,
        "fom": fom,
    }


def print_report(r: dict) -> None:
    print(f"AUW           {r['thrust_g']:.0f} g  ({r['thrust_n']:.2f} N)")
    print(f"4 × disk area {r['area_m2']:.4f} m^2")
    print(f"P_induced     {r['p_induced_w']:.1f} W")
    print(f"P_electrical  {r['p_electrical_w']:.1f} W   (FOM={r['fom']})")
    print(f"4S current ~  {r['current_4s_a']:.1f} A   (pack at 14.8 V)")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--thrust-g", type=float, default=497.0)
    p.add_argument("--disk-cm", type=float, default=12.7)
    p.add_argument("--fom", type=float, default=0.65)
    args = p.parse_args()
    print_report(report(args.thrust_g, args.disk_cm, args.fom))


if __name__ == "__main__":
    main()
