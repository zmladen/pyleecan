from matplotlib.path import Path
from numpy import pi, exp, linspace


def gen_wire_boundary(center, radius, num_points=16):
    angles = linspace(0, 2 * pi, num_points, endpoint=False)
    return [center + radius * exp(1j * angle) for angle in angles]


def _get_wire_coordinate(self, Wwire, is_outwards):
    """
    Filters the grid points to only keep the ones inside the polygon.

    Parameters:
    - grid_points: list of complex points representing the grid.
    - line_list: list of lines or arcs from the surface (each with 'begin' and 'end' points and possibly needing discretization).
    - nb_point: int, the number of points used for discretizing arcs/lines.

    Returns:
    - filtered_points: list of complex points that are inside the polygon.
    """

    grid_points = self._get_hexagonal_grid(Wwire, is_outwards)

    polygon_vertices = []
    for line in self.get_lines():
        # Only for arcs as line will not be discretized by default
        points = line.discretize()
        polygon_vertices.extend(points)

    path = Path([(vertex.real, vertex.imag) for vertex in polygon_vertices])

    # Firtst filter the grid points without consiredinr Wwire! It is faster
    filtered_points = [
        point for point in grid_points if path.contains_point((point.real, point.imag))
    ]

    # Now filter the points with Wwire
    output = []
    for point in filtered_points:
        w_points = gen_wire_boundary(point, 0.98 * Wwire / 2)

        if all(path.contains_point((bp.real, bp.imag)) for bp in w_points):
            output.append(point)

    return output
