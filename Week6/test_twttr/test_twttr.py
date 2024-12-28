import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("This is a test") == "Ths s  tst"

def test_shorten_num():
    assert shorten("1") == "1"
    assert shorten("I have 3 siblings") == " hv 3 sblngs"

def test_shorten_punc():
    assert shorten("I love you!!!") == " lv y!!!"