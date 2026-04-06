import numpy as np
import matplotlib.pyplot as plt

from dynamics import rhs
from integrators import euler_step

q = 1.0
m = 1.0
B = np.array([0.0, 0.0, 1.0])

y = np.array([
    1.0, 0.0, 0.0,
    0.0, 1.0, 0.0
])

dt = 0.01
steps = 2000
t = 0.0

trajectory = []

for _ in range(steps):
    trajectory.append(y[:3].copy())
    y = euler_step(rhs, t, y, dt, q, m, B)
    t += dt

trajectory = np.array(trajectory)

plt.figure()
plt.plot(trajectory[:, 0], trajectory[:, 1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Charged particle trajectory (Euler)")
plt.axis("equal")
plt.grid(True)
plt.show()