#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = value
        print(f"Height updated: {value}cm")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = value
        print(f"Age updated: {value} days")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    plant.show()
    print()

    # Valid updates
    plant.set_height(25)
    plant.set_age(30)
    print()

    # Invalid updates
    plant.set_height(-5)
    plant.set_age(-10)

    print()
    print("Current state:", end=" ")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
