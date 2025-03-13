from typing import Any, Iterator, Optional

import jsonschema

import tomlkit as toml
from tomlkit import TOMLDocument
from tomlkit.container import Container
from tomlkit.items import Item

import mktech.json as json
from mktech.path import PathInput
import mktech.toml

from typing import TypeAlias

ValidationError: TypeAlias = jsonschema.exceptions.ValidationError


class Config:
    """ Build configuration file. """
    def __init__(self, schema: Optional[PathInput] = None) -> None:
        self.config = TOMLDocument()

        if schema is None:
            self._schema = None
        else:
            with open(schema) as file:
                self._schema = json.load(file)

            self.config.update(json.from_schema(self._schema))

    @classmethod
    def from_file(cls, path: PathInput) -> 'Config':
        """ Parse the configuration from an existing file. """

        ctx = cls()
        ctx._init_from_file(path)

        return ctx

    def load_from_file(self, path: PathInput) -> None:
        """ Load the configuration from an existing file. """

        self._init_from_file(path)

    def asdict(self) -> dict[str, Any]:
        return dict(self.config)

    def toml(self) -> str:
        return toml.dumps(self.config)

    def write(self, path: str, mode: str = 'w') -> None:
        """ Write the configuration to a file. """

        with open(path, mode) as fi:
            if mode == 'a':
                fi.write('\n')

            fi.write(toml.dumps(self.config))

    def _init_from_file(self, path: PathInput) -> None:
        with open(path, 'r') as file:
            toml_document = toml.parse(file.read())

        if self._schema is None:
            self.config = toml_document
        else:
            self.config = mktech.toml.merge(self.config, toml_document)

            jsonschema.validate(self.asdict(), self._schema)

    def __iter__(self) -> Iterator[str]:
        return self.config.__iter__()

    def __getitem__(self, key: str) -> Item | Container:
        return self.config[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.config[key] = value
