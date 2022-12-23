from app import hello_world, home


def test_hello_world():
    assert hello_world() == "Hello World!"


def test_home():
    assert home() == "Home"
