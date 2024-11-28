from importlib import resources

from mktech.config import Config
from mktech.resources import resource_path

_resources = resources.files('test.data')


class TestConfig:

    def test_config_to_toml(self) -> None:
        config = Config()

        config['log_level'] = 'DEBUG'

        config['ssh'] = {'use_ssh': True}

        result = resource_path('test.data', 'config.toml')

        assert config.toml() == result.unwrap().read_text()

    def test_config_parse_toml(self) -> None:
        config_toml_path = resource_path('test.data', 'config.toml')

        config = Config.from_file(config_toml_path.unwrap())

        assert config.asdict() == {
            'log_level': 'DEBUG', 'ssh': {'use_ssh': True}
        }
