import numpy as np


def calculate_steady_state_error(target_speed, actual_speed_values):
    final_speed = actual_speed_values[-1]

    return abs(target_speed - final_speed)


def calculate_max_speed_error(target_speed, actual_speed_values):
    errors = [
        abs(target_speed - speed)
        for speed in actual_speed_values
    ]

    return max(errors)


def calculate_rms_speed_error(target_speed, actual_speed_values):
    errors = np.array(
        [
            target_speed - speed
            for speed in actual_speed_values
        ]
    )

    return float(
        np.sqrt(
            np.mean(errors ** 2)
        )
    )


def calculate_overshoot_percentage(target_speed, actual_speed_values):
    if target_speed == 0:
        return 0.0

    max_speed = max(actual_speed_values)
    overshoot = max_speed - target_speed

    if overshoot <= 0:
        return 0.0

    return float(
        (overshoot / target_speed) * 100
    )


def calculate_settling_time(
    time_values,
    actual_speed_values,
    target_speed,
    tolerance=0.02,
):
    tolerance_band = abs(target_speed) * tolerance

    for i in range(len(actual_speed_values)):
        remaining_values = actual_speed_values[i:]

        if all(
            abs(speed - target_speed) <= tolerance_band
            for speed in remaining_values
        ):
            return time_values[i]

    return None


def analyse_motor_response(
    time_values,
    actual_speed_values,
    target_speed,
):
    return {
        "steady_state_error": calculate_steady_state_error(
            target_speed,
            actual_speed_values,
        ),
        "max_speed_error": calculate_max_speed_error(
            target_speed,
            actual_speed_values,
        ),
        "rms_speed_error": calculate_rms_speed_error(
            target_speed,
            actual_speed_values,
        ),
        "overshoot_percentage": calculate_overshoot_percentage(
            target_speed,
            actual_speed_values,
        ),
        "settling_time": calculate_settling_time(
            time_values,
            actual_speed_values,
            target_speed,
        ),
    }