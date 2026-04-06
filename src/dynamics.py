import numpy as np

def rhs(t, y, q, m, B):
    x = y[0:3]
    v = y[3:6]

    dvdt = (q / m) * np.cross(v, B)
    dxdt = v

    return np.concatenate([dxdt, dvdt])