import requests

from .config import TIMEOUT
from .models import Show


class DataSource:
    """Download television show records from an API."""

    def fetch(self, url):
        """Download data and return a list of Show objects."""
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()

        data = response.json()

        return [Show.from_dictionary(item) for item in data]
