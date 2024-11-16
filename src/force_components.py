import os
import matplotlib.pyplot as plt

def plot_force_components(X, Y, forces_x, forces_y, forces_z, save_dir="plots/2_forces_components/"):
    os.makedirs(save_dir, exist_ok=True)

    # X-component
    plt.figure()
    plt.contourf(X, Y, forces_x, cmap="jet")
    plt.colorbar(label="Force X")
    plt.title("Force X Component")
    plt.savefig(f"{save_dir}/force_x.png")
    if not os.getenv("PYTEST_RUNNING"):  # Skip plt.show() during tests
        plt.show() # pragma: no cover
    plt.close()

    # Y-component
    plt.figure()
    plt.contourf(X, Y, forces_y, cmap="jet")
    plt.colorbar(label="Force Y")
    plt.title("Force Y Component")
    plt.savefig(f"{save_dir}/force_y.png")
    if not os.getenv("PYTEST_RUNNING"): # Skip plt.show() during tests
        plt.show()  # pragma: no cover 
    plt.close()

    # Z-component
    plt.figure()
    plt.contourf(X, Y, forces_z, cmap="jet")
    plt.colorbar(label="Force Z")
    plt.title("Force Z Component")
    plt.savefig(f"{save_dir}/force_z.png")
    if not os.getenv("PYTEST_RUNNING"):  # Skip plt.show() during tests
        plt.show()  # pragma: no cover
    plt.close()
