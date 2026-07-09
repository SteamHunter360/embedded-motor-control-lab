from src.motor_analysis import analyse_motor_response
from src.motor_visualisation import (
    plot_reference_vs_actual_speed,
    plot_pwm_signal,
)
from src.pid_speed_controller import simulate_pid_speed_control


def main():
    results = simulate_pid_speed_control(
        setpoint=750.0,
        simulation_time=5.0,
        dt=0.01,
        time_constant=0.5,
        max_speed=1000.0,
    )

    analysis = analyse_motor_response(
        results["time_values"],
        results["speed_values"],
        results["setpoint"],
    )

    reference_values = [
        results["setpoint"]
        for _ in results["time_values"]
    ]

    print("\nPID Speed Control Demo")
    print(f"Target speed: {results['setpoint']:.2f} RPM")
    print(f"Final speed: {results['speed_values'][-1]:.2f} RPM")
    print(f"Steady-state error: {analysis['steady_state_error']:.4f} RPM")
    print(f"RMS speed error: {analysis['rms_speed_error']:.4f} RPM")
    print(f"Overshoot: {analysis['overshoot_percentage']:.4f}%")

    plot_reference_vs_actual_speed(
        results["time_values"],
        reference_values,
        results["speed_values"],
        save_path="images/pid_speed_control_response.png",
    )

    plot_pwm_signal(
        results["time_values"],
        results["control_values"],
        save_path="images/pid_control_effort.png",
    )


if __name__ == "__main__":
    main()