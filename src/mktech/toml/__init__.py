from tomlkit.items import Table
from tomlkit import TOMLDocument

from typing import Any


def merge(target: TOMLDocument, source: dict[str, Any]) -> TOMLDocument:
    result = _merge(target, source)

    assert isinstance(result, TOMLDocument)

    return result


def _merge(
    target: TOMLDocument | Table, source: dict[str, Any]
) -> TOMLDocument | Table:
    for key, value in source.items():
        if key not in target:
            target[key] = value
        else:
            target_value = target[key]

            if isinstance(target_value, Table):
                target[key] = _merge(target_value, value)
            else:
                target[key] = value

    return target
