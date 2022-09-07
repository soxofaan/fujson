import io

import pytest

from fujson import FuJsonEncoder, dump, dumps


def test_basic():
    data = {"x": 1.2345678}
    encoder = FuJsonEncoder(float_format=".2f")
    assert encoder.encode(data) == '{"x": 1.23}'


@pytest.mark.parametrize(
    ["format", "expected"],
    [
        (".0f", '{"x": 1}'),
        (".1f", '{"x": 1.2}'),
        (".2f", '{"x": 1.23}'),
        (".3f", '{"x": 1.235}'),
        (".4f", '{"x": 1.2346}'),
    ],
)
def test_formats(format, expected):
    data = {"x": 1.2345678}
    encoder = FuJsonEncoder(float_format=format)
    assert encoder.encode(data) == expected


def test_dumps_basic():
    data = {"x": 1.2345678}
    assert dumps(data, float_format=".2f") == '{"x": 1.23}'


def test_dump_basic():
    data = {"x": 1.2345678}
    with io.StringIO() as f:
        dump(data, f, float_format=".2f")
        assert f.getvalue() == '{"x": 1.23}'
