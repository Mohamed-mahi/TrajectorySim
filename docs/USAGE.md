# **Usage Instructions for TrajectorySim**

This guide explains how to configure and use the **TrajectorySim** program to simulate atomic motion on a Potential Energy Surface (PES), generate visualizations, and analyze results.

---

## **1. Setup Instructions**

### Prerequisites

Ensure you have:
- **Python 3.8 or higher**
- Required libraries listed in `requirements.txt`:
  ```bash
  numpy==1.23.5
  matplotlib==3.7.1
  pytest==7.4.0

## **Installation**

Follow these steps to install and set up the program:

### **1. Clone the Repository**

Start by cloning the repository and navigating to the project directory:
```bash
git clone <repository-url>
cd TrajectorySim

### **2. Install Dependencies**
Install the required Python libraries using the requirements.txt file:

pip install -r requirements.txt

### **3. Verify the Installation**
To ensure the setup is complete, run the following command to check the program's main script:

python main.py --help
If the above command runs successfully, the program is ready to use.

### **4. Optional: Run Tests**
Run the tests to verify all components are functioning correctly:

pytest tests/

his step ensures that the PES, force calculations, and trajectory simulations are working as expected.



## **2. Configuration**

To customize the simulation, edit the configuration file located at `config/simulation_config.py`.

### **Key Parameters**

#### **PES Parameters**
These parameters control the **Potential Energy Surface (PES)**:
- `C0_min`, `C1_min`, `C2_min`: Minimum coefficients for the PES.
- `C0_max`, `C1_max`, `C2_max`: Maximum coefficients for the PES.
- `lattice_constant`: Defines the lattice constant of the surface.

Example:
```python
PES_PARAMETERS = {
    "C0_min": 1.63093e6,
    "C1_min": 3.347616,
    "C2_min": 8184.7,
    "C0_max": 2.75075e6,
    "C1_max": 3.349208,
    "C2_max": 8258.11,
    "lattice_constant": 2.462,
}

### **Simulation Parameters**
These parameters control the simulation behavior:

dt: Time step (s).
gamma: Damping coefficient.
temp: Temperature (meV).
mass: Mass of the particle.
nsteps: Number of simulation steps.
num_particles: Number of particles to simulate.
Example:

SIMULATION_PARAMETERS = {
    "dt": 0.01,
    "gamma": 1.0,
    "temp": 0.02,
    "mass": 1.0,
    "nsteps": 10000,
    "num_particles": 1,
    "initial_variance": 0.1,
}
## **3. Running the Simulation**
Run the program using the following command:

python main.py
If the configuration is correct, the simulation will execute and generate plots in the plots/ directory.

## **4. Outputs**
The simulation generates multiple outputs, which are saved in the plots/ directory:

### **Generated Plots**
#### **PES Plot:**

Location: plots/1_pes/pes_plot.png
Description: Visualizes the potential energy surface.
#### **Force Components:**

**Location**: plots/2_forces_components/
force_x.png
force_y.png
force_z.png
**Description**: Contour plots of force components across the surface.
#### **Interaction Energy:**

**Location**: plots/3_interaction_energy/
interaction_energy_y_axis.png
interaction_energy_stacking.png
**Description**: Energy curves as a function of position and stacking.
#### **Trajectories:**

**Location**: plots/trajectory_output/trajectory_simulation.png
**Description**: Particle trajectories overlaid on the PES colormap.

## **5. Example Workflow**
Follow these steps to simulate and analyze atomic motion:

### **Step 1: Modify Configuration**
Edit config/simulation_config.py to set the desired parameters for the PES and simulation.

### **Step 2: Run the Simulation**
Run the program:

python main.py
### **Step 3: View Results**
Open the generated plots in the plots/ directory to visualize:

The energy landscape (PES).
Forces, interaction energies, and particle trajectories.

## **6. Troubleshooting**
### **Common Issues**
**1. Missing Dependencies**
If dependencies are missing, reinstall them using:

pip install -r requirements.txt
**2. Slow Simulations**
If the simulation is slow:

Reduce nsteps in the SIMULATION_PARAMETERS section.
Lower the grid resolution in the GRID_PARAMETERS section.
Example:

GRID_PARAMETERS = {
    "x_min": 0,
    "x_max": 2 * 2.462,  # Covers two lattice constants
    "y_min": 0,
    "y_max": 2 * 2.462,
    "resolution": 50  # Reduce resolution for faster computations
}

## **7. Testing**
To ensure the program is functioning correctly, run the included tests:

pytest tests/
These tests validate:

Correct PES calculations.
Accurate force computations.
Proper trajectory simulations.