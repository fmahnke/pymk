from typing import (
    Any,
    TypeVar,
)

import result
from result import Err, Ok, Result, as_result, is_err, is_ok

__all__ = ['Err', 'Ok', 'Result', 'as_result', 'is_err', 'is_ok', 'replace_ok']

T = TypeVar('T')


def replace_ok(
    ctx: Result[T, Exception],
    ok_value: Any,
) -> Result[Any, Exception]:
    match ctx:
        case result.Err(e):
            assert isinstance(e, Exception)

            return Err(e)
        case result.Ok(v):
            return Ok(v)
        case _:
            raise NotImplementedError


def err_or_ok_none(ctx: Result[T, Exception]) -> Result[None, Exception]:
    match ctx:
        case result.Err(e):
            assert isinstance(e, Exception)

            return Err(e)
        case result.Ok(_):
            return Ok(None)
        case _:
            raise NotImplementedError
