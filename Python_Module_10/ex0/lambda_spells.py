from typing import Any


# Sort magical artifacts by power level in descending order
def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


# Filter mages who have a power level greater than or equal to min_power
def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


# Transform spell names by adding a '* ' prefix and ' *' suffix
def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


# Calculate the maximum, minimum, and average power levels of the mages
def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    # Pass the lambda directly into map()
    powers = list(map(lambda x: x["power"], mages))
    max_p = max(powers)
    min_p = min(powers)
    avg_p = round(sum(powers) / len(powers), 2)

    return {"max_power": max_p, "min_power": min_p, "avg_power": avg_p}


# Demonstration and local testing[cite: 1]
if __name__ == "__main__":
    sample_artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "Focus"},
        {"name": "Fire Staff", "power": 92, "type": "Weapon"},
        {"name": "Shadow Robe", "power": 78, "type": "Armor"},
    ]

    sample_mages = [
        {"name": "Alex", "power": 90, "element": "Fire"},
        {"name": "Jordan", "power": 75, "element": "Water"},
        {"name": "Riley", "power": 85, "element": "Earth"},
    ]

    sample_spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(sample_artifacts)
    if len(sorted_artifacts) >= 2:
        print(
            f"{sorted_artifacts[0]['name']} "
            f"({sorted_artifacts[0]['power']} power) "
            f"comes before {sorted_artifacts[1]['name']} "
            f"({sorted_artifacts[1]['power']} power)"
        )

    print("\nTesting spell transformer...")
    transformed = spell_transformer(sample_spells)
    print(" ".join(transformed))

    print("\nTesting power filter and stats...")
    filtered_mages = power_filter(sample_mages, 80)
    print(f"Mages with power >= 80: {[m['name'] for m in filtered_mages]}")

    stats = mage_stats(sample_mages)
    print(f"Stats: {stats}")
