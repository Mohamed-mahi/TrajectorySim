import os
import matplotlib.pyplot as plt

def plot_force_components(X, Y, forces_x, forces_y, forces_z, save_dir="plots/2_forces_components/"):
    # Ensure the save directory exists
    os.makedirs(save_dir, exist_ok=True)

    for force, label in zip([forces_x, forces_y, forces_z], ["x", "y", "z"]):
        plt.contourf(X, Y, force.T, levels=64, cmap="jet")
        plt.colorbar(label=f"Force ({label}-component)")
        plt.title(f"{label.capitalize()}-Force Surface")
        plt.xlabel("X (Å)")
        plt.ylabel("Y (Å)")
        plt.savefig(f"{save_dir}/force_{label}.png")
        plt.show()  # Display the plot interactively
        plt.close()
