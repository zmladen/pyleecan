# -*- coding: utf-8 -*-

from numpy import abs as np_abs, degrees
from numpy import arcsin, exp, pi
from ....Functions.Geometry.inter_line_line import inter_line_line


def get_H1(self):
    """Return H1 in [m]

    Parameters
    ----------
    self : SlotW31B
        A SlotW31B object

    Returns
    -------
    H1: float
        H1 in [m]

    """

    if not (self.H1_is_rad):
        return self.H1

    Rbo = self.get_Rbo()
    Ryoke = self.get_Ryoke()
    L = Rbo + Ryoke

    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(-1j * alpha)
    s_angle = 2 * pi / self.Zs

    # ls is the segment line
    Z1ls = 0 + 0j
    Z2ls = L * exp(-1j * s_angle / 2)
    perp_vec_tooth = (Z2ls - Z1ls) * 1j / np_abs(Z2ls - Z1ls)

    # l1 is the tooth line
    Z1l1 = Z1ls + (self.W1 / 2) * perp_vec_tooth
    Z2l1 = Z2ls + (self.W1 / 2) * perp_vec_tooth

    Z2 = Z1 + self.H0

    if self.is_outwards():
        # inner-runner
        angle_tip = 3 * pi / 2 + (-pi / 2 + self.H1 - s_angle / 2)

        # l2 is the tip line
        Z1l2 = Z2
        Z2l2 = Z2 + L * exp(1j * angle_tip)
        Z3 = inter_line_line(Z1l1, Z2l1, Z1l2, Z2l2)[0]

        # Can be positive and negative, depending on the angle...
        return Z3.real - Z2.real

    else:
        # outer-runner
        angle_tip = 3 * pi / 2 + (pi / 2 - self.H1 - s_angle / 2)

        # l2 is the tip line
        Z1l2 = Z2
        Z2l2 = Z2 + L * exp(1j * angle_tip)
        Z3 = inter_line_line(Z1l1, Z2l1, Z1l2, Z2l2)[0]

        return Z2.real - Z3.real
