# -*- coding: utf-8 -*-
from numpy import sqrt, ceil


def calculate_max_radius(Nwppc, R):
    """
    Calculate the maximum radius of the circle that contains all the smaller circles
    arranged in a hexagonal close-packed pattern.

    Parameters
    ----------
    Nwppc : int
        Total number of smaller circles (including the central circle).
    R : float
        Radius of each smaller circle.

    Returns
    -------
    R_total : float
        The minimum radius of the enclosing circle that contains all the smaller circles.

    Notes
    -----
    **Calculating the Number of Rings (Layers)**

    First, we determine how many complete rings (layers) are required to accommodate
    the given number of circles (Nwppc).

    **Total Number of Circles in 'n' Rings**

    The total number of circles up to ring 'n' is given by:

        N_total = 1 + 3 * n * (n + 1)

    - The '1' accounts for the central circle.
    - The term '3 * n * (n + 1)' sums the circles in all the rings up to ring 'n'.

    **Derivation of the Formula**

    *Number of Circles in Each Ring:*

    - Ring 1: 6 circles
    - Ring 2: 12 circles
    - Ring n: 6 * n circles

    *Total Circles in All Rings:*

        Total_circles_in_rings = sum_{k=1}^n (6 * k)
                               = 6 * sum_{k=1}^n k
                               = 6 * [n * (n + 1) / 2]
                               = 3 * n * (n + 1)

    *Including the Central Circle:*

        N_total = 1 + 3 * n * (n + 1)

    **Solving for the Number of Rings (n_max)**

    Given Nwppc, we solve for n_max in the equation:

        Nwppc = 1 + 3 * n_max * (n_max + 1)

    Rearranged as a quadratic equation:

        3 * n_max^2 + 3 * n_max + 1 - Nwppc = 0

    Simplify the quadratic equation:

        n_max^2 + n_max - (Nwppc - 1) / 3 = 0

    This is a quadratic equation in n_max of the form:

        a * n_max^2 + b * n_max + c = 0

    Where:

        a = 1
        b = 1
        c = - (Nwppc - 1) / 3

    **Solving the Quadratic Equation**

    Using the quadratic formula:

        n_max = [ -b + sqrt(b^2 - 4 * a * c) ] / (2 * a)

    Compute the discriminant D:

        D = b^2 - 4 * a * c
          = 1^2 - 4 * 1 * [ - (Nwppc - 1) / 3 ]
          = 1 + [4 * (Nwppc - 1)] / 3

    **Compute n_max:**

        n_max = [ -1 + sqrt(D) ] / (2)

    Since the number of rings cannot be negative, we discard the negative root.

    **Calculating the Maximum Radius (R_total)**

    The maximum radius of the enclosing circle is determined by the distance from
    the center to the centers of the outermost circles plus the radius of a circle.

    - The distance from the center to the centers of outermost circles:

        D_max = 2 * R * n_max

    - The maximum radius of the enclosing circle:

        R_total = D_max + R
                = 2 * R * n_max + R
                = R * (2 * n_max + 1)

    **Steps in the Function**

    1. **Calculate N:**

        N = Nwppc - 1

        This subtracts the central circle from the total count.

    2. **Compute the Discriminant D:**

        D = 1 + (4 * N) / 3

    3. **Solve for n_max:**

        n_max = (-1 + sqrt(D)) / 2

        We round up n_max to the next integer because we cannot have a fraction of a ring.

    4. **Calculate R_total:**

        R_total = R * (2 * n_max + 1)

    **Example Calculation**

    For Nwppc = 19 and R = 1.0:

    - N = 19 - 1 = 18
    - D = 1 + (4 * 18) / 3 = 1 + 24 = 25
    - n_max = (-1 + sqrt(25)) / 2 = ( -1 + 5 ) / 2 = 2
    - R_total = 1.0 * (2 * 2 + 1) = 1.0 * 5 = 5.0

    Therefore, the maximum radius containing all circles is 5.0 units.

    Raises
    ------
    ValueError
        If Nwppc is less than 1 or if the discriminant is negative.

    """
    # Ensure Nwppc is at least 1
    if Nwppc < 1:
        raise ValueError("Nwppc must be at least 1.")

    if Nwppc == 1:
        return R
    elif Nwppc == 2:
        return 2 * R
    elif Nwppc == 3:
        return (2 * sqrt(3) / 3 + 1) * R
    elif Nwppc == 4:
        return sqrt(2) * R + R
    else:
        N = Nwppc - 1
        D = 1 + (4 * N) / 3

        if D < 0:
            raise ValueError("Discriminant is negative. No real roots exist.")

        n_max = (-1 + sqrt(D)) / 2
        n_max = int(ceil(n_max))  # Round up to the next integer

        R_total = R * (2 * n_max + 1)

        return R_total


def comp_width(self):
    """Compute the width of the conductor

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    W: float
        Width of the conductor [m]

    """

    if self.Wins_cond is None:
        if self.Nwppc == 1:
            Wins_wire = self.Wins_wire if self.Wins_wire is not None else 0
            width = self.Wwire + 2 * Wins_wire
        else:
            Rmax = calculate_max_radius(self.Nwppc, self.Wwire / 2 + self.Wins_wire)
            return Rmax * 2
            # raise Exception("Conductor diameter not set")
    else:
        width = self.Wins_cond

    return width
