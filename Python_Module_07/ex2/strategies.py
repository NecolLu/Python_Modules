from abc import ABC, abstractmethod
from ex0.base import Creature
from ex1.capabilities import HealCapability, TransformCapability
from ex2.exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        # Suitable for any Creature
        return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        # Suitable only for Creatures with transform capabilities
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}'"
                f"for this aggressive strategy"
            )

        # We temporarily cast/know it has these methods
        # due to our is_valid check
        # This matches the required output order: transform, attack, revert
        lines = [
            creature.transform(),  # type: ignore
            creature.attack(),
            creature.revert()      # type: ignore
        ]
        return "\n".join(lines)


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        # Suitable only for Creatures with healing capabilities
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}'"
                f"for this defensive strategy"
            )

        # This matches the required output order: attack, then heal
        lines = [
            creature.attack(),
            creature.heal()       # type: ignore
        ]
        return "\n".join(lines)
