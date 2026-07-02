from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    # Validates ingredients against the dark spellbook globally.
    allowed = dark_spell_allowed_ingredients()
    items = [item.strip().lower() for item in ingredients.split(",")]

    # Check if at least one ingredient matches (case-insensitive)
    for item in items:
        if item in allowed:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
