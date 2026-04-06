
# Charged Particle Simulation

My very first computational physics project.

## First results

Simulated a charged particle in a constant magnetic field using Euler integration.

Observation:
 trajectory is approximately circular
 small numerical drift is visible (expected from Euler method, due to inaccuracy)

 Added RK4 integrator to improve numerical stability.

 ## Numerical methods comparison

Simulated the motion of a charged particle in a constant magnetic field.

Two integration methods were compared:
Euler method
 Runge-Kutta 4 named as RK4 in the following

Observations:
Euler shows visible numerical drift (trajectory expands over time)
RK4 maintains a stable circular trajectory, showing more accuracy