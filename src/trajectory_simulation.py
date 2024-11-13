import os
import numpy as np
import matplotlib.pyplot as plt


def force(x, y, z, pes):
    """Calculate force components and potential energy at (x, y, z)."""
    fx, fy, fz = pes.force(x, y, z)
    energy = pes.V(x, y, z)
    return energy, fx, fy, fz


def simulate_particle(particle_id, nsteps, dt, gamma, temp, mass, initial_variance, pes):
    """Simulate particle motion using velocity Verlet integration."""
    hdt = 0.5 * dt
    varg = np.sqrt(2. * gamma * temp * hdt / mass)
    random = np.random.default_rng()

    # Initial conditions
    xt, yt, zt = 0.0, 0.0, 3.2  # Start at z = 3.2
    vxt, vyt, vzt = 0.0, 0.0, 0.0

    # Calculate initial forces and potential energy
    energy, forcex, forcey, forcez = force(xt, yt, zt, pes)

    # Store trajectory
    traj_x, traj_y, traj_z = [xt], [yt], [zt]

    for _ in range(nsteps):
        # Update velocities (first half step)
        vxt += random.normal(0., varg) - gamma * hdt * vxt + hdt * forcex / mass
        vyt += random.normal(0., varg) - gamma * hdt * vyt + hdt * forcey / mass
        vzt += random.normal(0., varg) - gamma * hdt * vzt + hdt * forcez / mass

        # Update positions
        xt += dt * vxt
        yt += dt * vyt
        zt += dt * vzt

        # Update forces and potential energy
        energy, forcex, forcey, forcez = force(xt, yt, zt, pes)

        # Update velocities (second half step)
        vxt += random.normal(0., varg) - gamma * hdt * vxt + hdt * forcex / mass
        vyt += random.normal(0., varg) - gamma * hdt * vyt + hdt * forcey / mass
        vzt += random.normal(0., varg) - gamma * hdt * vzt + hdt * forcez / mass

        # Append to trajectory
        traj_x.append(xt)
        traj_y.append(yt)
        traj_z.append(zt)

    return traj_x, traj_y, traj_z


def trajectories_with_potential(pes, dt, gamma, temp, mass, nsteps, num_particles, initial_variance, save_dir="plots/trajectory_output/"):
    """Simulate particle trajectories and plot with the potential colormap."""
    os.makedirs(save_dir, exist_ok=True)

    # Generate grid for potential colormap
    x_vals = np.linspace(-10, 10, 100)
    y_vals = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = np.array([[force(x, y, 3.2, pes)[0] for x in x_vals] for y in y_vals])

    # Plot potential colormap
    fig, ax = plt.subplots(figsize=(8, 8))
    cmap = ax.contourf(X, Y, Z, cmap='viridis', alpha=0.6)
    fig.colorbar(cmap, label="Potential Energy")

    # Plot particle trajectories
    for i in range(num_particles):
        traj_x, traj_y, traj_z = simulate_particle(i, nsteps, dt, gamma, temp, mass, initial_variance, pes)
        ax.plot(traj_x, traj_y, linestyle='--', marker='o', markersize=1, alpha=0.4, label=f'Particle {i + 1}')

          
        # Start point
        ax.scatter(traj_x[0], traj_y[0], c='blue', marker='o', s=70, label='Start point')  # Increased size
        # End point
        ax.scatter(traj_x[-1], traj_y[-1], c='red', marker='o', s=70, label='End point')  # Increased size

    # Final plot touches
    ax.set_xlabel('x (Å)')
    ax.set_ylabel('y (Å)')
    ax.set_title('2D Trajectories with Potential Colormap')
    ax.grid(True)
    ax.legend(loc='upper right', fontsize='small')

    # Save and show the plot
    plot_path = os.path.join(save_dir, "trajectory_simulation.png")
    plt.savefig(plot_path)
    plt.show()
    plt.close()
