class Aggregation:
    """Base class for television show aggregations."""

    name = "aggregation"

    def compute(self, records):
        """Calculate a result from the supplied records."""
        raise NotImplementedError("Subclasses must implement compute().")


class ShowsPerGenre(Aggregation):
    """Count the number of shows in each genre."""

    name = "shows_per_genre"

    def compute(self, records):
        """Return the number of shows in each genre."""
        genre_counts = {}

        for show in records:
            for genre in show.genres:
                genre_counts[genre] = genre_counts.get(genre, 0) + 1

        return genre_counts


class AverageRatingByLanguage(Aggregation):
    """Calculate the average rating for each language."""

    name = "average_rating_by_language"

    def compute(self, records):
        """Return the average rating for every language."""
        ratings = {}

        for show in records:
            if show.language != "Unknown" and show.rating is not None:
                if show.language not in ratings:
                    ratings[show.language] = []

                ratings[show.language].append(show.rating)

        return {
            language: sum(values) / len(values)
            for language, values in ratings.items()
        }