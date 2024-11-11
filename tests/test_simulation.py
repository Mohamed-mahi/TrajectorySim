import pytest
from src.pes import PES
from src.simulation import simulate_particle

def test_simulate_particle():
    pes = PES(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 2.462)
    traj_x, traj_y, traj_z, traj_e = simulate_particle(
        particle_id=0,
        nsteps=10,
        dt=0.01,
        gamma=1.0,
        temp=0.02,
        mass=1.0,
        initial_variance=0.0,
        pes=pes
    )
    assert len(traj_x) == 11
    assert len(traj_y) == 11
    assert len(traj_z) == 11
    assert len(traj_e) == 11
