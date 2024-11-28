from importlib import resources

from result import Err, Ok, Result

from mktech.path import Path


def resource_path(package: str, name: str) -> Result[Path, Exception]:
    result: Result[Path, Exception]

    try:
        package_files = resources.files(package)

        result = Ok(Path(str(package_files.joinpath(name))))
    except Exception as e:
        result = Err(e)

    return result
