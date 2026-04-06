#!/usr/bin/env python3

class Plant:
    """Base Plant class with analytics."""

    class _Stats:
        """Nested class to track statistics."""

        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def inc_grow(self) -> None:
            self._grow_calls += 1

        def inc_age(self) -> None:
            self._age_calls += 1

        def inc_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant._Stats()

    def show(self) -> None:
        self._stats.inc_show()
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def grow(self) -> None:
        self._stats.inc_grow()
        self._height += 8.0

    def age_one_day(self) -> None:
        self._stats.inc_age()
        self._age += 1

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


# ================= FLOWER =================
class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


# ================= TREE =================
class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def display_stats(self) -> None:
        super().display_stats()
        print(f"{self._shade_calls} shade")


# ================= SEED =================
class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


# ================= GLOBAL FUNCTION =================
def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


# ================= MAIN =================
def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_year(400)}")
    print()

    # Flower
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print()

    # Tree
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print()

    # Seed
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_one_day()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)
    print()

    # Anonymous
    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_plant_stats(unknown)


if __name__ == "__main__":
    ft_garden_analytics()
