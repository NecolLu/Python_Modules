from alchemy.elements import create_air
from alchemy.potions import healing_potion, strength_potion
from alchemy import transmutation

# create an alias: 'heal' that points directly to the healing_potion func
heal = healing_potion

# We define __all__ to tell linters like flake8/mypy what is explicitly public
__all__ = ["create_air",
           "strength_potion",
           "heal",
           "transmutation",
           "grimoire"
           ]


# This magic custom function intercepts
# when someone tries to call alchemy.create_earth
def __getattr__(name: str) -> None:
    if name == "create_earth":
        raise AttributeError(
            "module 'alchemy' has no attribute 'create_earth'. "
            "Did you mean: 'create_air'?"
        )
    raise AttributeError(f"module 'alchemy' has no attribute '{name}'")
