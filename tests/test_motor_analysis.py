import pytest

from src.motor_analysis import (
    calculate_steady_state_error,
    calculate_max_speed_error,
    calculate_rms_speed_error,
    calculate_overshoot_percentage,
    calculate_settling_time,
    analyse_motor_response,
)


def test_calculate_steady_state_error_known_values():
    error = calculate_steady_state_error(
        target_speed=1000,
        actual_speed_values=[0, 500, 999],
    )

    assert error == pytest.approx(1.0)


def test_calculate_max_speed_error_known_values():
    error = calculate_max_speed_error(
        target_speed=1000,
        actual_speed_values=[0, 500, 999],
    )

    assert error == pytest.approx(1000.0)


def test_calculate_rms_speed_error_known_values():
    error = calculate_rms_speed_error(
        target_speed=10,
        actual_speed_values=[10, 8, 6],
    )

    assert error == pytest.approx(((0**2 + 2**2 + 4**2) / 3) ** 0.5)


def test_calculate_overshoot_percentage_known_values():
    overshoot = calculate_overshoot_percentage(
        target_speed=1000,
        actual_speed_values=[0, 1000, 1100],
    )

    assert overshoot == pytest.approx(10.0)


def test_calculate_settling_time_known_values():
    time_values = [0, 1, 2, 3]
    speed_values = [0, 900, 981, 990]

    settling_time = calculate_settling_time(
        time_values,
        speed_values,
        target_speed=1000,
        tolerance=0.02,
    )

    assert settling_time == pytest.approx(2)


def test_analyse_motor_response_returns_expected_keys():
    time_values = [0, 1, 2]
    speed_values = [0, 900, 1000]
    target_speed = 1000

    results = analyse_motor_response(
        time_values,
        speed_values,
        target_speed,
    )

    expected_keys = {
        "steady_state_error",
        "max_speed_error",
        "rms_speed_error",
        "overshoot_percentage",
        "settling_time",
    }

    assert set(results.keys()) == expected_keys