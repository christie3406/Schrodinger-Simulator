import numpy as np


# INFINITE POTENTIAL
def infinite_potential(grid_size=500):
    V = np.zeros(grid_size)
    V[0] = 1e10  # Use large finite value instead of inf to avoid NaN
    V[-1] = 1e10
    return V

# HARMONIC POTENTIAL
def harmonic_potential(w, x):
    return (w * x)**2 /2

# POTENTIAL BARRIER
def rectangular_potential_barrier(x, V0, w):
    # Rectangular potential barrier of height V0 and width w.
    return np.where((0 <= x) & (x < w), V0, 0.0)
