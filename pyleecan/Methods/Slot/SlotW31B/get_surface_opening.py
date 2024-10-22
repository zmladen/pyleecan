from ....Classes.SurfLine import SurfLine
from ....Functions.labels import SOP_LAB, DRAW_PROP_LAB
from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from numpy import abs as np_abs


def get_surface_opening(self, alpha=0, delta=0):
    """Return the list of surfaces defining the opening area of the Slot

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_list : list
        list of surfaces objects
    """

    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]
    Z9 = point_dict["Z9"]
    Z10 = point_dict["Z10"]

    Z11 = point_dict["Z11"]
    Z12 = point_dict["Z12"]
    Z13 = point_dict["Z13"]
    Z14 = point_dict["Z14"]
    Z15 = point_dict["Z15"]
    Z16 = point_dict["Z16"]
    Z17 = point_dict["Z17"]
    Z18 = point_dict["Z18"]

    Z15_ = point_dict["Z15*"]
    Z14_ = point_dict["Z14*"]
    Z18_ = point_dict["Z18*"]
    Z11_ = point_dict["Z11*"]

    # S1
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z9))
    curve_list.append(Segment(Z9, Z10))
    curve_list.append(Arc1(Z10, Z1, -np_abs(Z1), is_trigo_direction=False))
    Zmid = (Z1 + Z2 + Z9 + Z10) / 4
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S1"
    S1 = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # S2
    curve_list = list()
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z12))
    if abs(Z11 - Z18) > abs(Z11_ - Z18_):
        curve_list.append(Segment(Z12, Z11))
        curve_list.append(Segment(Z11, Z11_))
    else:
        curve_list.append(Segment(Z12, Z11_))

    curve_list.append(Segment(Z11_, Z18_))
    if abs(Z11 - Z18) > abs(Z11_ - Z18_):
        curve_list.append(Segment(Z18_, Z18))
        curve_list.append(Segment(Z18, Z17))
    else:
        curve_list.append(Segment(Z18_, Z17))
    curve_list.append(Segment(Z17, Z8))
    curve_list.append(Segment(Z8, Z9))
    curve_list.append(Segment(Z9, Z2))
    Zmid = (Z2 + Z3 + Z12 + Z11 + Z11_ + Z18_ + Z18 + Z17 + Z8 + Z9) / 10
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S2"
    S2 = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # S3
    curve_list = list()
    curve_list.append(Segment(Z3, Z4, prop_dict=None))
    curve_list.append(Segment(Z4, Z13, prop_dict=None))
    curve_list.append(Segment(Z13, Z12, prop_dict=None))
    curve_list.append(Segment(Z12, Z3, prop_dict=None))
    Zmid = (Z3 + Z4 + Z12 + Z13) / 4
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S3"
    S3 = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # S4
    Z15_ = point_dict["Z15*"]
    Z14_ = point_dict["Z14*"]
    curve_list = list()
    curve_list.append(Segment(Z13, Z4, prop_dict=None))
    curve_list.append(Segment(Z4, Z5, prop_dict=None))
    if abs(Z15 - Z14) > abs(Z15_ - Z14_):
        curve_list.append(Segment(Z5, Z14, prop_dict=None))
        curve_list.append(Segment(Z14, Z13, prop_dict=None))
        Zmid = (Z13 + Z4 + Z5 + Z14) / 4
    else:
        curve_list.append(Segment(Z5, Z14_, prop_dict=None))
        curve_list.append(Segment(Z14_, Z13, prop_dict=None))
        Zmid = (Z13 + Z4 + Z5 + Z14_) / 4
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S4"
    S4 = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # S5
    if abs(Z15 - Z14) > abs(Z15_ - Z14_):
        curve_list = list()
        curve_list.append(Segment(Z14, Z5, prop_dict=None))
        curve_list.append(Arc1(Z5, Z6, abs(Z5), prop_dict=None))
        curve_list.append(Segment(Z6, Z15, prop_dict=None))
        curve_list.append(Arc1(Z15, Z15_, -np_abs(Z15_), is_trigo_direction=False))
        curve_list.append(Segment(Z15_, Z14_, prop_dict=None))
        curve_list.append(Arc1(Z14_, Z14, -np_abs(Z14_), is_trigo_direction=False))
        Zmid = (Z14 + Z5 + Z6 + Z15 + Z15_ + Z14_) / 6
        label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S5"
        S5 = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)
    else:
        curve_list = list()
        curve_list.append(Segment(Z14_, Z5, prop_dict=None))
        curve_list.append(Arc1(Z5, Z6, abs(Z5), prop_dict=None))
        curve_list.append(Segment(Z6, Z15_, prop_dict=None))
        curve_list.append(Segment(Z15_, Z14_, prop_dict=None))
        Zmid = (Z5 + Z6 + Z15_ + Z14_) / 4
        label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S5"
        S5 = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # S6
    curve_list = list()
    curve_list.append(Segment(Z6, Z7, prop_dict=None))
    curve_list.append(Segment(Z7, Z16, prop_dict=None))
    if abs(Z15 - Z14) > abs(Z15_ - Z14_):
        curve_list.append(Segment(Z16, Z15, prop_dict=None))
        curve_list.append(Segment(Z15, Z6, prop_dict=None))
        Zmid = (Z6 + Z7 + Z16 + Z15) / 4
    else:
        curve_list.append(Segment(Z16, Z15_, prop_dict=None))
        curve_list.append(Segment(Z15_, Z6, prop_dict=None))
        Zmid = (Z6 + Z7 + Z16 + Z15_) / 4
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S6"
    S6 = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # S7
    curve_list = list()
    curve_list.append(Segment(Z16, Z7, prop_dict=None))
    curve_list.append(Segment(Z7, Z8, prop_dict=None))
    curve_list.append(Segment(Z8, Z17, prop_dict=None))
    curve_list.append(Segment(Z17, Z16, prop_dict=None))
    Zmid = (Z16 + Z7 + Z8 + Z17) / 4
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S7"
    S7 = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # S8
    curve_list = list()
    curve_list.append(Segment(Z11_, Z14_))
    curve_list.append(Segment(Z14_, Z15_))
    curve_list.append(Segment(Z15_, Z18_))
    curve_list.append(Segment(Z18_, Z11_))
    Zmid = (Z11_ + Z14_ + Z15_ + Z18_) / 4
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S8"
    S8 = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # Apply transformation
    surfaces = [S1, S2, S3, S4, S5, S6, S7, S8]
    for surface in surfaces:
        surface.rotate(alpha)
        surface.translate(delta)

    return surfaces
