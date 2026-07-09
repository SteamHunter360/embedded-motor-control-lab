import pytest

from src.dc_motor_simulation import simulate_dc_motor


def test_simulate_dc_motor_returns_matching_lengths():
    time_values, speed_values = simulate_dc_motor()

    assert len(time_values) == len(speed_values)


def test_simulate_dc_motor_starts_at_zero_speed():
    _, speed_values = simulate_dc_motor()

    assert speed_values[0] == pytest.approx(0.0)


def test_simulate_dc_motor_converges_toward_target_speed():
    target_speed = 1000.0

    _, speed_values = simulate_dc_motor(
        target_speed=target_speed,
        simulation_time=5.0,
        dt=0.01,
        time_constant=0.5,
    )

    assert abs(speed_values[-1] - target_speed) < 1.0


def test_simulate_dc_motor_rejects_negative_target_speed():
    with pytest.raises(ValueError):
        simulate_dc_motor(target_speed=-100)


def test_simulate_dc_motor_rejects_zero_dt():
    with pytest.raises(ValueError):
        simulate_dc_motor(dt=0)


def test_simulate_dc_motor_rejects_negative_simulation_time():
    with pytest.raises(ValueError):
        simulate_dc_motor(simulation_time=-1)


def test_simulate_dc_motor_rejects_zero_time_constant():
    with pytest.raises(ValueError):
        simulate_dc_motor(time_constant=0)