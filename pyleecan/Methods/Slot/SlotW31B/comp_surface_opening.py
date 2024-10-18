from numpy import pi, sin, arcsin, abs as np_abs


def comp_surface_opening(self):
    """Compute the Slot opening surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW31B
        A SlotW31B object

    Returns
    -------
    S: float
        Slot opening surface [m**2]

    """

    point_dict = self._comp_point_coordinate()

    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z8 = point_dict["Z8"]
    Z9 = point_dict["Z9"]
    Z10 = point_dict["Z10"]

    # Trapez: S = 0.5 * (Wb + Wt) * H
    # Circle Segment: S = 0.5 * r^2 * (alpha - sin(alpha))

    # Trapez 1:
    Wt = np_abs(Z1 - Z10)
    Wb = np_abs(Z2 - Z9)
    H = self.H0
    S1 = 0.5 * (Wb + Wt) * H

    # Trapez 2:
    Wt = np_abs(Z2 - Z9)
    Wb = np_abs(Z3 - Z8)
    H = np_abs(Z9.real - Z8.real)
    S2 = 0.5 * (Wb + Wt) * H

    alpha = self.comp_angle_opening()

    # Arc between W0
    Rbo = self.get_Rbo()
    S3 = (Rbo**2.0) / 2.0 * (alpha - sin(alpha))

    return S1 + S2 - S3
