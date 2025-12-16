# Schrödinger Simulator

A comprehensive quantum mechanics simulator that models fundamental quantum systems: the particle in a box, the quantum harmonic oscillator, and quantum tunneling through potential barriers.

## Overview

This project provides interactive simulations of key quantum mechanical phenomena, allowing users to explore wave function behavior, probability densities, and time evolution of quantum states in various potential configurations.

## Features

- **Interactive User Interface**: Customize simulation parameters (grid size, time steps, potential strengths, etc.)
- **Multiple Quantum Systems**: 
  - Particle in an infinite square well
  - Quantum harmonic oscillator
  - Quantum tunneling through potential barriers
- **Real-time Animations**: Visualize wave function evolution and probability densities
- **Numerical Methods**: Uses sparse matrix exponentials for efficient time evolution

## Running the Simulations

Each simulator is interactive and allows you to customize parameters:

### Particle in a Box
```bash
python src/particle-in-a-box/particle-in-a-box.py
```
Simulates a particle confined in an infinite potential well. Choose between Gaussian wavepackets or energy eigenstates.

### Harmonic Oscillator
```bash
python src/harmonic_oscillator/harmonic_oscillator.py
```
Models the quantum harmonic oscillator with interactive parameter control for frequency, wavepacket properties, and eigenstates.

### Quantum Tunneling
```bash
python src/tunneling/tunneling.py
```
Demonstrates wave function tunneling through potential barriers, with transmission coefficient calculations.

## Physical Constants

Default values (in natural units):
- Mass: m = 1
- Reduced Planck constant: ℏ = 1
- Grid points: 500-1024
- Simulation time: 20-500 steps

All parameters can be adjusted interactively when running a simulation.

## Dependencies

- NumPy
- SciPy (sparse matrices, linear algebra)
- Matplotlib (visualization)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

When running any simulator:
1. View default settings
2. Choose whether to use defaults or customize parameters
3. Interactively modify settings as needed
4. Press 0 to finish and start the simulation
5. Watch the animation of the wave function evolution

## Physical Concepts

- **Wave Function**: Represented as complex-valued states on a spatial grid
- **Time Evolution**: Computed using sparse matrix exponentials: U = exp(-iHt/ℏ)
- **Probability Density**: |ψ(x)|² shown in animations
- **Quantum Tunneling**: Wave function penetration through classically forbidden regions 

