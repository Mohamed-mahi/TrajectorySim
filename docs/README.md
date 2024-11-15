# **TrajectorySim: Potential Energy Surface and Diffusion Simulation**

**TrajectorySim** is a Python-based simulation program designed to model the behavior of atoms diffusing on a **Potential Energy Surface (PES)**. The program calculates energy and forces, evaluates interaction energy, and simulates atomic trajectories using the **velocity Verlet algorithm** and **Langevin equation**.

---

## **Overview**

Simulating atomic diffusion on surfaces can be computationally expensive due to the long timescales involved. Atoms typically remain in stable positions (PES minima) and occasionally jump to neighboring sites, overcoming potential barriers.

To accelerate this process, **TrajectorySim** applies random lateral forces that lower the energy barriers, enabling faster transitions while maintaining realistic dynamics.


---

## **Theoretical Background**

### **1. Potential Energy Surface (PES)**

The **Potential Energy Surface (PES)** describes the energy landscape that an atom "feels" as it interacts with a surface. It includes periodic energy variations from the lattice structure and vertical interactions (repulsion and attraction).

![](images/pes%20v%20x,y,z%20-%20Copy.png)

![](images/pes%20where.png)


### **2. Langevin Dynamics**

The motion of the atom is influenced by:
1. **Deterministic Forces:** Derived from the PES gradients.
2. **Random Forces (Thermal Noise):** Represented as random fluctuations to mimic thermal effects.
3. **Friction:** Damps the motion to ensure realistic behavior.

These effects are modeled using the **Langevin Equation** to simulate realistic atomic motion:

![](images/langevin%20eq2.png)
![](images/langevin%20eq2_where.png)


### **4. Diffusion on a PES**

Atoms on a Potential Energy Surface (PES) tend to stay in low-energy regions, such as hollow sites, where they are most stable. For an atom to move to a neighboring site, it must overcome an energy barrier. This natural diffusion process is typically slow because:

* The atom spends most of its time vibrating within the energy minima. 
* Transitions to neighboring sites occur infrequently, as they require significant thermal activation. 

To accelerate diffusion, this project introduces lateral forces, which effectively lower the energy barriers, making transitions more frequent. The reduced energy barrier is described by the equation:

![](images/reduced_energy_barrier.png)
![](images/reduced_where.png)
This formulation ensures that lateral forces assist atomic transitions by lowering the energy barriers, facilitating faster diffusion.
### **3. Velocity Verlet Algorithm**
To compute the atom's motion, the **Velocity Verlet algorithm** is used for integration. This method updates the atom's position, velocity, and acceleration iteratively, through these steps:

![](images/velocity_verlet_alg.png)

Here, \(r(t)\) and \(v(t)\) are the particle's position and velocity at time \(t\), \(F(t)\) is the force acting on the particle at time \(t\), \(m\) is the particle’s mass, \(Delta t\) is the time step, and \(v(t')\) is the intermediate velocity after the first update.


### **5. Applications**

This simulation is useful for:
- Understanding atomic diffusion on surfaces like graphene.
- Exploring the effects of thermal noise and external forces on atomic motion.
- Validating potential energy models derived from experimental or ab initio data.


---

## **Computational Key Features for Better Understanding of the program:**

- **PES Calculation:** 

   It computes the potential energy landscape for an atom on a surface.It also includes periodic contributions from the lattice geometry.
- **Force Computation:** 

  Derives force components \(Fx, Fy, Fz) from the PES gradients.
- **Interaction Energy:** 

  Evaluates energy as a function of atomic separation or stacking configuration.
- **Trajectory Simulation:** 

  Simulates atomic motion using the velocity Verlet algorithm and **Langevin equation**.
  
  Adds thermal noise and friction for realistic dynamics.
- **Visualization:** 
  Generates plots for:
* PES. 
* Force components. 
* Interaction energy. 
* Atomic trajectories overlaid on the PES. 

**To show some examples of the generated results:**
![](images/force_z.png)
![PES plot:](images/pes_plot.png)
![](images/trajectory_simulation.png)

---
## **Installation**

1. Clone the repository:

   ```bash
   
   git clone https://github.com/Mohamed-mahi/TrajectorySim.git
   cd TrajectorySim

2. Install Dependencies

   Install required libraries using ```requirements.txt```:

   ```bash 
   pip install -r requirements.txt
   ```
  
3. Verify the Installation
   Check that the program is ready by running:

   ```python    
   python main.py --help 
   ```