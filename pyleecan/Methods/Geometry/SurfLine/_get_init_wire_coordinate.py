from ....Functions.Geometry.inter_line_line import inter_line_line
import math
import numpy as np


def complex_to_array(z):
    """Converts a complex number into a 2D array [real, imag]."""
    return np.array([z.real, z.imag])


def determine_sign(ref_line, adj_line):
    # Calculate the perpendicular vectors

    perp_ref = (ref_line.end - ref_line.begin) / abs(ref_line.end - ref_line.begin) * 1j

    # Midpoints of the lines
    mid_ref = (ref_line.end + ref_line.begin) / 2
    mid_adj = (adj_line.end + adj_line.begin) / 2

    vec_mid = mid_adj - mid_ref

    dot_ref = np.dot(complex_to_array(vec_mid), complex_to_array(perp_ref))

    if dot_ref >= 0:
        return 1
    else:
        return -1


def _get_init_wire_coordinate(self, Wwire):
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
    ref_line, ref_idx = self._get_ref_line()
    adj_line, adj_idx = self._get_adj_line()

    d_ref = ref_line.end - ref_line.begin
    d_adj = adj_line.end - adj_line.begin

    # Determine the sign based on the direction (is_outwards)
    # sign = 1 if is_outwards else -1

    sign = determine_sign(ref_line, adj_line)

    # Move the adjacent line parallel to itself by Wwire / 2
    L_adj_Z1 = adj_line.begin + sign * Wwire / 2 * d_adj / abs(d_adj) * 1j
    L_adj_Z2 = adj_line.end + sign * Wwire / 2 * d_adj / abs(d_adj) * 1j

    # Move the reference line parallel to itself by Wwire / 2
    L_ref_Z1 = ref_line.begin + sign * Wwire / 2 * d_ref / abs(d_ref) * 1j
    L_ref_Z2 = ref_line.end + sign * Wwire / 2 * d_ref / abs(d_ref) * 1j

    center = inter_line_line(L_adj_Z1, L_adj_Z2, L_ref_Z1, L_ref_Z2)[0]

    return center
