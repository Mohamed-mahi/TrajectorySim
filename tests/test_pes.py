import pytest
import numpy as np
from src.pes import PES

@pytest.fixture
def pes():
    return PES(1.63093e6, 3.347616, 8184.7, 2.75075e6, 3.349208, 8258.11, 2.462)

def test_pes_initialization(pes):
    assert pes.C0_max == 2.75075e6
    assert pes.Delta_0 == pytest.approx(1.11982e6, rel=1e-6)

def test_u(pes):
    u_value = pes.u(0, 0)
    assert np.isclose(u_value, 0, atol=1e-6)

def test_v(pes):
    v_value = pes.V(0, 0, 3.2)
    assert isinstance(v_value, float)
    assert v_value < 0  # PES should return a negative potential at the tested point

def test_force(pes):
    fx, fy, fz = pes.force(0, 0, 3.2)
    assert isinstance(fx, float)
    assert isinstance(fy, float)
    assert isinstance(fz, float)

def test_force_accuracy(pes):
    fx, fy, fz = pes.force(1.0, 1.0, 3.2)
    expected_fx = 1.473065275092722  # Replace with the known expected value
    assert np.isclose(fx, expected_fx, atol=1e-3), f"Unexpected force value: {fx}"
