def validate_ingredients(ingredients: str) -> str:
    # Validates ingredients against the light spellbook locally
    # LOCAL IMPORT - Safely breaks the loop
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    items = [item.strip().lower() for item in ingredients.split(",")]

    for item in items:
        if item in allowed:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
