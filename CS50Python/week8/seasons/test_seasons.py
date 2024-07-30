import pytest
from seasons import validate
from seasons import math_it
from datetime import date
import datetime

def test_A():
    with pytest.raises(SystemExit):
        validate("1999 01 01")






