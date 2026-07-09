from src.motor_analysis import analyse_motor_response
from src.pid_speed_controller import simulate_pid_speed_control


def calculate_rms_control_effort(control_values):
    if len(control_values) == 0:
        return 0.0

    return (
        sum(control ** 2 for control in control_values)
        / len(control_values)
    ) ** 0.5


def compare_pid_tunings(
    tunings,
    setpoint=750.0,
    simulation_time=5.0,
    dt=0.01,
    time_constant=0.5,
    max_speed=1000.0,
):
    results = {}

    for tuning_name, gains in tunings.items():
        simulation = simulate_pid_speed_control(
            setpoint=setpoint,
            simulation_time=simulation_time,
            dt=dt,
            time_constant=time_constant,
            max_speed=max_speed,
            kp=gains["kp"],
            ki=gains["ki"],
            kd=gains["kd"],
        )

        metrics = analyse_motor_response(
            simulation["time_values"],
            simulation["speed_values"],
            setpoint,
        )

        metrics["rms_control_effort"] = calculate_rms_control_effort(
            simulation["control_values"]
        )

        results[tuning_name] = {
            "gains": gains,
            "metrics": metrics,
            "simulation": simulation,
        }

    return results