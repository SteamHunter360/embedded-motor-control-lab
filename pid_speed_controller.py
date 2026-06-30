import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

# Simulation settings
dt = 0.01
simulation_time = 5
time = np.arange(0, simulation_time, dt)

# Motor settings
time_constant = 0.5
max_speed = 1000

# Target speed
setpoint = float(input("Enter target speed (RPM): "))

# PID gains
Kp = 0.8
Ki = 0.4
Kd = 0.05

speed = np.zeros(len(time))
control_signal = np.zeros(len(time))

integral = 0
previous_error = 0

for i in range(1, len(time)):
    error = setpoint - speed[i - 1]

    integral += error * dt
    derivative = (error - previous_error) / dt

    control = Kp * error + Ki * integral + Kd * derivative
    control = max(0, min(max_speed, control))

    control_signal[i] = control

    speed[i] = speed[i - 1] + (control - speed[i - 1]) * dt / time_constant

    previous_error = error

plt.figure(figsize=(10, 5))
plt.plot(time, speed, label="Motor Speed")
plt.axhline(setpoint, linestyle="--", label="Target Speed")

plt.title("PID Speed Control Response")
plt.xlabel("Time (s)")
plt.ylabel("Speed (RPM)")
plt.grid(True)
plt.legend()

plt.savefig("images/pid_speed_control_response.png", dpi=300)

print(f"Final Speed = {speed[-1]:.1f} RPM")
print(f"Target Speed = {setpoint:.1f} RPM")
print(f"Final Error = {setpoint - speed[-1]:.2f} RPM")

plt.show()