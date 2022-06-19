from src.app import add
from src import app

def test_add():
    assert add(3, 2) == 5


def test_sub():
    assert app.sub(3, 2) == 1


def test_mult():
    assert app.mult(3, 2) == 6
