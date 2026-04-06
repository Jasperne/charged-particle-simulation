def euler_step(f, t, y, dt, *args):
    return y + dt * f(t, y, *args)