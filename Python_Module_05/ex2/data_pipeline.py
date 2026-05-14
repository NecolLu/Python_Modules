#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any
from typing import Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


# 1. The Blueprint
class DataProcessor(ABC):
    def __init__(self):
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
        def is_valid_dict(d):
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


# Json
class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []

        for status, value in data:
            items.append(f'{{"status": {status}, "data": "{value}"}}')

        print("[" + ", ".join(items) + "]")


# CSV
class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("status,data")
        for status, value in data:
            print(f"{status},{value}")


# 3. The Manager
class DataStream:

    def __init__(self):
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        collected: list[tuple[int, str]] = []
        
        for proc in self.processors:
            # For each processor, try to grab 'nb' items
            for _ in range(nb):
                try:
                    # This will pop from storage until it's empty
                    item = proc.output()
                    collected.append(item)
                except Exception:
                    # If this specific processor runs out, move to the next one
                    break

        # Send the combined results to the plugin
        plugin.process_output(collected)


# Testing
if __name__ == "__main__":
    # 1. Initialize the DataStream (The Manager)
    ds = DataStream()

    # 2. Register Processors (The Specialists)
    # These will be stored in the DataStream's internal list
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    # 3. Define the Test Data
    # A mix of types to demonstrate polymorphic routing
    mixed_data = [
        42,                                   # Numeric
        "Hello World",                        # Text
        {"event": "login", "status": "ok"},   # Log
        [10.5, 20.0],                         # Numeric (List)
        "Data Pipelines are fun",             # Text
        {"error": "timeout", "code": "408"}   # Log
    ]

    # --- PART A: CSV EXPORT ---
    print(">>> [PHASE 1] Loading stream for CSV Export...")
    ds.process_stream(mixed_data)

    print("\n>>> Current Statistics (Before CSV Export):")
    ds.print_processors_stats()

    print("\n>>> Executing CSV Output Pipeline (nb=1)...")
    # This will take 1 item from EACH registered processor
    ds.output_pipeline(1, CSVExport())

    print("\n>>> Statistics after CSV Export (Items should be reduced):")
    ds.print_processors_stats()

    print("\n" + "="*40 + "\n")

    # --- PART B: JSON EXPORT ---
    # We RE-FILL the stream here because the previous pipeline call 
    # 'consumed' (popped) data out of the internal storage.
    print(">>> [PHASE 2] Re-filling stream for JSON Export...")
    ds.process_stream(mixed_data)

    print("\n>>> Executing JSON Output Pipeline (nb=2)...")
    # This will take up to 2 items from EACH processor
    # Because we refilled, the processors are populated again.
    ds.output_pipeline(2, JSONExport())

    print("\n>>> Final Statistics:")
    ds.print_processors_stats()
