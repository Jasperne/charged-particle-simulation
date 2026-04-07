import numpy as np
import matplotlib.pyplot as plt

from dynamics import rhs
from integrators import euler_step, rk4_step


# Physical parameters (do not change these)
q = 1.0
m = 1.0
B = np.array([0.0, 0.0, 1.0])
E = np.array([0.1, 0.0, 0.0])

# Initial state: [x, y, z, vx, vy, vz]
y0 = np.array([
    1.0, 0.0, 0.0,
    0.0, 1.0, 0.0
])

# Simulation parameters (can be varied if wanted will change results tho)
dt = 0.01
steps = 2000

# Separate states for Euler and RK4
y_euler = y0.copy()
y_rk4 = y0.copy()

trajectory_euler = []
energy_euler = []
energy_rk4 = []
trajectory_rk4 = []

t = 0.0

for _ in range(steps):
    trajectory_euler.append(y_euler[:3].copy())
    trajectory_rk4.append(y_rk4[:3].copy())

    v_euler = y_euler[3:6]
    v_rk4 = y_rk4[3:6]

    energy_euler.append(0.5 * m * np.dot(v_euler, v_euler))
    energy_rk4.append(0.5 * m * np.dot(v_rk4, v_rk4))

    y_euler = euler_step(rhs, t, y_euler, dt, q, m, E, B,)
    y_rk4 = rk4_step(rhs, t, y_rk4, dt, q, m, E, B,)

    t += dt

trajectory_euler = np.array(trajectory_euler)
trajectory_rk4 = np.array(trajectory_rk4)
energy_euler = np.array(energy_euler)
energy_rk4 = np.array(energy_rk4)

position_error = np.linalg.norm(trajectory_euler - trajectory_rk4, axis=1)
energy_error = np.abs(energy_euler - energy_rk4)

# Plot trajectories in the x-y plane
plt.figure(figsize=(7, 7))
plt.plot(trajectory_euler[:, 0], trajectory_euler[:, 1], label="Euler")
plt.plot(trajectory_rk4[:, 0], trajectory_rk4[:, 1], label="RK4")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Charged Particle Trajectory: Euler vs RK4")
plt.axis("equal")
plt.legend()
plt.grid(True)
plt.show()

# Plot energy over time
plt.figure()

plt.plot(energy_euler, label="Euler")
plt.plot(energy_rk4, label="RK4")

plt.xlabel("Step")
plt.ylabel("Energy")
plt.title("Energy conservation")
plt.legend()
plt.grid(True)

plt.show()

# Plot error between Euler and RK4
plt.figure()

plt.plot(position_error, label=r"$\|x_{\mathrm{Euler}} - x_{\mathrm{RK4}}\|$")
plt.plot(energy_error, label=r"$|E_{\mathrm{Euler}} - E_{\mathrm{RK4}}|$")

plt.xlabel(r"Step $n$")
plt.ylabel(r"Error")
plt.title("Difference between Euler and RK4")
plt.legend()
plt.grid(True)

plt.show()