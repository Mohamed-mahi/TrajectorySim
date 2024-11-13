import pytest
from src.trajectory_simulation import simulate_trajectory
from src.pes import PES

@pytest.fixture
def pes():
    return PES(1.63093e6, 3.347616, 8184.70, 2.75075e6, 3.349208, 8258.11, 2.462)

def test_simulate_trajectory(pes):
    dt = 0.01
    gamma = 1.0
    temp = 0.02
    mass = 1.0
    nsteps = 10
    num_particles = 1

    trajectories = simulate_trajectory(pes, dt, gamma, temp, mass, nsteps, num_particles)
    
    assert len(trajectories) == num_particles
    for traj in trajectories:
        assert "x" in traj and "y" in traj and "z" in traj
        assert len(traj["x"]) == nsteps + 1  # Includes the initial position
