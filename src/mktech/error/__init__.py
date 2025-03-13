from typing import TypeAlias, TypeVar

import result
from result import Err, Ok

T = TypeVar('T')

Result: TypeAlias = result.Result[T, Exception]

__all__ = ['Err', 'Ok', 'Result']


class ParseError(Exception):
    pass


def todo(message: str = 'not implemented') -> None:
    raise AssertionError(f'TODO: {message}')
