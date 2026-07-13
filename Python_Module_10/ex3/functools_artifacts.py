import functools
import operator
from typing import Any, Callable


# Spell Reducer

def spell_reducer(spells: list[int], operation: str) -> int:
    # Reduce a list of spell powers using a specified operator
    if not spells:
        return 0

    op_map = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in op_map:
        raise ValueError(f"Unknown operation: {operation}")

    return int(functools.reduce(op_map[operation], spells))


# Partial Enchanter

def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    # Return a dictionary of specialized partial enchantment functions
    # Freeze power=50 and pre-fill individual element types
    fire_fn = functools.partial(base_enchantment, 50, "Fire")
    ice_fn = functools.partial(base_enchantment, 50, "Ice")
    lightning_fn = functools.partial(base_enchantment, 50, "Lightning")

    return {
        "fire": fire_fn,
        "ice": ice_fn,
        "lightning": lightning_fn
    }


#  Memoized Fibonacci

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    # Calculate the nth Fibonacci number using an LRU cache
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# Spell Dispatcher

@functools.singledispatch
def _base_dispatcher(spell: Any) -> str:
    # Fallback handler for unknown spell data types
    return "Unknown spell type"


@_base_dispatcher.register(int)
def _(spell: int) -> str:
    # Handle integer input as a damage spell
    return f"Damage spell: {spell} damage"


@_base_dispatcher.register(str)
def _(spell: str) -> str:
    # Handle string input as an enchantment
    return f"Enchantment: {spell}"


@_base_dispatcher.register(list)
def _(spell: list[Any]) -> str:
    # Handle list input as a multi-cast spell grouping
    return f"Multi-cast: {len(spell)} spells"


def spell_dispatcher() -> Callable[[Any], str]:
    # Return the single dispatch routing function entrypoint
    return _base_dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanter...")

    def generic_enchant(power: int, element: str, target: str) -> str:
        return f"{element} infusion ({power} status) applied to {target}"

    enchant_pool = partial_enchanter(generic_enchant)
    print(enchant_pool["fire"]("Sword"))
    print(enchant_pool["ice"]("Shield"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # Verify cache works behind the scenes
    print(f"Cache Performance Info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))
