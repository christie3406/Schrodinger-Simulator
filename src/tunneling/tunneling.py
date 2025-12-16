import numpy as np
from scipy import constants
from scipy.optimize import root_scalar

from src.common.simulation_tools import hamiltonian, time_evolution_operator, simulate, gaussian_wavepacket
from src.common.animation import animation
from src.common.potentials import rectangular_potential_barrier

# SETTINGS
grid = 1024 # number of points
max_time = 20 # number of time steps
dt = 1 # time step
m = 1   # mass
hbar = 1 # reduced Planck constant
a = 128 # x position length
e = 10   # Energy of the wave packet
V0 = 5  # Potential energy barrier
w = 1  # width of the barrier
sigma0 = 3.0 # width of wavepacket
x0 = -30.0 # initial position of wavepacket
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
print(f"  e = {e}")
print(f"  V0 = {V0}")
print(f"  w = {w}")
print(f"  sigma0 = {sigma0}")
print(f"  x0 = {x0}")
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
        print("5: e (energy of wave packet)")
        print("6: V0 (potential barrier height)")
        print("7: w (barrier width)")
        print("8: sigma0 (wavepacket width)")
        print("9: x0 (initial position)")
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
            e = float(input("Enter new energy e: "))
        elif choice == "6":
            V0 = float(input("Enter new potential barrier height V0: "))
        elif choice == "7":
            w = float(input("Enter new barrier width w: "))
        elif choice == "8":
            sigma0 = float(input("Enter new sigma0: "))
        elif choice == "9":
            x0 = float(input("Enter new initial position x0: "))
        else:
            print("Invalid choice, try again.")

x, dx = np.linspace(-a/2, a/2, grid, endpoint=False, retstep=True)
psi0 = gaussian_wavepacket(x, x0=x0, sigma0=sigma0, p0=np.sqrt(2*e))
V = rectangular_potential_barrier(x=x, V0=V0, w=w)  # w = width of the barrier

# MAIN
H = hamiltonian(grid, dx, V=V, hbar=hbar, m=m)
times, probability_densities, real, imaginary = simulate(psi0, H, dt=dt, max_time_val=max_time)
animation(x, times, probability_densities, real, imaginary, tunneling=True)

print(sum(probability_densities[0])/(grid/a))

transmission = sum(probability_densities[15][520:-1])/(grid/a)
print(round(transmission, 1))

