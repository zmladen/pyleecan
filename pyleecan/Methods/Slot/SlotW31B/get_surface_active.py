from ....Classes.SurfLine import SurfLine
from ....Functions.labels import WIND_LAB, DRAW_PROP_LAB


def get_surface_active(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotW31B
        A SlotW31B object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_wind: Surface
        Surface corresponding to the Winding Area
    """
    # Create curve list
    line_dict = self._comp_line_dict()

    curve_list = [
        line_dict["11-12"],
        line_dict["12-13"],
        line_dict["13-14"],
        line_dict["14-15"],
        line_dict["15-16"],
        line_dict["16-17"],
        line_dict["17-18"],
        line_dict["18-11"],
    ]

    curve_list = [line for line in curve_list if line is not None]

    # Only the closing arc (6-3) needs to be drawn (in FEMM)
    for curve in curve_list[:-1]:
        if curve.prop_dict is None:
            curve.prop_dict = dict()
        curve.prop_dict.update({DRAW_PROP_LAB: False})

    # Create surface
    if self.is_outwards():
        Zmid = self.get_Rbo() + self.H0 + self.get_H1() + self.H2 / 2
    else:
        Zmid = self.get_Rbo() - self.H0 - self.get_H1() - self.H2 / 2
    label = self.parent.get_label() + "_" + WIND_LAB + "_R0-T0-S0"
    surface = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
