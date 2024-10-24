def _get_adj_line(self):
    """Determine the adjacent line based on the direction of the current line and is_outwards flag.

    Parameters:
    line_list (list): List of lines in the surface.
    idx (int): Index of the current line in the line_list.
    line (Line): The current reference line.

    Returns:
    Line: The adjacent line to be used for intersection.
    """
    adj_line = None
    adj_idx = None

    line_list = self.get_lines()
    # Search for the reference line
    for idx, line in enumerate(line_list):
        if line and line.prop_dict and line.prop_dict.get("adj"):
            adj_line = line.copy()
            adj_idx = idx
            return adj_line, adj_idx

    # If no adj line is found, use the next segment as adj
    ref_line, ref_idx = self._get_ref_line()

    next_idx = (ref_idx + 1) if ref_idx < len(line_list) - 1 else 0
    adj_line = line_list[next_idx]

    return adj_line, next_idx

    # ref_line, ref_idx = self._get_ref_line()
    # line_list = self.get_lines()

    # if is_outwards:
    #     # inner-runner
    #     if ref_line.begin < ref_line.end:
    #         # Use the next segment
    #         next_idx = (ref_idx + 1) if ref_idx < len(line_list) - 1 else 0
    #         adjacent_line = line_list[next_idx]
    #     else:
    #         # Use the previous segment
    #         prev_idx = (ref_idx - 1) if ref_idx > 0 else len(line_list) - 1
    #         adjacent_line = line_list[prev_idx]
    # else:
    #     # outer-runner
    #     if ref_line.begin < ref_line.end:
    #         # Use the previous segment
    #         prev_idx = (ref_idx - 1) if ref_idx > 0 else len(line_list) - 1
    #         adjacent_line = line_list[prev_idx]
    #     else:
    #         # Use the next segment
    #         next_idx = (ref_idx + 1) if ref_idx < len(line_list) - 1 else 0
    #         adjacent_line = line_list[next_idx]

    # return adjacent_line
