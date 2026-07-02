def light_spell_allowed_ingredients() -> list[str]:
    # Returns the pure ingredients for light magic
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # Records a light spell by importing the validator ONLY when called
    # LOCAL IMPORT - Hidden inside the function to break the circular curse
    from .light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if "VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
