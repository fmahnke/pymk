from typing import Any, Tuple, Type

from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    TomlConfigSettingsSource,
)
from pydantic_settings.sources import PathType

__all__ = ['BaseModel', 'BaseConfig', 'Field']

_toml_path: PathType


class BaseConfig(
        BaseSettings,
        extra='ignore',
        env_prefix='mk_',
        env_nested_delimiter='_',
):
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        global _toml_path

        return (
            init_settings,
            env_settings,
            TomlConfigSettingsSource(settings_cls, toml_file=_toml_path),
        )

    def __init__(self, toml_path: PathType, *args: Any, **kwargs: Any) -> None:
        global _toml_path
        _toml_path = toml_path

        super().__init__(*args, **kwargs)
