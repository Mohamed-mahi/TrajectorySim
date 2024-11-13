from src import PES, plot_force_components, trajectories_with_potential
from src.interaction_energy import plot_interaction_energy_y_axis, plot_interaction_energy_stacking
from config.simulation_config import PES_PARAMETERS, SIMULATION_PARAMETERS, GRID_PARAMETERS
import numpy as np
import os
import matplotlib.pyplot as plt

def main():
    # Create directories for plots if they don't exist
    os.makedirs("plots/1_pes", exist_ok=True)
    os.makedirs("plots/2_forces_components", exist_ok=True)
    os.makedirs("plots/3_interaction_energy", exist_ok=True)
    os.makedirs("plots/trajectory_output", exist_ok=True)

    # Initialize PES using parameters from config
    pes = PES(**PES_PARAMETERS)

    # Grid setup for PES and forces
    x_range = np.linspace(GRID_PARAMETERS["x_min"], GRID_PARAMETERS["x_max"], GRID_PARAMETERS["resolution"])
    y_range = np.linspace(GRID_PARAMETERS["y_min"], GRID_PARAMETERS["y_max"], GRID_PARAMETERS["resolution"])
    X, Y = np.meshgrid(x_range, y_range)

    # 1. Plot PES (unchanged)
    energies = np.array([[pes.V(x, y, 3.2) for x in x_range] for y in y_range])
    plt.contourf(X, Y, energies.T, levels=64, cmap="jet")
    plt.colorbar(label="Potential Energy (meV)")
    plt.title("Potential Energy Surface (PES)")
    plt.xlabel("X (Å)")
    plt.ylabel("Y (Å)")
    plt.savefig("plots/1_pes/pes_plot.png")
    plt.close()

    # 2. Plot force components (unchanged)
    forces_x = np.zeros_like(X)
    forces_y = np.zeros_like(Y)
    forces_z = np.zeros_like(X)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            fx, fy, fz = pes.force(X[i, j], Y[i, j], 3.2)
            forces_x[i, j] = fx
            forces_y[i, j] = fy
            forces_z[i, j] = fz

    plot_force_components(X, Y, forces_x, forces_y, forces_z)

    # 3. Plot interaction energy along y-axis
    z_values_y_axis = [3.0, 3.2, 3.6]
    plot_interaction_energy_y_axis(pes, y_range, z_values_y_axis)

    # 4. Plot interaction energy for stacking
    z_values_stacking = np.linspace(3.0, 6.0, 100)
    plot_interaction_energy_stacking(pes, z_values_stacking)

    # 5. Plot trajectory simulation (unchanged)
    trajectories_with_potential(
        pes,
        SIMULATION_PARAMETERS["dt"],
        SIMULATION_PARAMETERS["gamma"],
        SIMULATION_PARAMETERS["temp"],
        SIMULATION_PARAMETERS["mass"],
        SIMULATION_PARAMETERS["nsteps"],
        SIMULATION_PARAMETERS["num_particles"],
        SIMULATION_PARAMETERS["initial_variance"]
    )

if __name__ == "__main__":
    main()
