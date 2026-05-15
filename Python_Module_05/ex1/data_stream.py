#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


# 1. The Blueprint
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


# 2. The Workers (Helper Funcs)
# Numeric
class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):  # and not isinstance(data, bool)
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


# 3. The Manager
class DataStream:

    def __init__(self) -> None:
        # A list to store the registered processor objects
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    handled = True
                    break

            if not handled:
                print(f"Error: No processor found for element: {item}")

    def print_processors_stats(self) -> None:
        print("--- Processor Statistics ---")
        for proc in self.processors:
            # __class__.__name__ gets the string name of the class
            count = len(proc._storage)
            print(f"{proc.__class__.__name__}: {count} items in storage")
        print("----------------------------")


# Testing
if __name__ == "__main__":
    # 1. SETUP
    # Create the Manager (DataStream)
    ds = DataStream()

    # Create and register the Workers
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    ds.register_processor(num_proc)
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    #  2. DEFINE THE STREAM
    # A mix of data types to test the "routing"
    stream_data = [
        42,                            # Should go to Numeric
        "Python is cool",              # Should go to Text
        {"user": "admin", "op": "1"},  # Should go to Log
        [1.1, 2.2],                    # Should go to Numeric (list)
        "Final message",               # Should go to Text
        True                           # True = 1, Should go to Numeric
    ]

    # 3. RUN THE PROCESSING
    print(">>> Processing the data stream...")
    ds.process_stream(stream_data)

    # 4. SHOW STATISTICS
    print("\n>>> Current Statistics:")
    ds.print_processors_stats()

    # 5. CONSUME AND OUTPUT
    print("\n>>> Consuming elements from processors:")
    for p in [num_proc, text_proc, log_proc]:
        try:
            status, data = p.output()
            print(
                f"[{p.__class__.__name__}]"
                f"Output: {data} (Status: {status})"
                )
        except Exception as e:
            print(f"[{p.__class__.__name__}] Error: {e}")

    # 6. FINAL STATS
    print("\n>>> Updated Statistics (after consumption):")
    ds.print_processors_stats()
