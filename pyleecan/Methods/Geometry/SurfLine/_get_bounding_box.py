def _get_bounding_box(self):
    """Calculate the bounding box for a surface."""

    line_list = self.get_lines()
    min_x = min(min(line.begin.real, line.end.real) for line in line_list)
    max_x = max(max(line.begin.real, line.end.real) for line in line_list)
    min_y = min(min(line.begin.imag, line.end.imag) for line in line_list)
    max_y = max(max(line.begin.imag, line.end.imag) for line in line_list)

    return min_x, max_x, min_y, max_y
