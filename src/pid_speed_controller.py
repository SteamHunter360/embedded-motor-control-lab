from src.validation import (
    validate_non_negative_number,
    validate_positive_number,
)


class PIDSpeedController:
    def __init__(
        self,
        kp=0.8,
        ki=0.4,
        kd=0.05,
        dt=0.01,
        output_min=0.0,
        output_max=1000.0,
    ):
        validate_non_negative_number(kp, "kp")
        validate_non_negative_number(ki, "ki")
        validate_non_negative_number(kd, "kd")
        validate_positive_number(dt, "dt")

        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.output_min = output_min
        self.output_max = output_max

        self.integral = 0.0
        self.previous_error = 0.0

    def update(self, setpoint, measurement):
        error = setpoint - measurement

        self.integral += error * self.dt
        derivative = (error - self.previous_error) / self.dt

        output = (
            self.kp * error
            + self.ki * self.integral
            + self.kd * derivative
        )

        output = max(
            self.output_min,
            min(self.output_max, output),
        )

        self.previous_error = error

        return output

    def reset(self):
        self.integral = 0.0
        self.previous_error = 0.0


def simulate_pid_speed_control(
    setpoint=750.0,
    simulation_time=5.0,
    dt=0.01,
    time_constant=0.5,
    max_speed=1000.0,
    kp=0.8,
    ki=0.4,
    kd=0.05,
):
    validate_non_negative_number(setpoint, "setpoint")
    validate_positive_number(simulation_time, "simulation_time")
    validate_positive_number(dt, "dt")
    validate_positive_number(time_constant, "time_constant")
    validate_positive_number(max_speed, "max_speed")

    controller = PIDSpeedController(
        kp=kp,
        ki=ki,
        kd=kd,
        dt=dt,
        output_min=0.0,
        output_max=max_speed,
    )

    num_steps = int(simulation_time / dt)

    time_values = [
        step * dt
        for step in range(num_steps)
    ]

    speed_values = [0.0 for _ in time_values]
    control_values = [0.0 for _ in time_values]

    for i in range(1, len(time_values)):
        control = controller.update(
            setpoint,
            speed_values[i - 1],
        )

        control_values[i] = control

        speed_values[i] = speed_values[i - 1] + (
            control - speed_values[i - 1]
        ) * dt / time_constant

    return {
        "time_values": time_values,
        "speed_values": speed_values,
        "control_values": control_values,
        "setpoint": setpoint,
    }