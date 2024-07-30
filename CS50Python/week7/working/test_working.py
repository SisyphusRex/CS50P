from working import convert
import pytest

def test_A():
    try:
        convert("9AM to 5PM")
    except ValueError:
        pytest.pass()

def test_B():
    try:
        convert("5:80 AM to 9:00 PM")
    except ValueError:
        pytest.pass()

def test_C():
    assert "21:00 to 05:00" == convert("9:00 PM to 5:00 AM")

