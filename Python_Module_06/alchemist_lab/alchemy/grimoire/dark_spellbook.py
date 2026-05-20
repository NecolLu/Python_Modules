# GLOBAL IMPORT: This triggers the circular trap immediately upon loading
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    # Returns the forbidden ingredients for dark magic
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    # Tries to record a dark spell using global validation
    result = validate_ingredients(ingredients)
    if "VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
