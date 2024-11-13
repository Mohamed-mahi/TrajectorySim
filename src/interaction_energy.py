import os
import numpy as np
import matplotlib.pyplot as plt


def plot_interaction_energy_y_axis(pes, y_range, z_values, save_dir="plots/3_interaction_energy/"):
    """Plot the interaction energy along the y-axis for different z-values."""
    os.makedirs(save_dir, exist_ok=True)

    plt.figure(figsize=(10, 6))
    for z in z_values:
        energies = [pes.V(0, y, z) for y in y_range]
        # Add markers for each z value
        if z == 3.0:
            marker = 'o'  # Circles for z = 3.0
        elif z == 3.2:
            marker = 's'  # Squares for z = 3.2
        elif z == 3.6:
            marker = '^'  # Triangles for z = 3.6
        plt.plot(y_range, np.array(energies) * 1000, marker=marker, label=f'z = {z} Å')  # Convert to meV/atom

    # Titles, labels, legend, and grid
    plt.title("The Interaction Energy along y-axis for different values at (x=0)")
    plt.xlabel("Distance along y (Å)")
    plt.ylabel("V(x=0, y, z) (meV/atom)")
    plt.legend()
    plt.grid(True)

    # Save and show
    plt.savefig(f"{save_dir}/interaction_energy_y_axis.png")
    plt.show()
    plt.close()


def plot_interaction_energy_stacking(pes, z_values, save_dir="plots/3_interaction_energy/"):
    """Plot the interaction energy for AA and AB stacking."""
    os.makedirs(save_dir, exist_ok=True)

    # Calculate interaction energies
    energy_AA = [pes.V(0, 0, z) for z in z_values]  # AA stacking
    energy_AB = [pes.V(1, 1, z) for z in z_values]  # AB stacking

    # Main plot
    plt.figure(figsize=(10, 6))
    plt.plot(z_values, energy_AA, 'ro-', label="AA stacking")
    plt.plot(z_values, energy_AB, 'k^-', label="AB stacking")

    # Titles, labels, and legend
    plt.title("The interaction energy of two layers as a function of separation")
    plt.xlabel("Distance along z (Å)")
    plt.ylabel("V(z) (meV/atom)")
    plt.legend()

    # Zoom-in plot
    plt.axes([0.4, 0.55, 0.25, 0.3])  # [left-right, bottom-up, width, height]
    plt.plot(z_values, energy_AA, 'ro-')
    plt.plot(z_values, energy_AB, 'k^-')
    plt.xlim(3.0, 4.0)
    plt.ylim(-45, -10)
    plt.grid(True)

    # Save and show
    plt.savefig(f"{save_dir}/interaction_energy_stacking.png")
    plt.show()
    plt.close()
