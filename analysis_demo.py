from src.dc_motor_simulation import simulate_dc_motor
from src.motor_analysis import analyse_motor_response


def main():
    target_speed = 1000.0

    time_values, speed_values = simulate_dc_motor(
        target_speed=target_speed,
        simulation_time=5.0,
        dt=0.01,
        time_constant=0.5,
    )

    results = analyse_motor_response(
        time_values,
        speed_values,
        target_speed,
    )

    print("\nDC Motor Response Analysis")
    print(f"Target speed: {target_speed:.2f} RPM")
    print(f"Final speed: {speed_values[-1]:.2f} RPM")
    print(f"Steady-state error: {results['steady_state_error']:.4f} RPM")
    print(f"Maximum speed error: {results['max_speed_error']:.4f} RPM")
    print(f"RMS speed error: {results['rms_speed_error']:.4f} RPM")
    print(f"Overshoot: {results['overshoot_percentage']:.4f}%")

    if results["settling_time"] is None:
        print("Settling time: Did not settle")
    else:
        print(f"Settling time: {results['settling_time']:.4f} s")


if __name__ == "__main__":
    main()