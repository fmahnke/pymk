from mktech.resources import resource_path

from result import is_err, is_ok


class TestResourcePath:
    def test_ok(self) -> None:
        result = resource_path('test.data', 'config.toml')

        assert is_ok(result)

    def test_err_not_found(self) -> None:
        result = resource_path('package.not_found', 'config.toml')

        assert is_err(result)
