import matplotlib.pyplot as plt


def plot_pid_tuning_comparison(results, save_path=None):
    tuning_names = list(results.keys())

    rms_errors = [
        results[name]["metrics"]["rms_speed_error"]
        for name in tuning_names
    ]

    steady_state_errors = [
        results[name]["metrics"]["steady_state_error"]
        for name in tuning_names
    ]

    overshoots = [
        results[name]["metrics"]["overshoot_percentage"]
        for name in tuning_names
    ]

    control_efforts = [
        results[name]["metrics"]["rms_control_effort"]
        for name in tuning_names
    ]

    x = range(len(tuning_names))

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, rms_errors, marker="o", label="RMS Speed Error")
    ax.plot(x, steady_state_errors, marker="o", label="Steady-State Error")
    ax.plot(x, overshoots, marker="o", label="Overshoot (%)")
    ax.plot(x, control_efforts, marker="o", label="RMS Control Effort")

    ax.set_xticks(list(x))
    ax.set_xticklabels(tuning_names)
    ax.set_title("PID Motor Speed Control Tuning Comparison")
    ax.set_ylabel("Metric Value")
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()

    return fig