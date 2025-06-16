from src.hello import greet


def test_greet():
    assert greet("Kachi") == "Hello, Kachi!"
