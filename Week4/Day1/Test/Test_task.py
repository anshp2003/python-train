def add(a,b):
    return a+b

def test_add():
    result=add(7,5)
    assert result==12


import pytest

@pytest.fixture
def setup_data():
    return {"key": "value"}

def test_use_fixture(setup_data):
    assert setup_data["key"] == "value"


import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
])
def test_add(a, b, expected):
    assert a + b == expected


import pytest

@pytest.mark.skip(reason="This test is not ready yet")
def test_not_ready():
    assert 1 == 1

@pytest.mark.skipif(1 == 1, reason="This test is conditionally skipped")
def test_conditionally_skipped():
    assert 1 == 1


import pytest

@pytest.mark.xfail
def test_expected_failure():
    assert 1 == 2
