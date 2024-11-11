import numpy as np
import matplotlib.pyplot as plt

def force(x, y, z, pes):
    fx, fy, fz = pes.force(x, y, z)
    energy = pes.V(x, y, z)
    return energy, fx, fy, fz

def simulate_particle(particle_id, nsteps, dt, gamma, temp, mass, initial_variance, pes):
    hdt = 0.5 * dt
    varg = np.sqrt(2. * gamma * temp * hdt / mass)
    random = np.random.default_rng()

    xt, yt, zt = 0.0, 0.0, 3.2
    vxt, vyt, vzt = 0.0, 0.0, 0.0

    energy, forcex, forcey, forcez = force(xt, yt, zt, pes)

    traj_x = [xt]
    traj_y = [yt]
    traj_z = [zt]
    traj_e = [energy]

    for k in range(nsteps):
        vxt += random.normal(0., varg) - gamma * hdt * vxt + hdt * forcex / mass
        vyt += random.normal(0., varg) - gamma * hdt * vyt + hdt * forcey / mass
        vzt += random.normal(0., varg) - gamma * hdt * vzt + hdt * forcez / mass

        xt += dt * vxt
        yt += dt * vyt
        zt += dt * vzt

        energy, forcex, forcey, forcez = force(xt, yt, zt, pes)

        vxt += random.normal(0., varg) - gamma * hdt * vxt + hdt * forcex / mass
        vyt += random.normal(0., varg) - gamma * hdt * vyt + hdt * forcey / mass
        vzt += random.normal(0., varg) - gamma * hdt * vzt + hdt * forcez / mass

        traj_x.append(xt)
        traj_y.append(yt)
        traj_z.append(zt)
        traj_e.append(energy)

    return traj_x, traj_y, traj_z, traj_e

def trajectories_with_potential(pes, dt, gamma, temp, mass, nsteps, num_particles, initial_variance):
    z_value = 3.2
    x_vals = np.linspace(-10, 10, 100)
    y_vals = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = np.array([[pes.V(x, y, z_value) for x in x_vals] for y in y_vals])

    fig, ax = plt.subplots(figsize=(6, 6))
    cmap = ax.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.7)
    fig.colorbar(cmap, ax=ax, label="Potential Energy (meV)")
    # Plot start and end points for particles
    ax.scatter(0, 0, c='blue', marker='o', s=50, label='Start point')  # Start point
    for i in range(num_particles):
        traj_x, traj_y, traj_z, traj_e = simulate_particle(i, nsteps, dt, gamma, temp, mass, initial_variance, pes)
        ax.plot(traj_x, traj_y, linestyle='--', marker='o', markersize=1, alpha=0.5)
        ax.scatter(traj_x[-1], traj_y[-1], c='red', marker='o', s=30) #label=f'End Point (Particle {i})')

    ax.set_xlabel('x (Å)')
    ax.set_ylabel('y (Å)')
    ax.set_title(f'2D Trajectories on PES at z={z_value} Å')
    ax.grid(True)
    plt.show()
