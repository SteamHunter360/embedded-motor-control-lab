import pytest

from src.pid_tuning import (
    calculate_rms_control_effort,
    compare_pid_tunings,
)


def test_calculate_rms_control_effort_known_values():
    effort = calculate_rms_control_effort([3, 4])

    assert effort == pytest.approx((25 / 2) ** 0.5)


def test_compare_pid_tunings_returns_all_tunings():
    tunings = {
        "A": {"kp": 0.8, "ki": 0.4, "kd": 0.05},
        "B": {"kp": 2.0, "ki": 1.5, "kd": 0.05},
    }

    results = compare_pid_tunings(
        tunings,
        simulation_time=1.0,
        dt=0.01,
    )

    assert set(results.keys()) == {"A", "B"}

    for result in results.values():
        assert "gains" in result
        assert "metrics" in result
        assert "simulation" in result
        assert "steady_state_error" in result["metrics"]
        assert "rms_speed_error" in result["metrics"]
        assert "rms_control_effort" in result["metrics"]