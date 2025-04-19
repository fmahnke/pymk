from typing import NoReturn

from .error import Error, ParseError
from .subclass import (
    Err,
    Ok,
    Result,
    as_result,
    is_err,
    is_ok,
    replace_ok,
)

__all__ = [
    'Err',
    'Error',
    'Ok',
    'ParseError',
    'Result',
    'as_result',
    'is_err',
    'is_ok',
    'replace_ok',
    'todo',
]
'''
from .result import (
    Err,
    Ok,
    Result,
    as_result,
    is_err,
    is_ok,
    replace_ok,
)

__all__ = [
    'Err',
    'Error',
    'Ok',
    'ParseError',
    'Result',
    'as_result',
    'is_err',
    'is_ok',
    'replace_ok',
    'todo',
]
'''


def todo(message: str = 'not implemented') -> NoReturn:
    raise AssertionError(f'TODO: {message}')
