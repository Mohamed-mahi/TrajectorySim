TrajectorySim: Potential Energy Surface and Diffusion Simulation
TrajectorySim is a Python-based simulation program designed to model the behavior of atoms diffusing on a Potential Energy Surface (PES). The program calculates energy and forces, evaluates interaction energy, and simulates atomic trajectories using the velocity Verlet algorithm and Langevin equation.

Overview
Simulating atomic diffusion on surfaces can be computationally expensive due to the long timescales involved. Atoms typically remain in stable positions (PES minima) and occasionally jump to neighboring sites, overcoming potential barriers.

To accelerate this process, TrajectorySim applies random lateral forces that lower the energy barriers, enabling faster transitions while maintaining realistic dynamics.

Key Features
PES Calculation:

Computes the potential energy landscape for an atom on a surface.
Includes periodic contributions from the lattice geometry.
Force Computation:

Derives force components (Fx,Fy,Fz) from the PES gradients.

from the PES gradients.
Interaction Energy:

Evaluates energy as a function of atomic separation or stacking configuration.
Trajectory Simulation:

Simulates atomic motion using the velocity Verlet algorithm and Langevin equation.
Adds thermal noise and friction for realistic dynamics.
Visualization:

Generates plots for:
PES.
Force components.
Interaction energy.
Atomic trajectories overlaid on the PES.


Installation
Clone the repository:

git clone <repository-url>
cd TrajectorySim
Install dependencies:

pip install -r requirements.txt

Usage
For detailed usage instructions, including configuration, running simulations, and interpreting results, see USAGE.md.

Code Structure
Main Components
PES Class: Models the PES and computes energy and forces.
Plotting Functions:
plot_force_components: Generates contour plots of force components.
plot_interaction_energy_y_axis and plot_interaction_energy_stacking: Visualize interaction energy.
Trajectory Simulation:
Uses the velocity Verlet algorithm and Langevin equation to simulate atomic motion.
Key Equations
Potential Energy Surface (PES):
Forces:
Langevin Equation for Trajectories:

Results
PES Visualization: 
Force Components:
Interaction Energy:
Trajectories:

Testing
Run the included tests to verify the implementation:

pytest tests/

References
Reguzzoni, M., et al. (2012). Potential energy surface for graphene on graphene: Ab initio derivation, analytical description, and microscopic interpretation. Physical Review B, 86, 245434.

License
This project is licensed under the MIT License.