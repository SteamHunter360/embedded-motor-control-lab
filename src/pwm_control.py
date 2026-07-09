from src.dc_motor_simulation import simulate_dc_motor
from src.validation import (
    validate_non_negative_number,
    validate_positive_number,
)


def clamp_pwm_duty_cycle(duty_cycle):
    if duty_cycle < 0:
        return 0.0

    if duty_cycle > 100:
        return 100.0

    return float(duty_cycle)


def calculate_target_speed_from_pwm(
    duty_cycle,
    max_speed=1000.0,
):
    validate_non_negative_number(
        duty_cycle,
        "duty_cycle",
    )

    validate_positive_number(
        max_speed,
        "max_speed",
    )

    duty_cycle = clamp_pwm_duty_cycle(duty_cycle)

    return max_speed * (duty_cycle / 100.0)


def simulate_pwm_motor_response(
    duty_cycle,
    max_speed=1000.0,
    simulation_time=5.0,
    dt=0.01,
    time_constant=0.5,
):
    target_speed = calculate_target_speed_from_pwm(
        duty_cycle,
        max_speed,
    )

    time_values, speed_values = simulate_dc_motor(
        target_speed=target_speed,
        simulation_time=simulation_time,
        dt=dt,
        time_constant=time_constant,
    )

    pwm_values = [
        clamp_pwm_duty_cycle(duty_cycle)
        for _ in time_values
    ]

    return {
        "time_values": time_values,
        "speed_values": speed_values,
        "pwm_values": pwm_values,
        "target_speed": target_speed,
        "duty_cycle": clamp_pwm_duty_cycle(duty_cycle),
    }