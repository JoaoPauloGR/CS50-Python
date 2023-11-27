import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("4/3")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"