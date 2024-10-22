import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from matplotlib.path import Path
from ....Functions.Geometry.inter_line_line import inter_line_line


def compute_wire_center(ref_line, adj_line, Wwire, is_outwards):
    """
    Compute the center position for the first wire by moving the reference
    and adjacent lines by Wwire / 2 and finding their intersection.

    Parameters:
    - ref_line: Line object representing the reference line.
    - adj_line: Line object representing the adjacent line.
    - Wwire: float, the wire diameter used to offset the lines.
    - is_outwards: bool, indicates the direction of the movement (sign).

    Returns:
    - center: complex, the center position of the first wire.
    """
    # Compute the direction vectors for the reference and adjacent lines
    d_ref = ref_line.end - ref_line.begin
    d_adj = adj_line.end - adj_line.begin

    # Determine the sign based on the direction (is_outwards)
    sign = 1 if is_outwards else -1

    # Move the adjacent line parallel to itself by Wwire / 2
    L_adj_Z1 = adj_line.begin + sign * Wwire / 2 * d_adj / np.abs(d_adj) * 1j
    L_adj_Z2 = adj_line.end + sign * Wwire / 2 * d_adj / np.abs(d_adj) * 1j

    # Move the reference line parallel to itself by Wwire / 2
    L_ref_Z1 = ref_line.begin + sign * Wwire / 2 * d_ref / np.abs(d_ref) * 1j
    L_ref_Z2 = ref_line.end + sign * Wwire / 2 * d_ref / np.abs(d_ref) * 1j

    # Find the intersection between the moved adjacent and reference lines
    center = inter_line_line(L_adj_Z1, L_adj_Z2, L_ref_Z1, L_ref_Z2)[0]

    return center


def calculate_bounding_box(surface):
    """Calculate the bounding box for a surface."""
    min_x = min(min(line.begin.real, line.end.real) for line in surface.line_list)
    max_x = max(max(line.begin.real, line.end.real) for line in surface.line_list)
    min_y = min(min(line.begin.imag, line.end.imag) for line in surface.line_list)
    max_y = max(max(line.begin.imag, line.end.imag) for line in surface.line_list)

    return min_x, max_x, min_y, max_y


def is_point_in_polygon(point, polygon_vertices):
    """
    Ray-casting algorithm to determine if a point is inside a polygon.

    Parameters:
    - point: complex, the point to check.
    - polygon_vertices: list of complex, the vertices of the polygon.

    Returns:
    - True if the point is inside the polygon, False otherwise.
    """
    n = len(polygon_vertices)
    inside = False
    x, y = point.real, point.imag

    # Loop through each edge of the polygon
    for i in range(n):
        v1 = polygon_vertices[i]
        v2 = polygon_vertices[(i + 1) % n]  # Wrap around to the first vertex

        x1, y1 = v1.real, v1.imag
        x2, y2 = v2.real, v2.imag

        # Check if point is on the edge or between the y-range of the edge
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside


def generate_circle_boundary(center, radius, num_points=16):
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    return [center + radius * np.exp(1j * angle) for angle in angles]


def filter_points_inside_polygon(grid_points, line_list, Wwire):
    """
    Filters the grid points to only keep the ones inside the polygon.

    Parameters:
    - grid_points: list of complex points representing the grid.
    - line_list: list of lines or arcs from the surface (each with 'begin' and 'end' points and possibly needing discretization).
    - nb_point: int, the number of points used for discretizing arcs/lines.

    Returns:
    - filtered_points: list of complex points that are inside the polygon.
    """
    # Collect the discretized points from the line_list
    polygon_vertices = []

    for line in line_list:
        # Discretize the line (or arc)
        if hasattr(line, "discretize"):
            points = line.discretize()  # Discretize returns a list of points
        else:
            points = [
                line.get_begin(),
                line.get_end(),
            ]  # If no discretize, just use begin and end points

        polygon_vertices.extend(points)  # Add all points from discretization

    # Convert polygon vertices to a (x, y) tuple format for Path
    polygon_path = Path([(vertex.real, vertex.imag) for vertex in polygon_vertices])

    # Firtst filter the grid points
    filtered_points = [
        point
        for point in grid_points
        if polygon_path.contains_point((point.real, point.imag))
    ]

    output = []
    for point in filtered_points:
        # Generate points on the boundary of the circle with radius Wwire / 2
        boundary_points = generate_circle_boundary(point, 0.98 * Wwire / 2)

        # Check if all boundary points are inside the polygon
        if all(
            polygon_path.contains_point((bp.real, bp.imag)) for bp in boundary_points
        ):
            output.append(point)

    return output


def create_hex_grid(initial_center, ref_line, Wwire, min_x, max_x, min_y, max_y):
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

    # Calculate the width and height of the bounding box
    width_x = max_x - min_x
    width_y = max_y - min_y

    # Calculate the number of points along the x and y directions
    num_points_x = int(width_x // Wwire)
    num_points_y = int(width_y // (Wwire * np.sqrt(3) / 2))

    dir_vec = ref_line.end - ref_line.begin
    dir_unit = dir_vec / abs(dir_vec)
    normal_unit = dir_unit * 1j

    # Grid spacing for hexagonal grid
    dx = Wwire * 1
    dy = Wwire * np.sqrt(3) / 2

    grid_points = []

    for i in range(-num_points_x, num_points_x + 1):
        for j in range(-num_points_y, num_points_y + 1):

            shift_y = 0
            shift_x = dx / 2
            if j % 2:
                pos = (
                    initial_center
                    + i * dx * dir_unit
                    + ((j - 1) * dy + shift_y) * normal_unit
                )
            else:
                pos = (
                    initial_center
                    + (i * dx + shift_x) * dir_unit
                    + ((j - 1) * dy + shift_y) * normal_unit
                )
            grid_points.append(pos)

    return grid_points


def get_adj_line(line_list, idx, line, is_outwards):
    """Determine the adjacent line based on the direction of the current line and is_outwards flag.

    Parameters:
    line_list (list): List of lines in the surface.
    idx (int): Index of the current line in the line_list.
    line (Line): The current reference line.
    is_outwards (bool): Direction flag.

    Returns:
    Line: The adjacent line to be used for intersection.
    """

    if is_outwards:
        # inner-runner
        print("inner-runner")
        if line.begin < line.end:
            # Use the next segment
            next_idx = (idx + 1) if idx < len(line_list) - 1 else 0
            adjacent_line = line_list[next_idx]
        else:
            # Use the previous segment
            prev_idx = (idx - 1) if idx > 0 else len(line_list) - 1
            adjacent_line = line_list[prev_idx]
    else:
        # outer-runner
        print("outer-runner")
        if line.begin < line.end:
            # Use the previous segment
            prev_idx = (idx - 1) if idx > 0 else len(line_list) - 1
            adjacent_line = line_list[prev_idx]
        else:
            # Use the next segment
            next_idx = (idx + 1) if idx < len(line_list) - 1 else 0
            adjacent_line = line_list[next_idx]

    return adjacent_line


def get_ref_line(surface):
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

    # Search for the reference line
    for idx, line in enumerate(surface.line_list):
        if hasattr(line, "is_ref") and line.is_ref:
            ref_line = line.copy()
            ref_idx = idx
            break

    # If no reference line is found, find the longest line
    if ref_line is None:
        longest_line = max(surface.line_list, key=lambda l: np.abs(l.end - l.begin))
        ref_line = longest_line.copy()
        ref_idx = surface.line_list.index(longest_line)

    return ref_line, ref_idx


def get_wire_coordinate(self, is_debug=False):

    wire_coordinate = []

    try:
        Nrad, Ntan = self.get_dim_wind()
    except Exception:
        Nrad, Ntan = 1, 1

    surf_Wind = self.build_geometry_active(
        Nrad=Nrad,
        Ntan=Ntan,
    )

    Wwire = self.get_Wwire() / 1

    if is_debug:
        fig, ax = plt.subplots()
        for surface in surf_Wind:
            surface.plot(fig=fig, ax=ax)

    for ii, surface in enumerate(surf_Wind):

        ref_line, ref_idx = get_ref_line(surface)
        adj_l = get_adj_line(surface.line_list, ref_idx, ref_line, self.is_outwards())

        center = compute_wire_center(ref_line, adj_l, Wwire, self.is_outwards())

        min_x, max_x, min_y, max_y = calculate_bounding_box(surface)

        wire_coordinate = create_hex_grid(
            center, ref_line, Wwire, min_x, max_x, min_y, max_y
        )

        wire_coordinate = filter_points_inside_polygon(
            wire_coordinate, surface.line_list, Wwire
        )

        if is_debug:
            center_x, center_y = center.real, center.imag
            red_circle = Circle(
                (center_x, center_y),
                Wwire / 2,
                color="red",
                fill=False,
                linewidth=2,
            )
            ax.add_patch(red_circle)

            for point in wire_coordinate:
                ax.plot(point.real, point.imag, "bo", markersize=1)
                red_circle = Circle(
                    (point.real, point.imag),
                    Wwire / 2,
                    color="red",
                    fill=False,
                    linewidth=2,
                )
                ax.add_patch(red_circle)

    if is_debug:
        plt.axis("equal")
        plt.show()

    return wire_coordinate
