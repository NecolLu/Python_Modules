from collections.abc import Callable


# Base Spells for Testing

def fireball(target: str, power: int) -> str:
    """Return a standard offensive spell description."""
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Return a standard restorative spell description."""
    return f"Heal restores {target} for {power} HP"


# Higher-Order Functions

def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    """Combine two spells into a single function returning a tuple."""
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combined_spell


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    """Return a new spell function where input power is multiplied."""
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    """Return a spell that only executes if condition returns True."""
    def gated_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return gated_spell


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    """Return a function that executes a list of spells sequentially."""
    def sequence_spell(target: str, power: int) -> list[str]:
        results = []
        for cast in spells:
            results.append(cast(target, power))
        return results
    return sequence_spell


#  Execution and Demonstration
if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res_fire, res_heal = combined("Dragon", 10)
    print(f"Combined spell result: {res_fire}, {res_heal}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original_output = fireball("Dragon", 10)
    amplified_output = mega_fireball("Dragon", 10)
    print(f"Original: 10 ({original_output})")
    print(f"Amplified: 30 ({amplified_output})")

    print("\nTesting conditional caster...")
    is_dragon: Callable[[str, int], bool] = (
        lambda target, power: target == "Dragon"
    )
    gated_fireball = conditional_caster(is_dragon, fireball)
    print(f"Targeting Dragon: {gated_fireball('Dragon', 15)}")
    print(f"Targeting Goblin: {gated_fireball('Goblin', 15)}")

    print("\nTesting spell sequence...")
    grimoire: list[Callable[[str, int], str]] = [fireball, heal, fireball]
    sequence = spell_sequence(grimoire)
    seq_results = sequence("Orc", 25)
    for i, result in enumerate(seq_results, 1):
        print(f"  Spell {i}: {result}")
