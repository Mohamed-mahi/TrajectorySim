# **Usage Instructions** 
This guide explains how to configure, run, and analyze the results of the **TrajectorySim** simulation program.

## **1. Configuration**

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
```
### **Source of Parameters**

The numerical values of `C0_min`, `C1_min`, `C2_min`, `C0_max`, `C1_max`, `C2_max` are derived from **Table II** in the reference:

**"Potential energy surface for graphene on graphene: Ab initio derivation, analytical description, and microscopic interpretation"**  
M. Reguzzoni, A. Fasolino, E. Molinari, and M. C. Righi  

**DOI:** [10.1103/PhysRevB.86.245434](https://doi.org/10.1103/PhysRevB.86.245434)

These parameters describe the interaction energy between two graphene layers for **AA** and **AB** stacking configurations. They are crucial for accurately modeling the PES and simulating atomic motion.



## 2. Running the Simulation
Run the program using the following command:

```python main.py```

If the configuration is correct, the simulation will execute and generate plots in the ```plots/``` directory.

## 3. Outputs
The simulation generates multiple outputs, which are saved in the ```plots/``` directory:

### Generated Plots
 #### PES Plot:
* ****Location****: ```plots/1_pes/pes_plot.png```
* **Description**: Visualizes the potential energy surface.

#### Force Components:
****Location****: ```plots/2_forces_components/```
* ```force_x.png``` Force in the x-direction.
* ```force_y.png``` Force in the y-direction. 
* ```force_z.png``` Force in the z-direction.
* **Description**: Contour plots of force components across the surface.

#### Interaction Energy:
**Location**: ```plots/3_interaction_energy/```
```interaction_energy_y_axis.png```  
```interaction_energy_stacking.png```
* **Description**: Energy curves as a function of position and stacking.

#### Trajectories:
**Location**: ```plots/trajectory_output/trajectory_simulation.png```
* **Description**: Particle trajectories overlaid on the PES colormap.

## 4. Example Workflow
Follow these steps to simulate and analyze atomic motion:

#### Step 1: Modify Configuration
Edit ```config/simulation_config.py``` to set the desired parameters for the PES and simulation.

#### Step 2: Run the Simulation
Run the program:
```python main.py```
#### Step 3: View Results
Open the generated plots in the ```plots/``` directory to visualize the results.

## 5. Troubleshooting
#### 5.1 Missing Dependencies
If required libraries are missing, reinstall them using:

```pip install -r requirements.txt```


### **5.2 Slow Simulations**

If the simulation runs slowly:

- Reduce the number of steps (`nsteps`) in the `SIMULATION_PARAMETERS` section.  
- Lower the grid resolution in the `GRID_PARAMETERS` section to reduce computational load.

## 6. Testing
To ensure that the program works correctly, run the test suite:

``` pytest tests/```

What the Tests Validate:
* Correct PES calculations. 
* Accurate force computations.
* Proper trajectory simulations.

 Running the tests will confirm that all components of the program are functioning as expected.


