from datetime import date
from core.recurring import next_occurrences, occurrences_before

def test_next_occurrences_returns_exact_count():
    result = next_occurrences(start=date(2026, 1, 1), interval_days=7, count=3)
    assert result == (date(2026, 1, 1), date(2026, 1, 8), date(2026, 1, 15))

def test_next_occurrences_with_zero_count_is_empty():
    assert next_occurrences(start=date(2026, 1, 1), interval_days=7, count=0) == ()

def test_occurrences_before_stops_at_the_limit():
    result = occurrences_before(start=date(2026, 1, 1), interval_days=10, limit=date(2026, 1, 25))
    assert result == (date(2026, 1, 1), date(2026, 1, 11), date(2026, 1, 21))
