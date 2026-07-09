import numbers


def validate_positive_number(value, parameter_name):
    if not isinstance(value, numbers.Real):
        raise TypeError(
            f"{parameter_name} must be a number."
        )

    if value <= 0:
        raise ValueError(
            f"{parameter_name} must be greater than zero."
        )


def validate_non_negative_number(value, parameter_name):
    if not isinstance(value, numbers.Real):
        raise TypeError(
            f"{parameter_name} must be a number."
        )

    if value < 0:
        raise ValueError(
            f"{parameter_name} cannot be negative."
        )


def validate_target_speed(target_speed):
    validate_non_negative_number(
        target_speed,
        "target_speed",
    )


def validate_time_step(dt):
    validate_positive_number(
        dt,
        "dt",
    )


def validate_simulation_time(simulation_time):
    validate_positive_number(
        simulation_time,
        "simulation_time",
    )


def validate_time_constant(time_constant):
    validate_positive_number(
        time_constant,
        "time_constant",
    )