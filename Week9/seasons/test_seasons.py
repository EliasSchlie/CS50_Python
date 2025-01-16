import pytest
from seasons import getMinTillNowInWords, getBirthday
from datetime import date

def test_getBirthday():
    assert getBirthday("2000-01-01") == date(2000, 1, 1)
    assert getBirthday("2019-11-20") == date(2019, 11, 20)

def test_getBirthday_error():
    with pytest.raises(SystemExit):
	    getBirthday("12-May-2002")
    with pytest.raises(SystemExit):
	    getBirthday("12 May 2002")
    with pytest.raises(SystemExit):
	    getBirthday("2000-02-30")
		
def test_getMinTillNowInWords():
    assert getMinTillNowInWords(date.today()) == "Zero minutes"
    assert getMinTillNowInWords(date(date.today().year, date.today().month, date.today().day-1)) == "One thousand, four hundred forty minutes"
    assert getMinTillNowInWords(date(date.today().year-2, date.today().month, date.today().day)) == "One million, fifty-two thousand, six hundred forty minutes"
    assert getMinTillNowInWords(date(date.today().year-1, date.today().month, date.today().day)) == "Five hundred twenty-seven thousand forty minutes"