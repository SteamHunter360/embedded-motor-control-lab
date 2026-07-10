from src.pid_tuning import compare_pid_tunings
from src.pid_tuning_visualisation import plot_pid_tuning_comparison


def main():
    tunings = {
        "Conservative": {"kp": 0.8, "ki": 0.4, "kd": 0.05},
        "Balanced": {"kp": 2.0, "ki": 1.5, "kd": 0.05},
        "Aggressive": {"kp": 4.0, "ki": 2.5, "kd": 0.1},
    }

    results = compare_pid_tunings(tunings)

    print("\nPID Tuning Comparison")

    for name, result in results.items():
        gains = result["gains"]
        metrics = result["metrics"]

        print(f"\n{name}")
        print(f"Kp={gains['kp']}, Ki={gains['ki']}, Kd={gains['kd']}")
        print(f"Steady-state error: {metrics['steady_state_error']:.4f} RPM")
        print(f"Maximum speed error: {metrics['max_speed_error']:.4f} RPM")
        print(f"RMS speed error: {metrics['rms_speed_error']:.4f} RPM")
        print(f"Overshoot: {metrics['overshoot_percentage']:.4f}%")

        if metrics["settling_time"] is None:
            print("Settling time: Did not settle")
        else:
            print(f"Settling time: {metrics['settling_time']:.4f} s")

        print(f"RMS control effort: {metrics['rms_control_effort']:.4f}")

    plot_pid_tuning_comparison(
        results,
        save_path="images/pid_tuning_comparison.png",
    )


if __name__ == "__main__":
    main()