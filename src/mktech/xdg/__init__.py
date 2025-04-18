from mktech.os import environ
from mktech.path import Path


def xdg_cache_home() -> Path:
    return Path(environ('XDG_CACHE_HOME'))


def xdg_config_home() -> Path:
    return Path(
        environ(
            'XDG_CONFIG_HOME',
            str(Path(environ('HOME'), '.config')),
        )
    )


def xdg_data_home() -> Path:
    return Path(
        environ(
            'XDG_data_HOME',
            str(Path(environ('HOME'), '.local/share')),
        )
    )


def xdg_runtime_dir() -> Path:
    return Path(environ('XDG_RUNTIME_DIR'))


def xdg_state_home() -> Path:
    return Path(
        environ(
            'XDG_STATE_HOME',
            str(Path(environ('HOME'), '.local/state')),
        )
    )
