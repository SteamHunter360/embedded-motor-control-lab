import matplotlib.pyplot as plt


def plot_speed_response(
    time_values,
    speed_values,
    target_speed=None,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        time_values,
        speed_values,
        linewidth=2,
        label="Motor Speed",
    )

    if target_speed is not None:
        ax.axhline(
            target_speed,
            linestyle="--",
            linewidth=2,
            label="Target Speed",
        )

    ax.set_title("DC Motor Speed Response")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Speed (RPM)")
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()

    return fig


def plot_reference_vs_actual_speed(
    time_values,
    reference_speed_values,
    actual_speed_values,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        time_values,
        reference_speed_values,
        linestyle="--",
        linewidth=2,
        label="Reference Speed",
    )

    ax.plot(
        time_values,
        actual_speed_values,
        linewidth=2,
        label="Actual Speed",
    )

    ax.set_title("Reference vs Actual Motor Speed")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Speed (RPM)")
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()

    return fig


def plot_pwm_signal(
    time_values,
    pwm_values,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(9, 4))

    ax.plot(
        time_values,
        pwm_values,
        linewidth=2,
        label="PWM Command",
    )

    ax.set_title("PWM Command Signal")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("PWM Duty Cycle (%)")
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()

    return fig


def plot_encoder_counts(
    time_values,
    encoder_counts,
    save_path=None,
):
    fig, ax = plt.subplots(figsize=(9, 4))

    ax.plot(
        time_values,
        encoder_counts,
        linewidth=2,
        label="Encoder Counts",
    )

    ax.set_title("Encoder Count Response")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Counts")
    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()

    return fig