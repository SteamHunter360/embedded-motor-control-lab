import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

# --------------------------
# Motor Parameters
# --------------------------

time_constant = 0.5
max_speed = 1000      # RPM
dt = 0.01
simulation_time = 5

time = np.arange(0, simulation_time, dt)

# User input
duty_cycle = float(input("Enter PWM duty cycle (0-100%): "))

duty_cycle = max(0, min(100, duty_cycle))

target_speed = max_speed * (duty_cycle / 100)

speed = np.zeros(len(time))

# --------------------------
# Simulation
# --------------------------

for i in range(1, len(time)):

    speed[i] = speed[i-1] + (
        target_speed - speed[i-1]
    ) * dt / time_constant

# --------------------------
# Plot
# --------------------------

plt.figure(figsize=(10,5))

plt.plot(time, speed, linewidth=2)

plt.title(f"Motor Speed Response ({duty_cycle:.0f}% PWM)")
plt.xlabel("Time (s)")
plt.ylabel("Speed (RPM)")
plt.grid(True)

plt.savefig("images/pwm_motor_response.png", dpi=300)

print(f"\nTarget Speed: {target_speed:.1f} RPM")
print(f"Final Speed : {speed[-1]:.1f} RPM")

plt.show()