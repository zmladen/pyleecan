def _get_ref_line(self):
    """
    Find the reference line in the surface. If no reference line is found,
    return the longest line.

    Parameters:
    - surface: Surface object containing the geometry (line_list).

    Returns:
    - ref_line: Line object, either the reference line or the longest line.
    - ref_idx: int, index of the selected line in the surface's line_list.
    """
    ref_line = None
    ref_idx = None

    line_list = self.get_lines()
    # Search for the reference line
    for idx, line in enumerate(line_list):
        if hasattr(line, "is_ref") and line.is_ref:
            ref_line = line.copy()
            ref_idx = idx

            return ref_line, ref_idx

    # If no reference line is found, find the longest line
    if ref_line is None:
        longest_line = max(line_list, key=lambda l: abs(l.end - l.begin))
        ref_line = longest_line.copy()
        ref_idx = line_list.index(longest_line)

    return ref_line, ref_idx
