#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 age: int, daily_growth: float) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.daily_growth = daily_growth

    def show(self) -> None:
        print(f"{self.name}: "
              f"{round(self.height, 1)}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.daily_growth

    def age_1(self) -> None:
        self.age += 1


def ft_plant_growth() -> None:
    plants = [
        Plant("Rose", 25, 30, 0.8),
        Plant("Sunflower", 80, 45, 1.2),
        Plant("Cactus", 15, 120, 0.2)
    ]
    initial_height = {plant.name: plant.height for plant in plants}
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        for plant in plants:
            plant.show()
            plant.grow()
            plant.age_1()
    print()
    for plant in plants:
        growth = round(plant.height - initial_height[plant.name], 1)
        print(f"{plant.name}'s Growth this week: {growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
