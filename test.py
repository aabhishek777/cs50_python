from pytest import Package
from hi import square


def test_square():
    assert square(3)==9

print("hi")