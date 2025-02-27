from mktech.date_time import parse_duration


class TestParseDuration:
    def test_none(self) -> None:
        assert parse_duration(None).unwrap() is None

    def test_hh_mm_ss_us_invalid_hh(self) -> None:
        td = parse_duration('x1:31:49.564124719')

        assert td.is_err()

    def test_hh_mm_ss_us(self) -> None:
        td = parse_duration('01:31:49.564124719').unwrap()

        assert td is not None

        assert td.seconds == 1 * 60 * 60 + 31 * 60 + 49
        assert td.microseconds == 564124

    def test_hh_mm_ss_us_zero_hours(self) -> None:
        td = parse_duration('00:31:49.564124719').unwrap()

        assert td is not None

        assert td.seconds == 31 * 60 + 49
        assert td.microseconds == 564124

    def test_mm_ss_us(self) -> None:
        td = parse_duration('31:49.564124719').unwrap()

        assert td is not None

        assert td.seconds == 31 * 60 + 49
        assert td.microseconds == 564124

    def test_ss_us(self) -> None:
        td = parse_duration('49.564124719').unwrap()

        assert td is not None

        assert td.seconds == 49
        assert td.microseconds == 564124

    def test_ss(self) -> None:
        td = parse_duration('49').unwrap()

        assert td is not None

        assert td.total_seconds() == 49
        assert td.microseconds == 0
