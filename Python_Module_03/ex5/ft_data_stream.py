#!/usr/bin/env python3
import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "use", "release"
    ]

    while True:  # Infinite loop
        yield (random.choice(players), random.choice(actions))


# Process and shrink the list one by one until empty
def consume_event(events: list[tuple[str, str]]) \
        -> Generator[tuple[tuple[str, str],
                           list[tuple[str, str]]], None, None]:

    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)  # Remove that event from the list
        yield event, events


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()

    # 1000 events
    for i in range(1000):
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")

    # build list of 10
    events_list = [next(event_gen) for _ in range(10)]
    print(f"Built list of 10 events: {events_list}")

    # Take one event and show remaining events
    for event, remaining in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {remaining}")


if __name__ == "__main__":
    main()
