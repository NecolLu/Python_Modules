#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
# class PlantError(Exception):
# its for creating own error type
# PlantError = your custom error name
# (Exception) = it inherits from Python’s built-in Exception class
# basically PlantError is a type of Exception


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "Lettuce"])
    print("Cleanup always happens, even with errors!")
