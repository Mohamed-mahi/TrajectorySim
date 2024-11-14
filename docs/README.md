# **TrajectorySim: Potential Energy Surface and Diffusion Simulation**

**TrajectorySim** is a Python-based simulation program designed to model the behavior of atoms diffusing on a **Potential Energy Surface (PES)**. The program calculates energy and forces, evaluates interaction energy, and simulates atomic trajectories using the **velocity Verlet algorithm** and **Langevin equation**.

---

## **Overview**

Simulating atomic diffusion on surfaces can be computationally expensive due to the long timescales involved. Atoms typically remain in stable positions (PES minima) and occasionally jump to neighboring sites, overcoming potential barriers.

To accelerate this process, **TrajectorySim** applies random lateral forces that lower the energy barriers, enabling faster transitions while maintaining realistic dynamics.

---

## **Key Features**

- **PES Calculation:** 
  - Computes the potential energy landscape for an atom on a surface.
  - Includes periodic contributions from the lattice geometry.
- **Force Computation:** 
  - Derives force components \((F_x, F_y, F_z)\) from the PES gradients.
- **Interaction Energy:** 
  - Evaluates energy as a function of atomic separation or stacking configuration.
- **Trajectory Simulation:** 
  - Simulates atomic motion using the **velocity Verlet algorithm** and **Langevin equation**.
  - Adds thermal noise and friction for realistic dynamics.
- **Visualization:** 
  - Generates plots for:
    - PES.
    - Force components.
    - Interaction energy.
    - Atomic trajectories overlaid on the PES.

---

## **Theoretical Background**

### **1. Potential Energy Surface (PES)**

The **Potential Energy Surface (PES)** describes the energy landscape that an atom "feels" as it interacts with a surface. It includes periodic energy variations from the lattice structure and vertical interactions (repulsion and attraction).

\[
V(x, y, z) = C_0(x, y)e^{-zC_1(x, y)} - \frac{C_2(x, y)}{z^4}
\]

Where:
- \( C_i(x, y) = C_{i,\text{max}} - \Delta_i U(x, y) \)
- \( U(x, y) = \frac{2}{9} \left[3 - 2 \cos(\theta_x) \cos(\theta_y) - \cos(2\theta_y)\right] \)

### **2. Langevin Dynamics**

To simulate realistic atomic motion:
\[
m \frac{d^2 \vec{r}}{dt^2} = -\nabla V(\vec{r}) - \gamma m \frac{d \vec{r}}{dt} + \vec{\eta}(t)
\]
Where:
- \( \nabla V(\vec{r}) \): PES forces.
- \( \gamma \): Friction coefficient.
- \( \vec{\eta}(t) \): Random noise representing thermal effects.

### **3. Velocity Verlet Algorithm**

The velocity Verlet algorithm integrates motion iteratively:
1. Update position:
   \[
   \vec{r}(t + \Delta t) = \vec{r}(t) + \vec{v}(t)\Delta t + \frac{1}{2}\vec{a}(t)(\Delta t)^2
   \]
2. Compute new acceleration from forces:
   \[
   \vec{a}(t + \Delta t) = \frac{\vec{F}(t + \Delta t)}{m}
   \]
3. Update velocity:
   \[
   \vec{v}(t + \Delta t) = \vec{v}(t) + \frac{\vec{a}(t) + \vec{a}(t + \Delta t)}{2}\Delta t
   \]

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd TrajectorySim
