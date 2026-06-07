from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.base import CreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    BattleStrategy,
    InvalidStrategyError,
)


def run_tournament(
    name: str, opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(f"Tournament {name}")

    # Format visual representation for the example match layout
    opp_names = [
        f"({fact.__class__.__name__.replace('CreatureFactory', '').replace('Factory', '')}+{strat.__class__.__name__.replace('Strategy', '')})"  # noqa: E501
        for fact, strat in opponents
    ]
    print(f"[ {', '.join(opp_names)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    # To avoid modifying state mid-loop, we pre-generate instances
    # We pair each generated creature with its selected tournament strategy
    participants = []
    for factory, strategy in opponents:
        participants.append((factory.create_base(), strategy))

    # Round-Robin match generator (everyone fights everyone else exactly once)
    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):
            c1, strat1 = participants[i]
            c2, strat2 = participants[j]

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                # Execute action sequences per their designated strategies
                print(strat1.act(c1))
                print(strat2.act(c2))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    # Setup Factories
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    # Setup Strategies
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    # Tournament 0 (Basic)
    run_tournament("0 (basic)", [(flame, normal), (healing, defensive)])
    print()

    # Tournament 1 (Error case)
    run_tournament("1 (error)", [(flame, aggressive), (healing, defensive)])
    print()

    # Tournament 2 (Multiple participants)
    run_tournament(
        "2 (multiple)",
        [
            (aqua, normal),
            (healing, defensive),
            (transform, aggressive),
        ],
    )
