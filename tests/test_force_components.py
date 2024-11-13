import numpy as np
from src.force_components import plot_force_components

def test_plot_force_components():
    # Create mock data
    x = np.linspace(0, 1, 10)
    y = np.linspace(0, 1, 10)
    X, Y = np.meshgrid(x, y)
    forces_x = np.random.random(X.shape)
    forces_y = np.random.random(Y.shape)
    forces_z = np.random.random(X.shape)

    # Call the plotting function
    plot_force_components(X, Y, forces_x, forces_y, forces_z, save_dir="test_plots/force_components/")
    # Check that plots are saved correctly (manually or by verifying the directory exists)
