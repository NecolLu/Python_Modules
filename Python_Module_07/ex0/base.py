from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, element_type: str) -> None:
        self.name = name
        self.element_type = element_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.element_type} type Creature"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass
