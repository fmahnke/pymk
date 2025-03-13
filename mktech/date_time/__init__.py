from datetime import datetime, timedelta
from typing import TypeAlias

from result import Result

from mktech.error import Err, Ok, ParseError, todo

Duration: TypeAlias = timedelta


def _seconds_microseconds(seconds: str) -> tuple[int, int]:
    second_parts = seconds.split('.')

    seconds_out = int(second_parts[0])

    if len(second_parts) == 2:
        microseconds = int(second_parts[1][:6])
    else:
        microseconds = 0

    return seconds_out, microseconds


def parse_duration(
    duration: str | None
) -> Result[timedelta | None, ParseError]:
    result: Result[timedelta | None, ParseError]

    if duration is None:
        result = Ok(None)
    else:
        parts = duration.split(':')

        try:
            if len(parts) == 3:
                hour = int(parts[0])
                minute = int(parts[1])
                second_str = parts[2]
            elif len(parts) == 2:
                hour = 0
                minute = int(parts[0])
                second_str = parts[1]
            elif len(parts) == 1:
                hour = 0
                minute = 0
                second_str = parts[0]
            else:
                todo()
        except ValueError as e:
            return Err(ParseError(e))

        second, microsecond = _seconds_microseconds(second_str)

        # TODO ValueError when second not 0..59

        duration_datetime = datetime(
            1900,
            1,
            1,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond
        )

        result = Ok(duration_datetime - datetime(1900, 1, 1))

    return result
