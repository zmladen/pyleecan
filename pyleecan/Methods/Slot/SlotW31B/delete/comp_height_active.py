def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlowW31B
        A SlowW31B object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]
    """
    point_dict = self._comp_point_coordinate()
    Z11 = point_dict["Z11"]
    Z14 = point_dict["Z14"]

    if self.is_outwards():
        # inner-runner
        return abs(Z11) - abs(Z14)
    else:
        # outer-runner
        return abs(Z14) - abs(Z11)
