import numpy as np                   
import matplotlib.pyplot as plt      
from matplotlib.animation import FuncAnimation

# ANIMATION
def animation(x, times, probability_densities, real, imaginary, show_real_imaginary=False, tunneling = False):   
    fig, ax = plt.subplots()
    probability_line, = ax.plot(x, probability_densities[0], label="Psi^2")
    if (show_real_imaginary):
        real_line, = ax.plot(x, real[0], label='Re(Psi)')
        imaginary_line, = ax.plot(x, imaginary[0], label='Im(Psi)')
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(0,np.max(probability_densities))
    if (show_real_imaginary):
        ax.set_ylim(np.min(imaginary), np.max(real))
    
    # transparent area representing potential barrier
    if tunneling:   
        ax.fill_between([0, 1], 0, np.max(probability_densities), color='gray', alpha=0.5)

    def update(frame):
        probability_line.set_ydata(probability_densities[frame])
        if (show_real_imaginary):
            real_line.set_ydata(real[frame])
            imaginary_line.set_ydata(imaginary[frame])
        ax.set_title(f"Time: {times[frame]}")

    ani = FuncAnimation(fig, update, frames=len(probability_densities), interval=100)
    ax.legend()
    plt.xlabel('x')
    plt.ylabel('Wave function')
    plt.show()