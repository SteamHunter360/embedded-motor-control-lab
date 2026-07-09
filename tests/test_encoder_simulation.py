import pytest

from src.encoder_simulation import (
    calculate_encoder_counts,
    simulate_encoder,
)


def test_calculate_encoder_counts_zero_speed():
    counts = calculate_encoder_counts(
        motor_speed=0,
        time_values=[0, 1, 2],
    )

    assert counts == [0, 0, 0]


def test_calculate_encoder_counts_known_value():
    counts = calculate_encoder_counts(
        motor_speed=60,
        time_values=[1],
        encoder_resolution=360,
    )

    assert counts[0] == pytest.approx(360)


def test_negative_motor_speed():
    with pytest.raises(ValueError):
        calculate_encoder_counts(
            motor_speed=-100,
            time_values=[0, 1],
        )


def test_zero_encoder_resolution():
    with pytest.raises(ValueError):
        calculate_encoder_counts(
            motor_speed=500,
            time_values=[0, 1],
            encoder_resolution=0,
        )


def test_simulate_encoder_returns_expected_keys():
    results = simulate_encoder(
        motor_speed=500,
    )

    expected_keys = {
        "time_values",
        "encoder_counts",
        "motor_speed",
        "encoder_resolution",
    }

    assert set(results.keys()) == expected_keys


def test_matching_lengths():
    results = simulate_encoder(
        motor_speed=500,
    )

    assert (
        len(results["time_values"])
        ==
        len(results["encoder_counts"])
    )


def test_encoder_counts_increase():
    results = simulate_encoder(
        motor_speed=500,
    )

    assert (
        results["encoder_counts"][-1]
        >
        results["encoder_counts"][0]
    )