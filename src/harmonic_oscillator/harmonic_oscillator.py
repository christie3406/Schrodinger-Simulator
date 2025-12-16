# DIRECTORIES
import numpy as np
import numpy.polynomial.hermite as Herm
import math

from src.common.simulation_tools import hamiltonian, time_evolution_operator, simulate, gaussian_wavepacket
from src.common.animation import animation
from src.common.potentials import harmonic_potential


# INITIAL WAVEFUNCTION
def eigenstate_qho(w, n, x):
    def hermite(x, n):
        xi = np.sqrt(m * w / hbar) * x
        herm_coeffs = np.zeros(n + 1)
        herm_coeffs[n] = 1
        return Herm.hermval(xi, herm_coeffs)

    xi = np.sqrt(m * w / hbar) * x
    prefactor = 1. / math.sqrt(2. ** n * math.factorial(n)) * (m * w / (np.pi * hbar)) ** (0.25)
    psi = prefactor * np.exp(- xi ** 2 / 2) * hermite(x, n)
    return psi

# SETTINGS
grid = 500 # number of points
max_time = 200 # number of time steps
dt = 5.0 # time step
m = 1   # mass
hbar = 1 # reduced Planck constant
a = 128 # x position length
w = 1/50 # angular frequency of harmonic oscillator
sigma0 = 3.0 # width of wavepacket
x0 = -30 # initial position of wavepacket
p0 = 0.0 # initial momentum
n = 1 # energy level for eigenstate
initial_wavefunction = 0  # 0 for gaussian wavepacket, 1 for eigenstate

# Print default settings
print("Default settings:")
print(f"  grid = {grid}")
print(f"  max_time = {max_time}")
print(f"  dt = {dt}")
print(f"  m = {m}")
print(f"  hbar = {hbar}")
print(f"  a = {a}")
print(f"  w = {w}")
print(f"  sigma0 = {sigma0}")
print(f"  x0 = {x0}")
print(f"  p0 = {p0}")
print(f"  n = {n}")
print(f"  initial_wavefunction = {'Gaussian' if initial_wavefunction==0 else 'Eigenstate'}")

# User input to change settings
use_default = input("Use default settings? (y/n): ").strip().lower()

if use_default != "y":
    while True:
        print("\nChoose a parameter to change:")
        print("1: grid (number of points)")
        print("2: max_time (number of steps)")
        print("3: dt (time step)")
        print("4: a (position length)")
        print("5: w (angular frequency)")
        print("6: sigma0 (wavepacket width)")
        print("7: x0 (initial position)")
        print("8: p0 (initial momentum)")
        print("9: n (energy level for eigenstate)")
        print("10: psi0 (initial wavefunction)")
        print("0: finished changing")
        choice = input("Enter number: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            grid = int(input("Enter new grid: "))
        elif choice == "2":
            max_time = int(input("Enter new max_time: "))
        elif choice == "3":
            dt = float(input("Enter new dt: "))
        elif choice == "4":
            a = float(input("Enter new position length a: "))
        elif choice == "5":
            w = float(input("Enter new angular frequency w: "))
        elif choice == "6":
            sigma0 = float(input("Enter new sigma0: "))
        elif choice == "7":
            x0 = float(input("Enter new initial position x0: "))
        elif choice == "8":
            p0 = float(input("Enter new p0: "))
        elif choice == "9":
            n = int(input("Enter new energy level n: "))
        elif choice == "10":
            initial_wavefunction = int(input("Enter 0 for gaussian wavepacket, 1 for eigenstate: "))
        else:
            print("Invalid choice, try again.")

x, dx = np.linspace(-a/2, a/2, grid, endpoint=False, retstep=True)

if initial_wavefunction == 0:
    psi0 = gaussian_wavepacket(x, x0=x0, sigma0=sigma0, p0=p0)
else:
    psi0 = eigenstate_qho(w=w, n=n, x=x)

V = harmonic_potential(w=w, x=x)

# MAIN
H = hamiltonian(grid, dx, V=V, hbar=hbar, m=m)
times, probability_densities, real, imaginary = simulate(psi0, H, dt=dt, max_time_val=max_time)
animation(x, times, probability_densities, real, imaginary)

print(sum(probability_densities[0])/(grid/a))