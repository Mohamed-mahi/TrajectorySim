import yaml
from pes import PES
from simulation import trajectories_with_potential

if __name__ == "__main__":
    # Load configuration
    with open("config/default_config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Debug: Print loaded configuration
    print("Loaded Configuration:")
    print(config)

    sim_params = config["simulation"]
    pes_params = config["pes"]

    # Initialize PES
    pes = PES(
        float(pes_params["C0_min"]), float(pes_params["C1_min"]), float(pes_params["C2_min"]),
        float(pes_params["C0_max"]), float(pes_params["C1_max"]), float(pes_params["C2_max"]),
        float(pes_params["lattice_constant"])
    )

    # Run simulation
    trajectories_with_potential(
        pes,
        float(sim_params["dt"]),
        float(sim_params["gamma"]),
        float(sim_params["temp"]),
        float(sim_params["mass"]),
        int(sim_params["nsteps"]),
        int(sim_params["num_particles"]),
        0.0  # Initial variance
    )
