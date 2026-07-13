from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError  # type: ignore


class SpaceStation(BaseModel):
    # String, 3-10 characters
    station_id: str = Field(min_length=3, max_length=10)

    # String, 1-50 characters
    name: str = Field(min_length=1, max_length=50)

    # Integer, 1-20 people
    crew_size: int = Field(ge=1, le=20)

    # Float, 0.0-100.0 percent
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)

    # DateTime field
    last_maintenance: datetime

    # Boolean, defaults to True
    is_operational: bool = Field(default=True)

    # Optional string, max 200 characters
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("-" * 30)

    # 1. Testing a Valid Space Station Instance
    valid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        # String auto-converted to datetime
        "last_maintenance": "2026-06-03T12:00:00",
        "notes": "All systems nominal."
    }

    try:
        station = SpaceStation(**valid_data)
        print("Valid station created successfully!")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(
            f"Status: "
            f"{'Operational' if station.is_operational else 'Non-Operational'}"
            )
        print(f"Notes: {station.notes}")
    except ValidationError as e:
        print(f"Unexpected Validation Error: {e}")

    print("\n" + "-" * 30 + "\n")

    # 2. Testing an Invalid Space Station Instance (Crew Size > 20)
    invalid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 25,  # Violates le=20
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": datetime.now()
    }

    print("Attempting to create an invalid station (crew_size = 25)...")
    try:
        SpaceStation(**invalid_data)
    except ValidationError as e:
        print("Expected validation error caught!")
        # Print the readable error message layout
        print(e)


if __name__ == "__main__":
    main()
