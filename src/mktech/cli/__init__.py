from typing import Callable

import click

from mktech import log

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

top_command_args = {
    'context_settings': CONTEXT_SETTINGS,
    'no_args_is_help': True,
}


def top() -> Callable:
    def decorator(func, *args, **kwargs):
        print(f'top func is {func}')

        @click.command(**top_command_args)
        @click.option('-l', '--log-level', default='warning')
        def wrapper(log_level: str | None = None, *args, **kwargs):
            log.init(log_level)

            func(*args, **kwargs)

        return wrapper

    return decorator
