import pytest

from functions import add, add_list


def test_add():
    result = add(1, 2)
    assert result == 3


def test_add_none():
    with pytest.raises(TypeError):
        add(1, None)  # type: ignore


def test_add_list():
    result = add_list([1, 2, 3])
    assert result == 6
