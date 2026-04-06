import numpy as np


def rhs(t, y, q, m, B):
    """
    Right-hand side of the ODE system for a charged particle
    in a constant magnetic field.

    Parameters
    ----------
    t : float
        Current time (not used here, but kept for generality).
    y : np.ndarray
        State vector [x, y, z, vx, vy, vz].
    q : float
        Particle charge.
    m : float
        Particle mass.
    B : np.ndarray
        Magnetic field vector [Bx, By, Bz].

    Returns
    -------
    np.ndarray
        Time derivative of the state vector.
    """
    v = y[3:6]

    dxdt = v
    dvdt = (q / m) * np.cross(v, B)

    return np.concatenate([dxdt, dvdt])