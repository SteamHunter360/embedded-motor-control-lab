import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

# ------------------------
# Parameters
# ------------------------

motor_speed = float(input("Enter motor speed (RPM): "))

simulation_time = 5
dt = 0.01

time = np.arange(0, simulation_time, dt)

encoder_resolution = 360

# ------------------------
# Calculate encoder pulses
# ------------------------

revolutions_per_second = motor_speed / 60

total_revolutions = revolutions_per_second * time

encoder_counts = total_revolutions * encoder_resolution

# ------------------------
# Plot
# ------------------------

plt.figure(figsize=(10,5))

plt.plot(
    time,
    encoder_counts,
    linewidth=2
)

plt.title("Encoder Counts vs Time")

plt.xlabel("Time (s)")
plt.ylabel("Encoder Counts")

plt.grid(True)

plt.savefig(
    "images/encoder_counts.png",
    dpi=300
)

print()

print(f"Final Encoder Count = {encoder_counts[-1]:.0f}")

plt.show()