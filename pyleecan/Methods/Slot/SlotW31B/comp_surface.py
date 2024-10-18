from numpy import pi, sin, arcsin, abs as np_abs


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW31B
        A SlotW31B object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    point_dict = self._comp_point_coordinate()

    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]

    Rbo = self.get_Rbo()

    # Trapez: S = 0.5 * (Wb + Wt) * H
    # Circle Segment: S = 0.5 * r^2 * (alpha - sin(alpha))

    # Trapez 1:
    Wt = np_abs(Z3 - Z8)
    Wb = np_abs(Z7 - Z4)
    H = np_abs(Z7.real - Z8.real)
    S1 = 0.5 * (Wb + Wt) * H

    # Trapez 2:
    Wt = np_abs(Z6 - Z5)
    Wb = np_abs(Z7 - Z4)
    H = np_abs(Z7.real - Z6.real)
    S2 = 0.5 * (Wb + Wt) * H

    # Arc 1 (Of circle segment defined by W2)
    R = abs(Z5)
    alpha = float(2 * arcsin(self.W2 / (2 * R)))
    S3 = (R**2.0) / 2.0 * (alpha - sin(alpha))

    if self.is_outwards():
        # Add the circle segmet surface
        return S1 + S2 + S3
    else:
        # Substract the circle segment surface (different direction for outer-runner)
        return S1 + S2 - S3
