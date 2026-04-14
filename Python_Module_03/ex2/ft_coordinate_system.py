#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts: list[str] = raw.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)

        except ValueError as e:
            for part in parts:
                part = part.strip()
                try:
                    float(part)
                except ValueError:
                    print(f"Error on parameter '{part}': {e}")
                    break


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    return math.sqrt(
        (b[0] - a[0]) ** 2 +
        (b[1] - a[1]) ** 2 +
        (b[2] - a[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    p1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

    dist_center: float = distance(p1, (0.0, 0.0, 0.0))
    print(f"Distance to center: {round(dist_center, 4)}")

    print("Get a second set of coordinates")
    p2: tuple[float, float, float] = get_player_pos()

    dist_between: float = distance(p1, p2)
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
    )


if __name__ == "__main__":
    main()
