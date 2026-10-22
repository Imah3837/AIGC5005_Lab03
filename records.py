import json
from pathlib import Path

import requests

SOURCE_URL = "https://api.tvmaze.com/shows?page=0"
OUTPUT = Path("summary.json")


def fetch_records(url):
    """Download the records and return them as Python objects."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def shows_per_genre(records):
    """Count the number of shows in each genre."""
    genre_counts = {}

    for show in records:
        genres = show.get("genres", [])

        for genre in genres:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts


def average_rating_by_language(records):
    """Calculate the average rating for each language."""
    ratings = {}

    for show in records:
        language = show.get("language")
        rating = show.get("rating", {}).get("average")

        if language and isinstance(rating, (int, float)):
            if language not in ratings:
                ratings[language] = []

            ratings[language].append(rating)

    averages = {
        language: sum(values) / len(values) for language, values in ratings.items()
    }

    return averages


def build_summary(records):
    """Combine the aggregations into one dictionary."""
    return {
        "source_url": SOURCE_URL,
        "records_processed": len(records),
        "shows_per_genre": shows_per_genre(records),
        "average_rating_by_language": average_rating_by_language(records),
    }


def write_summary(summary, path):
    """Write the summary to a JSON file."""
    with path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)


def main():
    """Download, process, and save the TV show data."""
    try:
        records = fetch_records(SOURCE_URL)

        if len(records) < 50:
            print("The API returned fewer than 50 records.")
            return

        summary = build_summary(records)
        write_summary(summary, OUTPUT)

        print(f"Processed {len(records)} records.")
        print(f"Summary written to {OUTPUT}")

    except requests.RequestException:
        print("Could not download the records. Please check your internet connection.")


if __name__ == "__main__":
    main()
