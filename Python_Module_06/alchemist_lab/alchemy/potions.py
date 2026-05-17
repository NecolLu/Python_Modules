# Import from the root folder's elements.py
import elements

# Import from alchemy/elements.py (the dot = "current package folder")
from .elements import create_air, create_earth


def healing_potion() -> str:
    # healing potion using earth and air
    earth = create_earth()
    air = create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    # strength potion using fire and water
    fire = elements.create_fire()
    water = elements.create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
