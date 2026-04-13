#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    # Initial list
    players = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")

    # 1. Capitalize all names
    all_caps = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_caps}")

    # 2. Only already capitalized names
    caps_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {caps_only}")

    # 3. Dict comprehension (scores)
    scores = {name: random.randint(0, 1000) for name in all_caps}
    print(f"Score dict: {scores}")

    # 4. Average
    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    # 5. High scores
    high_scores = {
        name: score
        for name, score in scores.items()
        if score > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()