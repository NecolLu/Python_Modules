from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    # We can explicitly use the capability method here for testing
    if hasattr(base, 'heal'):
        print(base.heal())

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if hasattr(evolved, 'heal'):
        print(evolved.heal())


def test_transform() -> None:
    print("\nTesting Creature with transform capability")
    factory = TransformCreatureFactory()

    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if hasattr(base, 'transform') and hasattr(base, 'revert'):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if hasattr(evolved, 'transform') and hasattr(evolved, 'revert'):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    test_healing()
    test_transform()
