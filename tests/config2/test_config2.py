from enum import Enum
from typing import Annotated, Any, final

from annotated_types import Len

from mktech.config2 import BaseConfig, BaseModel
from mktech.error import Err, Ok
from mktech.resources import resource_path

_config_path = 'config.toml'


class ExampleConfig(BaseConfig):
    class Scon(BaseModel):
        version: str

    class Arduino(BaseModel):
        core: str
        version: str
        board: str
        port: str

    class Keypad(BaseModel):
        class Driver(str, Enum):
            digital = 'digital'
            analog = 'analog'

        row_pins: list[int]
        column_pins: list[int]
        driver: Driver

    class Motor(BaseModel):
        class Interface(str, Enum):
            driver = 'driver'
            full4wire = 'full4wire'

        interface: Interface
        steps_per_revolution: int
        pins: Annotated[list[int],
                        Len(min_length=2, max_length=2)] | Annotated[
                            list[int], Len(min_length=4, max_length=4)]

    class Display(BaseModel):
        class Controller(str, Enum):
            PCD8544 = 'PCD8544'
            SSD1306 = 'SSD1306'

        class BufferMode(str, Enum):
            _1Page = '1Page'
            _2Page = '2Page'
            full = 'Full'

        controller: Controller
        buffer_mode: BufferMode
        clock: int
        data: int
        cs: int
        dc: int
        reset: int
        backlight: int

    scon: Scon
    log_level: str
    arduino: Arduino
    keypad: Keypad
    motor: Motor
    display: Display

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


@final
class TestConfig2:
    expected = {
        'log_level': 'DEBUG',
        'scon': {'version': '0.2.0'},
        'arduino':
            {
                'core': 'arduino:renesas_uno',
                'version': '1.2.0',
                'board': 'minima',
                'port': '/dev/ttyACM0'
            },
        'keypad':
            {
                'row_pins': [3, 2, 14, 15, 16],
                'column_pins': [10, 19, 18, 17],
                'driver': ExampleConfig.Keypad.Driver.digital
            },
        'motor':
            {
                'interface': ExampleConfig.Motor.Interface.driver,
                'steps_per_revolution': 1024,
                'pins': [9, 8, 0, 0]
            },
        'display':
            {
                'controller': ExampleConfig.Display.Controller.PCD8544,
                'buffer_mode': ExampleConfig.Display.BufferMode._1Page,
                'clock': 13,
                'data': 11,
                'cs': 4,
                'dc': 6,
                'reset': 5,
                'backlight': 7
            }
    }
    scon = ExampleConfig.Scon(version='0.2.0')

    arduino = ExampleConfig.Arduino(
        core='arduino:renesas_uno',
        version='1.2.0',
        board='minima',
        port='/dev/ttyACM0'
    )

    keypad = ExampleConfig.Keypad(
        row_pins=[3, 2, 14, 15, 16],
        column_pins=[10, 19, 18, 17],
        driver=ExampleConfig.Keypad.Driver.digital
    )

    motor = ExampleConfig.Motor(
        interface=ExampleConfig.Motor.Interface.driver,
        steps_per_revolution=1024,
        pins=[9, 8, 0, 0]
    )

    display = ExampleConfig.Display(
        controller=ExampleConfig.Display.Controller.PCD8544,
        buffer_mode=ExampleConfig.Display.BufferMode._1Page,
        clock=13,
        data=11,
        cs=4,
        dc=6,
        reset=5,
        backlight=7
    )

    def test_toml_source(self) -> None:
        match resource_path('tests.config2', 'data'):
            case Err(e):
                raise AssertionError(e)
            case Ok(v):
                toml_path = v.joinpath(_config_path)

                conf = ExampleConfig(toml_path)
                assert conf.model_dump() == self.expected

    def test_init_source(self) -> None:
        conf = ExampleConfig(
            log_level='DEBUG',
            scon=self.scon,
            arduino=self.arduino,
            keypad=self.keypad,
            motor=self.motor,
            display=self.display
        )

        assert conf.model_dump() == self.expected
