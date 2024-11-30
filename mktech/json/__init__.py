from json import load
from typing import Any

__all__ = ['from_schema', 'load']


def from_schema(schema: dict[str, Any]) -> dict[str, Any]:
    # TODO error handling

    assert schema['type'] == 'object'

    return _default_properties(schema)


def _default_properties(schema: dict[str, Any]) -> dict[str, Any]:
    result = {}

    properties = schema['properties']

    for key, value in properties.items():
        type = value['type']

        if type == 'object':
            properties = _default_properties(value)

            if properties != {}:
                result[key] = properties
        else:
            if 'default' in value:
                result[key] = _value_from_json(value['default'], type)

    return result


def _value_from_json(value: Any, type: str) -> Any:
    if type == 'boolean':
        if value == 'true':
            result = True
        elif value == 'false':
            result = False
        else:
            # TODO error handling

            assert False
    else:
        result = value

    return result
