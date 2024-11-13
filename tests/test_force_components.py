import pytest
import numpy as np
from src.force_components import plot_forces

def test_plot_forces():
    X, Y = np.meshgrid(np.linspace(0, 2, 10), np.linspace(0, 2, 10))
    forces_x = np.random.rand(10, 10)
    forces_y = np.random.rand(10, 10)
    forces_z = np.random.rand(10, 10)
    
    try:
        plot_forces(X, Y, forces_x, forces_y, forces_z)
    except Exception as e:
        pytest.fail(f"Plotting force components failed: {e}")
