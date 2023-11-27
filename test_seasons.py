from datetime import date
from seasons import convert_date
import pytest

def test_convert_date():
    assert convert_date("1997-09-14") == date(1997, 9, 14)
    assert convert_date("1999-06-25") == date(1999, 6, 25)
    with pytest.raises(SystemExit):
        convert_date("June 25, 1999")