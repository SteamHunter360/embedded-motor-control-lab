import pytest

from src.pid_speed_controller import (
    PIDSpeedController,
    simulate_pid_speed_control,
)


def test_pid_speed_controller_positive_error():
    controller = PIDSpeedController(
        kp=1.0,
        ki=0.0,
        kd=0.0,
        dt=0.1,
    )

    output = controller.update(
        setpoint=100,
        measurement=80,
    )

    assert output == pytest.approx(20.0)


def test_pid_speed_controller_negative_error_clamps_to_zero():
    controller = PIDSpeedController(
        kp=1.0,
        ki=0.0,
        kd=0.0,
        dt=0.1,
    )

    output = controller.update(
        setpoint=80,
        measurement=100,
    )

    assert output == pytest.approx(0.0)


def test_pid_speed_controller_output_limit():
    controller = PIDSpeedController(
        kp=100.0,
        ki=0.0,
        kd=0.0,
        dt=0.1,
        output_max=50.0,
    )

    output = controller.update(
        setpoint=100,
        measurement=0,
    )

    assert output == pytest.approx(50.0)


def test_pid_speed_controller_reset():
    controller = PIDSpeedController(
        kp=1.0,
        ki=1.0,
        kd=0.0,
        dt=0.1,
    )

    controller.update(
        setpoint=100,
        measurement=0,
    )

    controller.reset()

    assert controller.integral == pytest.approx(0.0)
    assert controller.previous_error == pytest.approx(0.0)


def test_simulate_pid_speed_control_returns_expected_keys():
    results = simulate_pid_speed_control()

    expected_keys = {
        "time_values",
        "speed_values",
        "control_values",
        "setpoint",
    }

    assert set(results.keys()) == expected_keys


def test_simulate_pid_speed_control_matching_lengths():
    results = simulate_pid_speed_control()

    assert len(results["time_values"]) == len(results["speed_values"])
    assert len(results["time_values"]) == len(results["control_values"])


def test_simulate_pid_speed_control_converges_towards_setpoint():
    results = simulate_pid_speed_control(
        setpoint=750.0,
        simulation_time=5.0,
    )

    final_speed = results["speed_values"][-1]

    assert final_speed > 0.8 * 750.0