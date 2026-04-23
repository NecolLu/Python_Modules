#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")

    all_caps = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_caps}")

    caps_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {caps_only}")

# 	caps_only = []
# 	for name in players:
#     if name[0].isupper():
#         caps_only.append(name)

    scores = {name: random.randint(0, 1000) for name in all_caps}
    print(f"Score dict: {scores}")

    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    high_scores = {
        name: score
        for name, score in scores.items()
        if score > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

# List comprehension = [(expression) for (item) in (iterable) if (condition)]
# Dict comprehension = {key: value for (item) in (iterable) if (condition)}
