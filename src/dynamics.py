import numpy as np


def rhs(t, y, q, m, E, B):
   
    v = y[3:6]

    dxdt = v
    dvdt = (q / m) * (E + np.cross(v, B))

    return np.concatenate([dxdt, dvdt])