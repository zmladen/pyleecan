from ....Methods import ParentMissingError


def get_Wins_cond(self):
    """Return the wire width (Wins_cond) from the conductor if it exists."""
    if self.parent is not None:
        if hasattr(self.parent, "winding") and self.parent.winding is not None:
            if (
                hasattr(self.parent.winding, "conductor")
                and self.parent.winding.conductor is not None
            ):
                conductor = self.parent.winding.conductor
                if hasattr(conductor, "Wins_cond"):
                    return conductor.comp_width()
                else:
                    raise AttributeError(
                        f"Error: 'Conductor' is a base class and has no attribute 'Wins_cond'. Assign different conductor type to winding."
                    )
            else:
                raise ValueError("Error: No conductor found inside the winding.")
        else:
            raise ValueError("Error: No winding found inside the slot.")
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination.")
