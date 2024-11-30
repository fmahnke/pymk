import mktech.json as json

from test.util import resource_path


def test_from_schema() -> None:
    with open(resource_path('config_schema.json')) as file:
        schema = json.load(file)

    with open(resource_path('config_default.json')) as file:
        default = json.load(file)

    assert json.from_schema(schema) == default
