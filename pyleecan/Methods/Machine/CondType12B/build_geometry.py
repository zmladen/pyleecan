# -*- coding: utf-8 -*-

from numpy import linspace
from ....Classes.Circle import Circle


def build_geometry(self, alpha=0, delta=0):
    """Builds the geometry conductors.

    Parameters
    ----------
    self : Surface
        A Surface object
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : Complex
        complex for translation (Default value = 0)

    Returns
    -------
    surf_list:
        List of surfaces each representing single wire

    """

    surf_list = list()

    for center in self.comp_wire_centers():
        c = Circle(center=complex(*center), radius=self.Wwire / 2)
        surf_list.append(c)

    # Apply transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
