from collections.abc import Callable
import functools
import time
from typing import Any


# Spell Timer Decorator

def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Measure and print the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


# Parameterized Power Validator Decorator

def power_validator(
        min_power: int
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Return a decorator that validates a spell's minimum power level."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Detect power from positional arguments or keyword arguments
            # If applied to a method, args[0] is 'self', so power is args[1]
            if len(args) > 1 and isinstance(args[1], int):
                power = args[1]
            elif args and isinstance(args[0], int):
                power = args[0]
            else:
                power = kwargs.get("power", 0)

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


# Retry Spell Decorator

def retry_spell(
        max_attempts: int
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Return a decorator that retries a function if it raises an exception."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


# MageGuild Class Integration

class MageGuild:
    """Class representing a guild of mages managing spells"""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check if a mage's name is valid (>= 3 chars, letters/spaces only)"""
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Execute a spell casting if the minimum power threshold is met."""
        return f"Successfully cast {spell_name} with {power} power"


# Execution and Demonstration
if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)  # Simulate small delay
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise ValueError("Wild magic fluctuation!")

    print(f"Waaaaaaagh spelled ! -> {unstable_spell()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("G1"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
