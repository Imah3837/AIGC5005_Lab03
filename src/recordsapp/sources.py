import requests

from recordsapp.models import Show


class DataSource:
    """Download and convert television show data."""

    def fetch(self, url: str) -> list[Show]:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        return [
            Show(
                name=item.get("name"),
                language=item.get("language"),
                genres=item.get("genres"),
                rating=(
                    item.get("rating", {}).get("average")
                    if item.get("rating")
                    else None
                ),
            )
            for item in data
        ]
