from datetime import date, timedelta
from itertools import islice, takewhile
from typing import Iterator

def recurring_task_dates(start: date, interval_days: int) -> Iterator[date]:
    current = start
    while True:
        yield current
        current = current + timedelta(days=interval_days)

def next_occurrences(start: date, interval_days: int, count: int) -> tuple[date, ...]:
    return tuple(islice(recurring_task_dates(start, interval_days), count))

def occurrences_before(start: date, interval_days: int, limit: date) -> tuple[date, ...]:
    return tuple(takewhile(lambda d: d < limit, recurring_task_dates(start, interval_days)))
