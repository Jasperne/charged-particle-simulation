
# Charged Particle Simulation

A first computational physics project exploring the motion of a charged particle in electromagnetic fields and the impact of numerical integration methods.

## Overview

This project simulates the dynamics of a charged particle under the Lorentz force and compares different numerical integrators:
- Explicit Euler method
- Runge–Kutta method of order 4 (RK4)

The focus is on how the choice of integrator affects trajectory accuracy and energy conservation.

## Magnetic Field Only (B ≠ 0, E = 0)

In a constant magnetic field, the analytical expectation is circular motion with constant kinetic energy.

### Observations (Euler)
- Trajectory is approximately circular
- Visible numerical drift over time
- Energy is not conserved (systematic increase)

### Improvement with RK4
- Trajectory remains stable and close to a perfect circle
- Energy is nearly conserved
- Significantly higher numerical accuracy

## Numerical Methods Comparison

Both integrators are applied to the same initial conditions.

- **Euler**: Uses only the local slope → accumulates error over time
- **RK4**: Uses multiple intermediate evaluations → much higher accuracy

Result:
- Euler diverges from the expected solution
- RK4 closely matches the theoretical behavior

## Timestep Study

The timestep \( \Delta t \) has a strong influence on accuracy:

- Reducing \( \Delta t \) improves Euler results
- However, Euler still does not conserve energy exactly
- RK4 remains accurate even for comparatively larger timesteps

Conclusion:
- Numerical error depends on timestep size
- Higher-order methods (like RK4) reduce error much more efficiently

## Current Status

- Lorentz force model implemented
- Euler and RK4 integrators implemented
- Trajectory comparison completed
- Energy conservation analysis added
- Quantitative error analysis between methods included

## Next Steps

- Add analytical reference solution for pure magnetic field case
- Extend simulations to combined electric and magnetic fields
- Explore parameter studies and long-term stability