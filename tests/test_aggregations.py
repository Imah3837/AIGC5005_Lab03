from recordsapp.aggregations import (
    AverageRatingByLanguage,
    ShowsPerGenre,
)
from recordsapp.models import Show


def test_shows_per_genre():
    records = [
        Show("A", "English", ["Drama"], 8.0),
        Show("B", "English", ["Drama"], 7.0),
        Show("C", "French", ["Comedy"], 9.0),
    ]

    result = ShowsPerGenre().compute(records)

    assert result["Drama"] == 2
    assert result["Comedy"] == 1


def test_average_rating_by_language():
    records = [
        Show("A", "English", [], 8.0),
        Show("B", "English", [], 6.0),
    ]

    result = AverageRatingByLanguage().compute(records)

    assert result["English"] == 7.0


def test_empty_records():
    result = ShowsPerGenre().compute([])

    assert result == {}