from ....Methods.Slot.SlotW31B import *


def check(self):
    """Check that the SlotCirc object is correct

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    None
    """

    if self.i_tan == 0:
        raise SlotW31BIsolationCheckError("You must have i_tan > 0")

    if self.i_bore == 0:
        raise SlotW31BIsolationCheckError("You must have i_bore > 0")

    if self.i_tooth == 0:
        raise SlotW31BIsolationCheckError("You must have i_tooth > 0")

    if self.i_yoke == 0:
        raise SlotW31BIsolationCheckError("You must have i_yoke > 0")
