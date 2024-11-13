# PES parameters
PES_PARAMETERS = {
    "C0_min": 1.63093e6,
    "C1_min": 3.347616,
    "C2_min": 8184.7,
    "C0_max": 2.75075e6,
    "C1_max": 3.349208,
    "C2_max": 8258.11,
    "lattice_constant": 2.462,
}

# Simulation parameters
SIMULATION_PARAMETERS = {
    "dt": 0.01,               # Time step (s)
    "gamma": 1.0,             # Damping coefficient (s^-1)
    "temp": 0.02,             # Temperature (meV)
    "mass": 1.0,              # Mass of the particle in amu
    "nsteps": 10000,          # Number of steps
    "num_particles": 1,       # Number of particles
    "initial_variance": 0.1,  # Variance for random noise
}

# Plotting parameters
GRID_PARAMETERS = {
    "x_min": 0,
    "x_max": 2 * 2.462,  # 2 * lattice_constant
    "y_min": 0,
    "y_max": 2 * 2.462,
    "resolution": 100
}
