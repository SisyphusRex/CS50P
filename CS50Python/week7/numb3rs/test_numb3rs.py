from numb3rs import validate

def test_A():
    assert False == validate("255.255.255.255.0")
    assert False == validate("256.255.255.0")
    assert False == validate("255.256.255.0")

def test_B():
    assert True == validate("255.255.255.0")
