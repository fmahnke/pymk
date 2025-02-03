from mktech.config import Config, ValidationError

import pytest

from test.util import resource_path


class TestConfig:
    def test_missing_key(self) -> None:
        config = Config.from_file(resource_path('config.toml'))

        assert 'missing_key' not in config

    def test_config_to_toml(self) -> None:
        config = Config()

        config['log_level'] = 'WARNING'

        config['zsh'] = {'fzf': True}
        config['ssh'] = {'use_ssh': False, 'port': 22}

        assert config.toml() == resource_path('config.toml').read_text()

    def test_config_parse_toml(self) -> None:
        config = Config.from_file(resource_path('config.toml'))

        assert config.asdict() == {
            'log_level': 'WARNING',
            'zsh': {'fzf': True},
            'ssh': {'use_ssh': False, 'port': 22}
        }

    def test_config_schema_invalid(self) -> None:
        config = Config(schema=resource_path('config_schema.json'))

        with pytest.raises(ValidationError):
            config.load_from_file(resource_path('config_invalid.toml'))

    def test_config_schema(self) -> None:
        config = Config(schema=resource_path('config_schema.json'))

        assert config.asdict() == {
            'log_level': 'WARNING',
            'modules': [],
            'zsh': {'fzf': False, 'lsd': False}
        }

    def test_config_schema_update(self) -> None:
        config = Config(schema=resource_path('config_schema.json'))

        config.load_from_file(resource_path('config.toml'))

        assert config.asdict() == {
            'log_level': 'WARNING',
            'modules': [],
            'zsh': {'fzf': True, 'lsd': False},
            'ssh': {'use_ssh': False, 'port': 22}
        }
