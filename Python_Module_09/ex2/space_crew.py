from datetime import datetime
from enum import Enum
from typing import List
from pydantic import (  # type:ignore
    BaseModel,
    Field,
    ValidationError,
    model_validator
)


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety_rules(self) -> 'SpaceMission':
        # Rule 1: Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # Rule 2 & 4: Safety audits checking each crew member
        has_leadership = False
        experienced_count = 0

        for member in self.crew:
            # Rule 4: All crew members must be active
            if not member.is_active:
                raise ValueError(f"Crew member {member.name} is inactive")

            # Tracking Rule 2 (Leadership)
            if member.rank in (Rank.CAPTAIN, Rank.COMMANDER):
                has_leadership = True

            # Tracking Rule 3 (Experience)
            if member.years_experience >= 5:
                experienced_count += 1

        if not has_leadership:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )

        # Rule 3: Long missions (> 365 days)
        # need 50% experienced crew (5+ years)
        if self.duration_days > 365:
            crew_size = len(self.crew)
            if (experienced_count / crew_size) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) "
                    "need 50% experienced crew (5+ years)"
                    )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    # 1. Setup a Valid Mission
    valid_crew = [
        {
            "member_id": "CM01",
            "name": "Sarah Connor",
            "rank": "commander",
            "age": 45,
            "specialization": "Mission Command",
            "years_experience": 15
        },
        {
            "member_id": "CM02",
            "name": "John Smith",
            "rank": "lieutenant",
            "age": 32,
            "specialization": "Navigation",
            "years_experience": 6
        },
        {
            "member_id": "CM03",
            "name": "Alice Johnson",
            "rank": "officer",
            "age": 28,
            "specialization": "Engineering",
            "years_experience": 3
        }
    ]

    valid_mission_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2026-10-12T08:00:00",
        "duration_days": 900,  # > 365 days, requires 50% experienced
        "crew": valid_crew,
        "budget_millions": 2500.0
    }

    try:
        mission = SpaceMission.model_validate(valid_mission_data)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for m in mission.crew:
            print(f" - {m.name} ({m.rank.value}) - {m.specialization}")
    except ValidationError as e:
        print(f"Unexpected Error: {e}")

    print("=" * 40)

    # 2. Setup an Invalid Mission (Missing Leadership)
    invalid_crew = [
        {
            "member_id": "CM04",
            "name": "Bob Vance",
            "rank": "cadet",
            "age": 21,
            "specialization": "Logistics",
            "years_experience": 0
        }
    ]

    invalid_mission_data = {
        "mission_id": "M2026_LUNAR",
        "mission_name": "Lunar Survey",
        "destination": "Moon",
        "launch_date": datetime.now(),
        "duration_days": 30,
        "crew": invalid_crew,
        "budget_millions": 150.0
    }

    print("Expected validation error:")
    try:
        SpaceMission.model_validate(invalid_mission_data)
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
