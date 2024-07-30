from bank import value

def test_hello():
    assert 0 == value("hello")

def test_h():
    assert 20 == value("heck")

def test_other():
    assert 100 == value("yeet")
