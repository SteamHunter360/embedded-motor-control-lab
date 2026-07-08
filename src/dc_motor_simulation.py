import numpy as np


def simulate_dc_motor(
    target_speed=1000.0,
    simulation_time=5.0,
    dt=0.01,
    time_constant=0.5,
):
    """
    Simulate the speed response of a first-order DC motor.

    Parameters
    ----------
    target_speed : float
        Desired motor speed (RPM).

    simulation_time : float
        Total simulation duration (seconds).

    dt : float
        Simulation timestep (seconds).

    time_constant : float
        Motor time constant (seconds).

    Returns
    -------
    tuple
        (time, speed)
    """

    time = np.arange(
        0,
        simulation_time,
        dt,
    )

    speed = np.zeros(len(time))

    for i in range(1, len(time)):

        ds = (
            target_speed
            - speed[i - 1]
        ) * dt / time_constant

        speed[i] = speed[i - 1] + ds

    return (
        time,
        speed,
    )