#!/usr/bin/env python3
import sys

def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, qty_str = arg.split(":", 1)

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty = int(qty_str)
            if qty < 0:
                raise ValueError("quantity must be non-negative")

            inventory[item] = qty

        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    return inventory


def print_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total = sum(inventory.values())

    print(f"Total quantity of the {len(inventory)} items: {total}")

    if total == 0:
        print("Inventory is empty.")
        return

    for item, qty in inventory.items():
        percent = (qty / total) * 100
        print(f"Item {item} represents {percent:.1f}%")

    most_item = max(inventory, key=inventory.get)
    least_item = min(inventory, key=inventory.get)

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
    )


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])
    print_inventory(inventory)

    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()