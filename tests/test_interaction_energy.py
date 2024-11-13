import pytest
import numpy as np
from src.interaction_energy import plot_interaction_energy
from src.pes import PES

@pytest.fixture
def pes():
    return PES(1.63093e6, 3.347616, 8184.70, 2.75075e6, 3.349208, 8258.11, 2.462)

def test_interaction_energy_plot(pes):
    z_values = [3.0, 3.2, 3.6]
    y_range = np.linspace(0, 10, 100)

    try:
        plot_interaction_energy(pes, z_values, y_range)
    except Exception as e:
        pytest.fail(f"Interaction energy plotting failed: {e}")
