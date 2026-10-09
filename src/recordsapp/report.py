import json


class ReportWriter:
    """Write the completed summary to a JSON file."""

    def write(self, summary, path):
        """Save a summary dictionary as formatted JSON."""
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as file:
            json.dump(summary, file, indent=2)