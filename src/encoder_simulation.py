from src.validation import (
    validate_non_negative_number,
    validate_positive_number,
)


def calculate_encoder_counts(
    motor_speed,
    time_values,
    encoder_resolution=360,
):
    """
    Calculate cumulative encoder counts.

    Parameters
    ----------
    motor_speed : float
        Motor speed in RPM.

    time_values : array-like
        Simulation time values.

    encoder_resolution : int
        Encoder pulses per revolution.

    Returns
    -------
    list
        Encoder counts.
    """

    validate_non_negative_number(
        motor_speed,
        "motor_speed",
    )

    validate_positive_number(
        encoder_resolution,
        "encoder_resolution",
    )

    revolutions_per_second = motor_speed / 60.0

    encoder_counts = []

    for t in time_values:

        total_revolutions = revolutions_per_second * t

        counts = (
            total_revolutions
            * encoder_resolution
        )

        encoder_counts.append(counts)

    return encoder_counts


def simulate_encoder(
    motor_speed,
    simulation_time=5.0,
    dt=0.01,
    encoder_resolution=360,
):
    validate_positive_number(
        simulation_time,
        "simulation_time",
    )

    validate_positive_number(
        dt,
        "dt",
    )

    num_steps = int(simulation_time / dt)

    time_values = [
        i * dt
        for i in range(num_steps)
    ]

    encoder_counts = calculate_encoder_counts(
        motor_speed,
        time_values,
        encoder_resolution,
    )

    return {
        "time_values": time_values,
        "encoder_counts": encoder_counts,
        "motor_speed": motor_speed,
        "encoder_resolution": encoder_resolution,
    }