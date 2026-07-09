import pytest

from src.validation import (
    validate_target_speed,
    validate_time_step,
    validate_simulation_time,
    validate_time_constant,
)


def test_negative_target_speed():
    with pytest.raises(ValueError):
        validate_target_speed(-100)


def test_negative_dt():
    with pytest.raises(ValueError):
        validate_time_step(-0.01)


def test_zero_dt():
    with pytest.raises(ValueError):
        validate_time_step(0)


def test_negative_simulation_time():
    with pytest.raises(ValueError):
        validate_simulation_time(-1)


def test_zero_time_constant():
    with pytest.raises(ValueError):
        validate_time_constant(0)


def test_valid_inputs():
    validate_target_speed(1000)
    validate_time_step(0.01)
    validate_simulation_time(5)
    validate_time_constant(0.5)