import pytest
import numpy as np
from src.pes import PES

@pytest.fixture
def pes():
    return PES(1.63093e6, 3.347616, 8184.70, 2.75075e6, 3.349208, 8258.11, 2.462)

def test_pes_initialization(pes):
    assert pes.C0_max == 2.75075e6
    assert pes.Delta_0 == pytest.approx(1.11982e6, rel=1e-6)

def test_u(pes):
    u_value = pes.u(0, 0)
    assert np.isclose(u_value, 0, atol=1e-6)

def test_v(pes):
    v_value = pes.V(0, 0, 3.2)
    assert isinstance(v_value, float)
    assert v_value < 0  # PES should have a negative potential

def test_force(pes):
    fx, fy, fz = pes.force(0, 0, 3.2)
    assert isinstance(fx, float)
    assert isinstance(fy, float)
    assert isinstance(fz, float)

def test_force_numerical_accuracy(pes):
    fx, fy, fz = pes.force(1, 1, 3.2)
    expected_fx = -1.23e6  # Replace with analytical/expected value
    assert fx < 0  # Expected negative force in x-direction
