from src.encoder_simulation import simulate_encoder
from src.motor_visualisation import plot_encoder_counts


def main():
    results = simulate_encoder(
        motor_speed=750,
        simulation_time=5,
        dt=0.01,
        encoder_resolution=360,
    )

    print("\nEncoder Simulation Demo")
    print(f"Motor speed: {results['motor_speed']} RPM")
    print(f"Final encoder count: {results['encoder_counts'][-1]:.0f}")

    plot_encoder_counts(
        results["time_values"],
        results["encoder_counts"],
        save_path="images/encoder_counts.png",
    )


if __name__ == "__main__":
    main()