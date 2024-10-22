from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW31B
        A SlotW31B object

    Returns
    -------
    line_dict: dict
        Dictionnary of the slot lines (key: line name, value: line object)
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

    # Creation of curve
    line_dict = dict()
    if self.H0 > 0:
        line_dict["1-2"] = Segment(Z1, Z2)
    else:
        line_dict["1-2"] = None
    line_dict["2-3"] = Segment(Z2, Z3)
    line_dict["3-4"] = Segment(Z3, Z4)
    line_dict["4-5"] = Segment(Z4, Z5)
    line_dict["5-6"] = Arc1(Z5, Z6, abs(Z5))
    line_dict["6-7"] = Segment(Z6, Z7)
    line_dict["7-8"] = Segment(Z7, Z8)
    line_dict["8-9"] = Segment(Z8, Z9)

    if self.H0 > 0:
        line_dict["9-10"] = Segment(Z9, Z10)
    else:
        line_dict["9-10"] = None

    # Closing Arc (Rbo)
    line_dict["10-1"] = Arc1(Z10, Z1, -self.get_Rbo(), is_trigo_direction=False)

    # Add closings for active part. Needed in get_surface_active
    line_dict["8-3"] = Segment(Z8, Z3)
    line_dict["9-2"] = Segment(Z9, Z2)

    # Add isolation lines
    line_dict["11-12"] = Segment(Z11, Z12)
    line_dict["12-13"] = Segment(Z12, Z13, is_ref=True)
    line_dict["13-14"] = Segment(Z13, Z14)
    line_dict["14-15"] = Arc1(Z14, Z15, abs(Z15))
    line_dict["15-16"] = Segment(Z15, Z16)
    line_dict["16-17"] = Segment(Z16, Z17, is_ref=True)
    line_dict["17-18"] = Segment(Z17, Z18)
    line_dict["18-11"] = Segment(Z18, Z11)

    return line_dict
