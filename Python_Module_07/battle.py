from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(fact_a: CreatureFactory, fact_b: CreatureFactory) -> None:
    print("Testing battle")
    c1 = fact_a.create_base()
    c2 = fact_b.create_base()

    print(c1.describe())
    print("VS.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()

    test_factory(flame_fact)
    test_factory(aqua_fact)
    test_battle(flame_fact, aqua_fact)
