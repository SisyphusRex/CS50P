from um import count
import pytest

def test_A():
    assert count("yeet") == 0

def test_B():
    assert count("um") == 1

def test_C():
    assert count("yeet um") == 1

def test_D():
    assert count("yeet um.") == 1

def test_E():
    assert count("um yeet yum um") == 2

def test_F():
    assert count("UM") == 1
