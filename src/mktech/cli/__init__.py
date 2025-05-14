from typing import Any

import click
from pydanclick import from_pydantic as from_config

from mktech import log

__all__ = ['from_config', 'top']

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

top_command_args = {
    'context_settings': CONTEXT_SETTINGS,
    'no_args_is_help': True,
}


def top() -> Any:
    def decorator(func: Any, *args: Any, **kwargs: Any) -> Any:
        @click.command(**top_command_args)  # type: ignore[call-overload,misc]
        @click.option('-l', '--log-level', default='warning')
        def wrapper(log_level: str, *args: Any, **kwargs: Any) -> Any:
            log.init(log_level)

            func(*args, **kwargs)

        return wrapper

    return decorator
