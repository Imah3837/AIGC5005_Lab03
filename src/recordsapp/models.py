class Show:
    """Represent one television show record."""

    def __init__(self, name, language, genres, rating):
        """Initialize and clean the television show data."""
        self.name = name if name else "Unknown"
        self.language = language if language else "Unknown"
        self.genres = genres if isinstance(genres, list) else []

        if isinstance(rating, (int, float)):
            self.rating = float(rating)
        else:
            self.rating = None

    @classmethod
    def from_dictionary(cls, data):
        """Create a Show object from an API dictionary."""
        rating_data = data.get("rating") or {}

        return cls(
            name=data.get("name"),
            language=data.get("language"),
            genres=data.get("genres", []),
            rating=rating_data.get("average"),
        )

    def __str__(self):
        """Return a readable representation of the show."""
        return f"{self.name} ({self.language})"
