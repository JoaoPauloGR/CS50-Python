from bank import value

def test_bank():
    assert value("Hello") == 0
    assert value("hi") == 20
    assert value("What's up") == 100
