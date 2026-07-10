# Embedded Motor Control Laboratory

A professional Python-based embedded systems project that simulates the core components of a closed-loop DC motor speed control system.

This project demonstrates the software architecture commonly used in embedded motor control applications before deployment to physical hardware such as Arduino, STM32 or other microcontrollers.

The repository includes:

- DC motor dynamic simulation
- PWM motor control
- Encoder simulation
- PID speed controller
- PID tuning comparison
- Performance analysis
- Engineering visualisations
- Automated testing
- Continuous Integration (GitHub Actions)

---

# Features

## DC Motor Simulation

- First-order DC motor model
- Adjustable time constant
- Adjustable simulation timestep
- Adjustable target speed
- Dynamic motor speed response

---

## PWM Motor Control

- Duty-cycle based motor control
- Target speed calculation
- PWM signal simulation
- Speed response visualisation

---

## Encoder Simulation

- Incremental encoder model
- Adjustable encoder resolution
- Encoder count generation
- Position feedback simulation

---

## PID Speed Controller

Closed-loop motor speed control using

- Proportional control
- Integral control
- Derivative control

Features include

- Speed tracking
- Control effort calculation
- Tunable gains
- Stable closed-loop response

---

## PID Tuning Comparison

Three controller configurations are compared:

- Conservative
- Balanced
- Aggressive

Performance metrics include:

- Steady-state error
- RMS speed error
- Overshoot
- Settling time
- RMS control effort

---

## Performance Analysis

The project automatically calculates engineering metrics including:

- Steady-state error
- Maximum speed error
- RMS speed error
- Overshoot
- Settling time

These metrics allow quantitative evaluation of controller performance.

---

## Validation

The software validates engineering inputs including:

- Target speed
- PWM duty cycle
- Simulation time
- Time step
- Motor time constant
- Encoder resolution
- PID gains

Invalid parameters generate informative exceptions rather than undefined behaviour.

---

## Automated Testing

The project contains **42 automated unit tests** covering:

- Motor simulation
- PWM control
- Encoder simulation
- PID controller
- PID tuning
- Motor analysis
- Validation

Example:

```bash
python -m pytest tests/ -v
```

Current status:

```
42 passed
```

---

# Continuous Integration

GitHub Actions automatically:

- installs dependencies
- runs the full test suite
- validates every push
- validates pull requests

---

# Repository Structure

```text
embedded-motor-control-lab
│
├── images/
│   ├── dc_motor_speed_response.png
│   ├── encoder_counts.png
│   ├── pid_control_effort.png
│   ├── pid_speed_control_response.png
│   ├── pid_tuning_comparison.png
│   ├── pwm_command_signal.png
│   └── pwm_motor_response.png
│
├── src/
│   ├── dc_motor_simulation.py
│   ├── encoder_simulation.py
│   ├── motor_analysis.py
│   ├── motor_visualisation.py
│   ├── pid_speed_controller.py
│   ├── pid_tuning.py
│   ├── pid_tuning_visualisation.py
│   ├── pwm_control.py
│   └── validation.py
│
├── tests/
│
├── analysis_demo.py
├── encoder_demo.py
├── motor_demo.py
├── pid_demo.py
├── pid_tuning_demo.py
├── pwm_demo.py
│
├── requirements.txt
└── README.md
```

---

# Demonstration Results

## DC Motor Simulation

```
Target Speed:        1000 RPM
Final Speed:         999.96 RPM
Steady-State Error:  0.0419 RPM
RMS Speed Error:     224.73 RPM
Settling Time:       1.94 s
```

---

## PWM Control

```
PWM Duty Cycle:      60%
Target Speed:        600 RPM
Final Speed:         599.97 RPM
Steady-State Error:  0.0251 RPM
RMS Speed Error:     134.84 RPM
```

---

## Encoder Simulation

```
Motor Speed:         750 RPM
Final Encoder Count: 22455
```

---

## PID Speed Control

```
Target Speed:        750 RPM
Final Speed:         736.95 RPM
Steady-State Error:  13.05 RPM
RMS Speed Error:     156.34 RPM
Overshoot:           0%
```

---

## PID Tuning Comparison

| Controller   | Steady-State Error |  RMS Error |  Settling Time | Overshoot |
| ------------ | -----------------: | ---------: | -------------: | --------: |
| Conservative |         128.15 RPM | 296.82 RPM | Did not settle |        0% |
| Balanced     |          13.05 RPM | 156.34 RPM |         4.74 s |        0% |
| Aggressive   |           4.78 RPM | 137.87 RPM |         2.85 s |        0% |

---

# Generated Visualisations

The project automatically generates engineering plots including:

- DC motor speed response
- PWM motor response
- PWM command signal
- Encoder counts
- PID speed response
- PID control effort
- PID tuning comparison

These are saved in the `images/` directory.

---

# Engineering Concepts Demonstrated

- Embedded systems software architecture
- Closed-loop feedback control
- DC motor modelling
- PWM motor control
- Incremental encoder feedback
- PID controller implementation
- Controller tuning
- Performance analysis
- Software validation
- Automated testing
- Continuous Integration
- Scientific visualisation

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/embedded-motor-control-lab.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Demos

Motor simulation

```bash
python motor_demo.py
```

PWM simulation

```bash
python pwm_demo.py
```

Encoder simulation

```bash
python encoder_demo.py
```

PID control

```bash
python pid_demo.py
```

PID tuning comparison

```bash
python pid_tuning_demo.py
```

---

# Running Tests

```bash
python -m pytest tests/ -v
```

---

# Future Work

## Phase 2 – Hardware Implementation

The current repository focuses on software simulation.

Future development will deploy the control algorithms to physical hardware including:

- Arduino implementation
- STM32 implementation
- Real DC motor
- Quadrature encoder
- Hardware PWM generation
- Interrupt-driven encoder feedback
- Serial telemetry
- Real-time speed estimation
- Hardware-in-the-loop testing

---

# Author

**Daniel Olowe**

Mechanical Engineering Student

Specialising in:

- Robotics
- Embedded Systems
- Control Engineering
- Mechatronics
- Engineering Software
- Machine Learning for Engineering

GitHub Portfolio:
https://github.com/SteamHunter360
