# -*- coding: utf-8 -*-

from numpy import tan, abs as np_abs, degrees, radians
from numpy import arcsin, exp, sqrt, pi
from ....Functions.Geometry.inter_line_circle import inter_line_circle
from ....Functions.Geometry.inter_line_line import inter_line_line


def get_H2(self):
    """Return H2 in [m]

    Parameters
    ----------
    self : SlotW31B
        A SlotW31B object

    Returns
    -------
    H2: float
        H2 in [m]

    """

    if not (self.H2_is_rad):
        return self.H2

    Rbo = self.get_Rbo()
    Ryoke = self.get_Ryoke()
    L = Rbo + Ryoke

    s_angle = 2 * pi / self.Zs

    # l3 is the back width line
    Z1l3 = 0 - self.W2 / 2 * 1j
    Z2l3 = Ryoke - self.W2 / 2 * 1j

    # ls is the segment line
    Z1ls = 0 + 0j
    Z2ls = L * exp(-1j * s_angle / 2)
    perp_vec_tooth = (Z2ls - Z1ls) * 1j / np_abs(Z2ls - Z1ls)

    # l1 is the tooth line
    Z1l1 = Z1ls + (self.W1 / 2) * perp_vec_tooth
    Z2l1 = Z2ls + (self.W1 / 2) * perp_vec_tooth

    if self.is_outwards():
        # inner-runner
        angle_back = 3 * pi / 2 + (pi / 2 - self.H2 - s_angle / 2)

        Z5 = next(
            (
                Z
                for Z in inter_line_circle(Z1l3, Z2l3, Ryoke - self.H3, 0 + 0j)
                if Z.real > 0
            ),
            None,
        )

        # l4 is the back angle line
        Z1l4 = Z5
        Z2l4 = Z5 + L * exp(1j * angle_back)
        Z4 = inter_line_line(Z1l1, Z2l1, Z1l4, Z2l4)[0]

        return Z5.real - Z4.real

    else:
        # outer-runner
        angle_back = 3 * pi / 2 + (-pi / 2 + self.H2 - s_angle / 2)

        Z5 = next(
            (
                Z
                for Z in inter_line_circle(Z1l3, Z2l3, Ryoke + self.H3, 0 + 0j)
                if Z.real > 0
            ),
            None,
        )

        # l4 is the back angle line
        Z1l4 = Z5
        Z2l4 = Z5 + L * exp(1j * angle_back)
        Z4 = inter_line_line(Z1l1, Z2l1, Z1l4, Z2l4)[0]

        return Z4.real - Z5.real
