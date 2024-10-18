from ....Methods import ParentMissingError


def get_Ryoke(self):
    """Return the parent lamination bore yoke

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    Ryoke: float
        The parent lamination yoke radius [m]

    """

    if self.parent is not None:
        return self.parent.get_Ryoke()
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination")
