import functools
import inspect
from typing import (
    Any,
    Callable,
    Type,
    TypeAlias,
    Union,
)

import result
from result import is_err, is_ok
from result.result import TBE, E, P, R, T

__all__ = [
    'Err',
    'Ok',
    'Result',
    'as_result',
    'is_err',
    'is_ok',
    'replace_ok',
]


def replace_ok(ctx: Any, ok_value: Any) -> Any:
    raise NotImplementedError


class Ok(result.Ok[T]):
    def replace_ok(self, ok_value: R) -> 'Ok[R]':
        match self:
            case result.Err(_):
                raise NotImplementedError
            case result.Ok(_):
                return Ok(ok_value)
            case _:
                raise NotImplementedError

    def err_or_ok_none(self) -> 'Ok[None]':
        match self:
            case result.Err(_):
                raise NotImplementedError
            case result.Ok(_):
                return Ok(None)
            case _:
                raise NotImplementedError


class Err(result.Err[T]):
    def replace_ok(self, ok_value: R) -> 'Err[Exception]':
        match self:
            case result.Err(e):
                assert isinstance(e, Exception)

                return Err(e)
            case result.Ok(_):
                raise NotImplementedError
            case _:
                raise NotImplementedError

    def err_or_ok_none(self) -> 'Err[Exception]':
        match self:
            case result.Err(e):
                assert isinstance(e, Exception)

                return Err(e)
            case result.Ok(_):
                raise NotImplementedError
            case _:
                raise NotImplementedError


Result: TypeAlias = Union[Ok[T], Err[E]]


def as_result(
    *exceptions: Type[TBE],
) -> Callable[[Callable[P, R]], Callable[P, Result[R, TBE]]]:
    """
    Make a decorator to turn a function into one that returns a ``Result``.

    Regular return values are turned into ``Ok(return_value)``. Raised
    exceptions of the specified exception type(s) are turned into ``Err(exc)``.
    """
    if not exceptions or not all(
            inspect.isclass(exception) and issubclass(exception, BaseException)
            for exception in exceptions):
        raise TypeError("as_result() requires one or more exception types")

    def decorator(f: Callable[P, R]) -> Callable[P, Result[R, TBE]]:
        """
        Decorator to turn a function into one that returns a ``Result``.
        """
        @functools.wraps(f)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Result[R, TBE]:
            try:
                return Ok(f(*args, **kwargs))
            except exceptions as exc:
                return Err(exc)

        return wrapper

    return decorator
