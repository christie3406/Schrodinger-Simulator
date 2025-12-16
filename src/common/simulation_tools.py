import numpy as np
import scipy.sparse
import scipy.linalg

def hamiltonian(N, dx, V=None, hbar, m):
    # Construct Hamiltonian as a sparse matrix.
    L = scipy.sparse.diags([1, -2, 1], offsets=[-1, 0, 1], shape=(N, N))
    H = - (hbar**2) * L / (2 * m * dx**2)
    if V is not None:
        H += scipy.sparse.spdiags(V, 0, N, N)
    return H.tocsc()

def time_evolution_operator(H, dt, hbar):
    # Compute sparse matrix exponential for time evolution.
    generator = -1j * H * dt / hbar
    U = scipy.sparse.linalg.expm(generator)
    if hasattr(U, "data"):
        U.data[np.abs(U.data) < 1e-10] = 0
    return U.tocsc()

def simulate(psi0, H, dt, max_time_val):
    # Simulate time evolution of a wave function.
    # Returns: times, probability_densities, real, imaginary lists
    psi = psi0.copy()
    U = time_evolution_operator(H, dt)

    times = []
    probability_densities = []
    real = []
    imaginary = []

    t = 0
    while t < max_time_val:
        times.append(t)
        probability_densities.append(np.abs(psi)**2)
        real.append(np.real(psi))
        imaginary.append(np.imag(psi))
        psi = U @ psi
        t += dt

    return times, probability_densities, real, imaginary


def gaussian_wavepacket(x, x0, sigma0, p0):
    # Gaussian wavepacket at x0 +/- width sigma0, with initial impuls p0.
    A = (2 * np.pi * sigma0**2)**(-0.25)
    return A * np.exp(1j*p0*x - ((x - x0)/(2 * sigma0))**2)

