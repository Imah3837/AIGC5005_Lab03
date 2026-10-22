import pytest

from recordsapp.models import Show


@pytest.fixture
def sample_show():
    return Show(
        name="Sample Show",
        language="English",
        genres=["Drama"],
        rating=8.0,
    )