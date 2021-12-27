import pytest

from columnar import columnar


def test_minimal_table():
    res = columnar([["some string"]])
    assert res == '|-----------|\n|some string|\n|-----------|\n'


def test_empty_table():
    with pytest.raises(TypeError) as exc_info:
        columnar(data=[])
    assert str(exc_info.value) == "'data' must be a list of lists. Got an empty list"


def test_empty_table_with_header():
    with pytest.raises(TypeError) as exc_info:
        columnar(data=[], headers=["User", "Message", "Zip"])
    assert str(exc_info.value) == "'data' must be a list of lists. Got an empty list"
