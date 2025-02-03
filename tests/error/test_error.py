from mktech.error import todo
import pytest


def test_todo() -> None:
    with pytest.raises(AssertionError):
        todo()


def test_todo_with_message() -> None:
    with pytest.raises(AssertionError):
        todo('message')
