from twttr import shorten

def test_shorten():
    assert shorten("mississipi") == "mssssp"
    assert shorten("HElp") == "Hlp"
    assert shorten("H3lp") == "H3lp"
    assert shorten("hi!") == "h!"
