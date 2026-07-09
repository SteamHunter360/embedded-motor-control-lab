from src.motor_analysis import analyse_motor_response
from src.motor_visualisation import (
    plot_pwm_signal,
    plot_speed_response,
)
from src.pwm_control import simulate_pwm_motor_response


def main():
    duty_cycle = 60.0

    results = simulate_pwm_motor_response(
        duty_cycle=duty_cycle,
        max_speed=1000.0,
        simulation_time=5.0,
        dt=0.01,
        time_constant=0.5,
    )

    analysis = analyse_motor_response(
        results["time_values"],
        results["speed_values"],
        results["target_speed"],
    )

    print("\nPWM Motor Response Demo")
    print(f"Duty cycle: {results['duty_cycle']:.2f}%")
    print(f"Target speed: {results['target_speed']:.2f} RPM")
    print(f"Final speed: {results['speed_values'][-1]:.2f} RPM")
    print(f"Steady-state error: {analysis['steady_state_error']:.4f} RPM")
    print(f"RMS speed error: {analysis['rms_speed_error']:.4f} RPM")

    plot_speed_response(
        results["time_values"],
        results["speed_values"],
        target_speed=results["target_speed"],
        save_path="images/pwm_motor_response.png",
    )

    plot_pwm_signal(
        results["time_values"],
        results["pwm_values"],
        save_path="images/pwm_command_signal.png",
    )


if __name__ == "__main__":
    main()