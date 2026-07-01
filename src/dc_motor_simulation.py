import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

# -------------------------
# Motor Parameters
# -------------------------

time_constant = 0.5      # seconds
target_speed = 1000      # RPM
simulation_time = 5      # seconds
dt = 0.01                # time step

time = np.arange(0, simulation_time, dt)

speed = np.zeros(len(time))

# -------------------------
# Motor Simulation
# -------------------------

for i in range(1, len(time)):

    ds = (
        target_speed - speed[i-1]
    ) * dt / time_constant

    speed[i] = speed[i-1] + ds

# -------------------------
# Plot
# -------------------------

plt.figure(figsize=(10,5))

plt.plot(time, speed, linewidth=2)

plt.title("DC Motor Speed Response")
plt.xlabel("Time (s)")
plt.ylabel("Speed (RPM)")

plt.grid(True)

plt.savefig(
    "images/dc_motor_speed_response.png",
    dpi=300
)

print(f"Final Motor Speed = {speed[-1]:.1f} RPM")

plt.show()