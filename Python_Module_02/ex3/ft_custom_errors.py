#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")

    errors_to_test = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]

    for err in errors_to_test:
        try:
            raise err
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    test_custom_errors()
    print("All custom error types work correctly!")
