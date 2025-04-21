from mktech.error import is_err, is_ok
from mktech.resources import resource_path


class TestResourcePath:
    def test_ok(self) -> None:
        result = resource_path('tests.data', 'config.toml')

        assert is_ok(result)

    def test_err_not_found(self) -> None:
        result = resource_path('package.not_found', 'config.toml')

        assert is_err(result)
