import pytest
from src.pes import PES

def test_pes_initialization():
    pes = PES(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 2.462)
    assert pes.Delta_0 == 3.0
    assert pes.Delta_1 == 3.0
    assert pes.Delta_2 == 3.0

def test_pes_potential():
    pes = PES(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 2.462)
    V = pes.V(0.0, 0.0, 3.2)
    assert V is not None
    assert isinstance(V, float)
