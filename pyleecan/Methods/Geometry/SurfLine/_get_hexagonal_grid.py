from numpy import sqrt


def _get_hexagonal_grid(self, Wwire):
    """
    Creates a hexagonal grid of points aligned with a reference line.

    Parameters:
    - initial_center: complex, the starting point of the grid (complex number).
    - ref_line: complex, the reference line direction (complex number).
    - Wwire: float, the wire diameter used to define the grid spacing.
    - num_points_x: int, number of points along the reference direction.
    - num_points_y: int, number of points perpendicular to the reference direction.

    Returns:
    - grid_points: list of complex points representing the grid.
    """

    ref_line, ref_idx = self._get_ref_line()
    min_x, max_x, min_y, max_y = self._get_bounding_box()
    Zi = self._get_init_wire_coordinate(Wwire)
    num_points_x = int(abs(max_x - min_x) // Wwire)
    num_points_y = int(abs(max_y - min_y) // (Wwire * sqrt(3) / 2))

    dir_vec = ref_line.end - ref_line.begin
    dir_unit = dir_vec / abs(dir_vec)
    normal_unit = dir_unit * 1j

    dx = Wwire * 1
    dy = Wwire * sqrt(3) / 2

    grid_points = []

    for i in range(-num_points_x, num_points_x + 1):
        for j in range(-num_points_y, num_points_y + 1):

            shift_x = dx / 2
            if j % 2:
                pos = Zi + i * dx * dir_unit + ((j - 1) * dy) * normal_unit
            else:
                pos = Zi + (i * dx + shift_x) * dir_unit + ((j - 1) * dy) * normal_unit
            grid_points.append(pos)

    return grid_points
