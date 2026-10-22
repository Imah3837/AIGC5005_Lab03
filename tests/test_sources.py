import requests


def test_connection_error():
    err = requests.ConnectionError()
    assert isinstance(err, Exception)


def test_timeout_error():
    err = requests.Timeout()
    assert isinstance(err, Exception)