def euler_step(f, t, y, dt, *args):
   
    return y + dt * f(t, y, *args)


def rk4_step(f, t, y, dt, *args):
  
    k1 = f(t, y, *args)
    k2 = f(t + dt / 2, y + dt / 2 * k1, *args)
    k3 = f(t + dt / 2, y + dt / 2 * k2, *args)
    k4 = f(t + dt, y + dt * k3, *args)

    return y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)