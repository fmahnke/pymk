from typing import Any, NoReturn, TypeAlias, TypeVar

import result
from result import Err, Ok, is_err, is_ok

__all__ = ['Err', 'Error', 'Ok', 'Result', 'is_err', 'is_ok']

T = TypeVar('T')

Result: TypeAlias = result.Result[T, Exception]


class Error(Exception):
    def __init__(
        self,
        message: str | None = None,
        cause: Any = None,
        *args: Any,
        **kwargs: Any
    ) -> None:
        self.message: str | None = message or self.__class__.__name__

        super().__init__(*args, **kwargs)
        self.__cause__ = cause

    def __str__(self) -> str:
        result = f'Error: {self.message}'

        if self.__cause__ is not None:
            result += f'\nCause: {self.__cause__}'

        return result


class ParseError(Exception):
    pass


def todo(message: str = 'not implemented') -> NoReturn:
    raise AssertionError(f'TODO: {message}')
