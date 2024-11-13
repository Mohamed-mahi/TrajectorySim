from src.trajectory_simulation import trajectories_with_potential
from src.pes import PES

def test_trajectory_simulation():
    pes = PES(1.63093e6, 3.347616, 8184.7, 2.75075e6, 3.349208, 8258.11, 2.462)

    # Simulation parameters
    dt = 0.01
    gamma = 1.0
    temp = 0.02
    mass = 1.0
    nsteps = 100
    num_particles = 1
    initial_variance = 0.1

    # Call the simulation function
    trajectories_with_potential(pes, dt, gamma, temp, mass, nsteps, num_particles, initial_variance, save_dir="test_plots/trajectory_output/")
    # Check that the plot is saved correctly (manually or by verifying the directory)
