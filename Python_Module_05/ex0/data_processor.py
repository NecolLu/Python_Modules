#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise Exception("No data to output")

        data = self._storage.pop(0)
        return (0, data)


# Numeric

class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            # isinstance is a built-in function in Python
            # checking if the variable data is either an int or float
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Invalid numeric data")

        if isinstance(data, list):
            self._storage.extend([str(x) for x in data])
        else:
            self._storage.append(str(data))


# Text

class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Invalid text data")

        if isinstance(data, list):
            self._storage.extend(data)
        else:
            self._storage.append(data)


# Log

class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def is_valid_dict(d: Any) -> bool:
            return (
                isinstance(d, dict)
                and all(
                    isinstance(k, str) and
                    isinstance(v, str)
                    for k, v in d.items()
                    )
            )

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(d) for d in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Invalid log data")

        def convert(d: dict[str, str]) -> str:
            return ", ".join(f"{k}={v}" for k, v in d.items())

        if isinstance(data, list):
            for d in data:
                self._storage.append(convert(d))
        else:
            self._storage.append(convert(data))


# Testing

if __name__ == "__main__":
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    # Validate tests
    print(num.validate(10))          # True
    print(num.validate("abc"))       # False

    print(text.validate("hello"))    # True
    print(text.validate([1, 2]))     # False

    print(log.validate({"a": "1"}))  # True
    print(log.validate({"a": 1}))    # False

    # Ingest valid data
    num.ingest(10)
    num.ingest([1, 2.5])

    text.ingest("hello")
    text.ingest(["world", "python"])

    log.ingest({"user": "alice"})
    log.ingest([{"id": "1"}, {"id": "2"}])

    # Output data
    print(num.output())
    print(text.output())
    print(log.output())

    # Force error
    num.ingest("wrong type")  # should raise TypeError
