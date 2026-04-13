#!/usr/bin/env python3
import random


def gen_player_achievements(all_achievements: list[str]) -> set[str]:
    count = random.randint(3, 7)
    return set(random.sample(all_achievements, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    all_achievements: list[str] = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder"
    ]

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(all_achievements),
        "Bob": gen_player_achievements(all_achievements),
        "Charlie": gen_player_achievements(all_achievements),
        "Dylan": gen_player_achievements(all_achievements),
    }

    # Print each player
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    # All distinct achievements (union)
    all_sets = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_sets}")

    # Common achievements
    common = set(all_achievements)
    for ach in players.values():
        common = common.intersection(ach)

    print(f"Common achievements: {common}")

    # Only each player has
    print()
    for name, ach in players.items():
        others = set().union(*[v for k, v in players.items() if k != name])
        unique = ach.difference(others)
        print(f"Only {name} has: {unique}")

    # Missing achievements per player
    print()
    full_set = set(all_achievements)

    for name, ach in players.items():
        missing = full_set.difference(ach)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()