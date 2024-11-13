import numpy as np
from src.interaction_energy import plot_interaction_energy_y_axis, plot_interaction_energy_stacking
from src.pes import PES

def test_plot_interaction_energy_y_axis():
    pes = PES(1.63093e6, 3.347616, 8184.7, 2.75075e6, 3.349208, 8258.11, 2.462)
    y_range = np.linspace(0, 10, 50)
    z_values = [3.0, 3.2, 3.6]

    # Call the plotting function
    plot_interaction_energy_y_axis(pes, y_range, z_values, save_dir="test_plots/interaction_energy/")
    # Check that the plot is saved correctly (manually or by verifying the directory)

def test_plot_interaction_energy_stacking():
    pes = PES(1.63093e6, 3.347616, 8184.7, 2.75075e6, 3.349208, 8258.11, 2.462)
    z_values = np.linspace(3.0, 6.0, 50)

    # Call the plotting function
    plot_interaction_energy_stacking(pes, z_values, save_dir="test_plots/interaction_energy/")
    # Check that the plot is saved correctly (manually or by verifying the directory)
