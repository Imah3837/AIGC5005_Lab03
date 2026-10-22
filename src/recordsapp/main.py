import requests

from recordsapp import (
    OUTPUT_PATH,
    SOURCE_URL,
    AverageRatingByLanguage,
    DataSource,
    ReportWriter,
    ShowsPerGenre,
)


def build_summary(records):
    """Run each aggregation and combine the results."""
    summary = {
        "source_url": SOURCE_URL,
        "records_processed": len(records),
    }

    aggregations = [
        ShowsPerGenre(),
        AverageRatingByLanguage(),
    ]

    for aggregation in aggregations:
        summary[aggregation.name] = aggregation.compute(records)

    return summary


def main():
    """Download, process, and save the television show data."""
    try:
        records = DataSource().fetch(SOURCE_URL)

        if len(records) < 50:
            print("The API returned fewer than 50 records.")
            return

        summary = build_summary(records)
        ReportWriter().write(summary, OUTPUT_PATH)

        print(f"Processed {len(records)} records.")
        print(f"Summary written to {OUTPUT_PATH}")

    except requests.RequestException:
        print(
            "Could not download the records. "
            "Please check your internet connection."
        )


if __name__ == "__main__":
    main()