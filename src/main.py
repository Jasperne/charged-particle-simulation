import numpy as np
import matplotlib.pyplot as plt

from dynamics import rhs
from integrators import euler_step, rk4_step


# Physical parameters
q = 1.0
m = 1.0
B = np.array([0.0, 0.0, 1.0])

# Initial state: [x, y, z, vx, vy, vz]
y0 = np.array([
    1.0, 0.0, 0.0,
    0.0, 1.0, 0.0
])

# Simulation parameters
dt = 0.01
steps = 2000

# Separate states for Euler and RK4
y_euler = y0.copy()
y_rk4 = y0.copy()

trajectory_euler = []
trajectory_rk4 = []

t = 0.0

for _ in range(steps):
    trajectory_euler.append(y_euler[:3].copy())
    trajectory_rk4.append(y_rk4[:3].copy())

    y_euler = euler_step(rhs, t, y_euler, dt, q, m, B)
    y_rk4 = rk4_step(rhs, t, y_rk4, dt, q, m, B)

    t += dt

trajectory_euler = np.array(trajectory_euler)
trajectory_rk4 = np.array(trajectory_rk4)

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