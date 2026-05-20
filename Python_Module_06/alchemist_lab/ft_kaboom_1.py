print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION\n")

try:
    # This triggers the circular execution crash
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(dark_spell_record("Necromancy", "bats, frogs"))
except ImportError as e:
    import traceback
    traceback.print_exc()
