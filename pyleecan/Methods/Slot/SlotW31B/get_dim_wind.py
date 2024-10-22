from ....Methods import ParentMissingError


def get_dim_wind(self):
    """Return the winding dimensions (Nrad, Ntan) if they exist, or default to (1, 1)."""
    if self.parent is not None:
        if hasattr(self.parent, "winding") and self.parent.winding is not None:
            winding = self.parent.winding
            try:
                # Try to get winding dimensions (Nrad, Ntan)
                Nrad, Ntan = winding.get_dim_wind()
            except Exception:
                # Default to (1, 1) if there's an issue
                Nrad, Ntan = 1, 1
            return Nrad, Ntan
        else:
            raise ValueError("Error: No winding found inside the slot.")
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination.")
