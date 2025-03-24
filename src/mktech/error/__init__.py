from typing import TypeAlias, TypeVar

import result
from result import Err, Ok, is_err, is_ok

T = TypeVar('T')

Result: TypeAlias = result.Result[T, Exception]

__all__ = ['Err', 'Ok', 'Result', 'is_err', 'is_ok']


class ParseError(Exception):
    pass


def todo(message: str = 'not implemented') -> None:
    raise AssertionError(f'TODO: {message}')
