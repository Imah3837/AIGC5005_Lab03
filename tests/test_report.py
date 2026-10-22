import json

from recordsapp.report import ReportWriter


def test_report_written(tmp_path):
    summary = {"records_processed": 10}

    path = tmp_path / "summary.json"

    ReportWriter().write(summary, path)

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    assert data["records_processed"] == 10