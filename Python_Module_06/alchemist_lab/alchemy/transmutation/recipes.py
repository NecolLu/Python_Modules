# ABSOLUTE IMPORT: Grabs Air from the alchemy package elements
from alchemy.elements import create_air

# RELATIVE IMPORT: Goes up one folder to get the strength potion
from ..potions import strength_potion

# ROOT IMPORT: Grab the root elements file directly by name
import elements as root_elements


def lead_to_gold() -> str:
    air = create_air()
    potion = strength_potion()
    # Use the root_elements module to get fire
    fire = root_elements.create_fire()

    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' and '{potion}' "
        f"mixed with '{fire}'"
    )
