import pytest

from src.pwm_control import (
    clamp_pwm_duty_cycle,
    calculate_target_speed_from_pwm,
    simulate_pwm_motor_response,
)


def test_clamp_pwm_duty_cycle_keeps_valid_value():
    assert clamp_pwm_duty_cycle(50) == pytest.approx(50.0)


def test_clamp_pwm_duty_cycle_clamps_negative_value():
    assert clamp_pwm_duty_cycle(-10) == pytest.approx(0.0)


def test_clamp_pwm_duty_cycle_clamps_above_100():
    assert clamp_pwm_duty_cycle(150) == pytest.approx(100.0)


def test_calculate_target_speed_from_pwm_known_value():
    target_speed = calculate_target_speed_from_pwm(
        duty_cycle=60,
        max_speed=1000,
    )

    assert target_speed == pytest.approx(600.0)


def test_calculate_target_speed_from_pwm_rejects_negative_duty_cycle():
    with pytest.raises(ValueError):
        calculate_target_speed_from_pwm(
            duty_cycle=-10,
            max_speed=1000,
        )


def test_simulate_pwm_motor_response_returns_expected_keys():
    results = simulate_pwm_motor_response(
        duty_cycle=60,
        max_speed=1000,
    )

    expected_keys = {
        "time_values",
        "speed_values",
        "pwm_values",
        "target_speed",
        "duty_cycle",
    }

    assert set(results.keys()) == expected_keys


def test_simulate_pwm_motor_response_matching_lengths():
    results = simulate_pwm_motor_response(
        duty_cycle=60,
        max_speed=1000,
    )

    assert len(results["time_values"]) == len(results["speed_values"])
    assert len(results["time_values"]) == len(results["pwm_values"])