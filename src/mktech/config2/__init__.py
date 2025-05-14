from typing import Any, Tuple, Type

import tomlkit
from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    TomlConfigSettingsSource,
)
from pydantic_settings.sources import PathType

from mktech.path import PathInput

__all__ = ['BaseModel', 'BaseConfig', 'Field']

_toml_path: PathType | None


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

    def __init__(
        self,
        toml_path: PathType | None = None,
        *args: Any,
        **kwargs: Any
    ) -> None:
        global _toml_path
        _toml_path = toml_path

        super().__init__(*args, **kwargs)

    def write(self, path: PathInput) -> None:
        """ Write the configuration to a file. """

        with open(path, 'w') as file:
            model = _model_without_none(self.model_dump())

            file.write(tomlkit.dumps(model))


def _model_without_none(model: dict[str, Any]) -> dict[str, Any]:
    result = {}

    for k, v in model.items():
        if isinstance(v, dict):
            result[k] = _model_without_none(v)
        elif v is not None:
            result[k] = v

    return result
