import sys
from signal import SIGHUP

from mktech.error import Err, Ok
from mktech.resources import resource_path
from mktech.subprocess import Subprocess


class TestSubprocess:
    count_path = resource_path('tests.subprocess.resources',
                               'count.py').unwrap()
    count_command = f'{sys.executable} {count_path}'

    def test_terminated_with_exit_0(self) -> None:
        process = Subprocess(f'{self.count_command} 4 0', encoding='utf-8')

        assert [line for line in process.readline()] == ['0', '1', '2', '3']

        match process.terminated_status:
            case Err(error):
                raise AssertionError(error)
            case Ok(status):
                assert status.condition == 'exit'
                assert status.code == 0
            case _:
                raise AssertionError()

    def test_terminated_with_exit_1(self) -> None:
        process = Subprocess(f'{self.count_command} 0 0', encoding='utf-8')

        [line for line in process.readline()]

        match process.terminated_status:
            case Err(error):
                raise AssertionError(error)
            case Ok(status):
                assert status.condition == 'exit'
                assert status.code == 1
            case _:
                raise AssertionError()

    def test_terminated_with_signal(self) -> None:
        process = Subprocess(f'{self.count_command} 4 0', encoding='utf-8')

        next(process.readline())

        process.close()

        match process.terminated_status:
            case Err(error):
                raise AssertionError(error)
            case Ok(status):
                assert status.condition == 'signal'
                assert status.code == SIGHUP
            case _:
                raise AssertionError()
