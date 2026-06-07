from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    # Sort magical artifacts by 'power' level in descending order
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    # Filter mages with power >= min_power
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    # Transform spell names by adding '* ' prefix and ' *' suffix
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    # Calculate max, min, and average power levels using lambdas
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_p = max(mages, key=lambda x: x["power"])["power"]
    min_p = min(mages, key=lambda x: x["power"])["power"]

    # Simple lambda to extract power values for processing
    get_powers = map(lambda x: x["power"], mages)
    avg_p = round(sum(get_powers) / len(mages), 2)

    return {"max_power": max_p, "min_power": min_p, "avg_power": avg_p}


if __name__ == "__main__":
    # Test cases mirroring the expected subject behavior
    print("Testing artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
    ]
    sorted_arts = artifact_sorter(artifacts)
    print(
        f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
        f"comes before {sorted_arts[1]['name']} "
        f"({sorted_arts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    print(" ".join(spell_transformer(spells)))
