from ....Methods import ParentMissingError


def get_conductor(self):
    """Return the conductor object inside the winding if it exists."""
    if self.parent is not None:
        if hasattr(self.parent, "winding") and self.parent.winding is not None:
            winding = self.parent.winding
            if hasattr(winding, "conductor") and winding.conductor is not None:
                return winding.conductor  # Return the conductor object
            else:
                raise ValueError("Error: No conductor found inside the winding.")
        else:
            raise ValueError("Error: No winding found inside the slot.")
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination.")
