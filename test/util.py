from mktech.path import Path
import mktech.resources


def resource_path(name: str) -> Path:
    return mktech.resources.resource_path('test.data', name).unwrap()
