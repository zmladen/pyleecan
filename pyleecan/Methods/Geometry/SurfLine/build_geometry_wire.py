# -*- coding: utf-8 -*-

from numpy import linspace
from ....Classes.Circle import Circle
from ....Methods.Geometry.SurfLine import *


def build_geometry_wire(self, conductor=None, alpha=0, delta=0):
    """Builds the geometry surfaces for wires.For that build_geometry_active method must be provided

    Parameters
    ----------
    self : Surface
        A Surface object
    Wins_cond : int.
        Width of conductor insulation
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : Complex
        complex for translation (Default value = 0)

    Returns
    -------
    surf_list:
        List of surface delimiting the active zone

    """
    if not conductor:
        raise CondMissingError(
            "Please provide conductor object to build wire geometry."
        )

    surf_list = list()

    for center in self.comp_conductor_centers(conductor.comp_width()):
        wire_surf_list = conductor.build_geometry(delta=center)
        surf_list.extend(wire_surf_list)

    # Apply transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
