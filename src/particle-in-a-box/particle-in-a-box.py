import numpy as np
import math

from src.common.simulation_tools import hamiltonian, time_evolution_operator, simulate, gaussian_wavepacket
from src.common.animation import animation
from src.common.potentials import infinite_potential

# Eigenstate of the infinite square well
def eigenstate_isw(n, a, x):
    return np.sqrt(2/a)*np.sin(n*np.pi*x/a)

# SETTINGS
grid = 500 # number of points
max_time = 500 # number of time steps
dt = 20.0 # time step
m = 1   # mass
hbar = 1 # reduced Planck constant
a = 200 # length of box
sigma0 = 10.0 # width of wavepacket
p0 = 2 # initial momentum
n = 1 # energy level for eigenstate
initial_wavefunction = 0  # 0 for guassian wavepacket, 1 for eigenstate

# Print default settings
print("Default settings:")
print(f"  grid = {grid}")
print(f"  max_time = {max_time}")
print(f"  dt = {dt}")
print(f"  m = {m}")
print(f"  hbar = {hbar}")
print(f"  a = {a}")
print(f"  sigma0 = {sigma0}")
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
        print("4: a (length of box)")
        print("5: sigma0 (wavepacket width)")
        print("6: p0 (initial momentum)")
        print("7: n (energy level for eigenstate)")
        print("8: psi0 (initial wavefunction)")
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
            a = float(input("Enter new box length a: "))
        elif choice == "5":
            sigma0 = float(input("Enter new sigma0: "))
        elif choice == "6":
            p0 = float(input("Enter new p0: "))
        elif choice == "7":
            n = int(input("Enter new energy level n: "))
        elif choice == "8":
            initial_wavefunction = int(input("Enter 0 for gaussian wavepacket, 1 for eigenstate: "))
        else:
            print("Invalid choice, try again.")

x, dx = np.linspace(0, a, grid, endpoint=False, retstep=True) # position grid

if initial_wavefunction == 0:
    psi0 = gaussian_wavepacket(x, x0=a/2, sigma0=sigma0, p0= p0) # initial wavefunction
else:
    psi0 = eigenstate_isw(n=n, a=a, x=x)

V = infinite_potential(grid_size=grid)

# MAIN
H = hamiltonian(grid, dx, V=V, hbar=hbar, m=m)
times, probability_densities, real, imaginary = simulate(psi0, H, dt=dt, max_time_val=max_time)
animation(x, times, probability_densities, real, imaginary)

# Check for normalisation
print(sum(probability_densities[0])/(grid/a))
