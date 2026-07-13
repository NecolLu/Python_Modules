from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import (  # type: ignore
    BaseModel,
    Field,
    ValidationError,
    model_validator,
)


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    # String, 5-15 characters
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime

    # String, 3-100 characters
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType

    # Float, 0.0-10.0 scale
    signal_strength: float = Field(ge=0.0, le=10.0)

    # Integer, 1-1440 (max 24 hours)
    duration_minutes: int = Field(ge=1, le=1440)

    # Integer, 1-100 people
    witness_count: int = Field(ge=1, le=100)

    # Optional string, max 500 characters
    message_received: Optional[str] = Field(default=None, max_length=500)

    # Boolean, defaults to False
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        # Rule 1: Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        # Rule 2: Physical contact reports must be verified
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Rule 3: Telepathic contact requires at least 3 witnesses
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )

        # Rule 4: Strong signals (> 7.0) should include received messages
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
                )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    # 1. Testing a Valid Contact Report
    valid_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2026-06-03T01:30:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False
    }

    try:
        contact = AlienContact(**valid_data)
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")
    except ValidationError as e:
        print(f"Unexpected Error: {e}")

    print("======================================")

    # 2. Testing an Invalid Contact Report
    invalid_telepathic = {
        "contact_id": "AC_2026_999",
        "timestamp": datetime.now(),
        "location": "Mount Shasta, California",
        "contact_type": "telepathic",
        "signal_strength": 3.0,
        "duration_minutes": 10,
        "witness_count": 1,  # Fails: Needs at least 3
        "is_verified": True
    }

    print("Expected validation error:")
    try:
        AlienContact(**invalid_telepathic)
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
