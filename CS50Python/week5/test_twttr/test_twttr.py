from twttr import shorten

def test_A():
    assert "A" not in shorten("YAet")
    assert "a" not in shorten("Yaet")
