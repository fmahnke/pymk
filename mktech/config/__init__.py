from typing import Any

import tomlkit as toml
from tomlkit import TOMLDocument
from tomlkit.container import Container
from tomlkit.items import Item

from mktech.path import PathInput


class Config:
    """ Build configuration file. """

    def __init__(self) -> None:
        self.config = TOMLDocument()

    @classmethod
    def from_file(cls, path: PathInput) -> 'Config':
        """ Parse the configuration from an existing file. """

        ctx = cls()
        ctx._init_from_file(path)

        return ctx

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
        with open(path, 'r') as fi:
            self.config = toml.parse(fi.read())

    def __getitem__(self, key: str) -> Item | Container:
        return self.config[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.config[key] = value
