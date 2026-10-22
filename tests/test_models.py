import unittest

from recordsapp.models import Show


class TestShow(unittest.TestCase):
    """Test the Show model without using the network."""

    def test_valid_show(self):
        """Test creation with valid values."""
        show = Show(
            name="Example Show",
            language="English",
            genres=["Drama"],
            rating=8.5,
        )

        self.assertEqual(show.name, "Example Show")
        self.assertEqual(show.language, "English")
        self.assertEqual(show.genres, ["Drama"])
        self.assertEqual(show.rating, 8.5)

    def test_invalid_values_are_cleaned(self):
        """Test that missing or invalid values are cleaned."""
        show = Show(
            name=None,
            language=None,
            genres="Drama",
            rating="Not available",
        )

        self.assertEqual(show.name, "Unknown")
        self.assertEqual(show.language, "Unknown")
        self.assertEqual(show.genres, [])
        self.assertIsNone(show.rating)


if __name__ == "__main__":
    unittest.main()
