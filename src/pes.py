import numpy as np

class PES:
    def __init__(self, C0_min, C1_min, C2_min, C0_max, C1_max, C2_max, lattice_constant):
        self.Delta_0 = C0_max - C0_min
        self.Delta_1 = C1_max - C1_min
        self.Delta_2 = C2_max - C2_min
        self.C0_max = C0_max
        self.C1_max = C1_max
        self.C2_max = C2_max
        self.lattice_constant = lattice_constant

    def u(self, x, y):
        theta_x = 2. * np.pi * x / self.lattice_constant
        theta_y = 2. * np.pi * y / (self.lattice_constant * np.sqrt(3.))
        return 2. * (3. - 2. * np.cos(theta_x) * np.cos(theta_y) - np.cos(2. * theta_y)) / 9.

    def V(self, x, y, z):
        u_ = self.u(x, y)
        C0 = self.C0_max - self.Delta_0 * u_
        C1 = self.C1_max - self.Delta_1 * u_
        C2 = self.C2_max - self.Delta_2 * u_
        return C0 * np.exp(-z * C1) - C2 / (z**4)

    def force(self, x, y, z, h=1.e-6):
        dV_dx = (self.V(x + h, y, z) - self.V(x - h, y, z)) / (2. * h)
        dV_dy = (self.V(x, y + h, z) - self.V(x, y - h, z)) / (2. * h)
        dV_dz = (self.V(x, y, z + h) - self.V(x, y, z - h)) / (2. * h)
        return -dV_dx, -dV_dy, -dV_dz
