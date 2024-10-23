from numpy import arcsin, exp, sqrt, pi, abs as np_abs, degrees
from ....Functions.Geometry.circle_from_3_points import circle_from_3_points
from ....Functions.Geometry.inter_line_line import inter_line_line
from ....Functions.Geometry.inter_line_circle import inter_line_circle
import matplotlib.pyplot as plt


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    point_dict: dict
        A dict of the slot coordinates
    """
    Rbo = self.get_Rbo()
    Ryoke = self.get_Ryoke()
    # Length of lines to calculate intersections
    L = Rbo + Ryoke

    alpha = float(arcsin(self.W0 / (2 * Rbo)))
    s_angle = 2 * pi / self.Zs

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)  # Point in the middle of the slot opening
    Z1 = Z0 * exp(-1j * alpha)  # First point

    # ls os the segment line
    Z1ls = 0 + 0j
    Z2ls = L * exp(-1j * s_angle / 2)
    perp_vec_tooth = (Z2ls - Z1ls) * 1j / np_abs(Z2ls - Z1ls)

    # l1 is the tooth line
    Z1l1 = Z1ls + (self.W1 / 2) * perp_vec_tooth
    Z2l1 = Z2ls + (self.W1 / 2) * perp_vec_tooth

    # l3 is the back width line
    Z1l3 = 0 - self.W2 / 2 * 1j
    Z2l3 = L - self.W2 / 2 * 1j

    if self.is_outwards():
        # inner-runner
        Z2 = Z1 + self.H0

        if self.H1_is_rad:
            # l2 is the tip line
            Z1l2 = Z2 + self.get_H1()
            Z2l2 = Z1l2 + 1j * L  # Vertical line
            Z3 = inter_line_line(Z1l1, Z2l1, Z1l2, Z2l2)[0]
        else:
            # l4 is the H1 line
            Z1l4 = Z2.real + self.H1
            Z2l4 = Z1l4 + 1j * L  # Vertical line
            Z3 = inter_line_line(Z1l1, Z2l1, Z1l4, Z2l4)[0]

        Z5 = next(
            (
                Z
                for Z in inter_line_circle(Z1l3, Z2l3, Ryoke - self.H3, 0 + 0j)
                if Z.real > 0 and Z.imag < 0
            ),
            None,
        )

        if self.H2_is_rad:
            # l4 is the back angle line
            Z1l4 = Z5.real - self.get_H2()
            Z2l4 = Z1l4 + 1j * L  # Vertical line
            Z4 = inter_line_line(Z1l1, Z2l1, Z1l4, Z2l4)[0]
        else:
            # l5 is the H2 line
            Z1l5 = Z5.real - self.H2
            Z2l5 = Z1l5 + 1j * L  # Vertical line
            Z4 = inter_line_line(Z1l1, Z2l1, Z1l5, Z2l5)[0]
    else:
        # outer-runner
        Z2 = Z1 - self.H0

        if self.H1_is_rad:
            # l2 is the tip line
            Z1l2 = Z2 - self.get_H1()
            Z2l2 = Z1l2 + 1j * L  # Vertical line
            Z3 = inter_line_line(Z1l1, Z2l1, Z1l2, Z2l2)[0]
        else:
            # l4 is the H1 line
            Z1l4 = Z2.real - self.H1
            Z2l4 = Z1l4 + 1j * L  # Vertical line
            Z3 = inter_line_line(Z1l1, Z2l1, Z1l4, Z2l4)[0]

        Z5 = next(
            (
                Z
                for Z in inter_line_circle(Z1l3, Z2l3, Ryoke + self.H3, 0 + 0j)
                if Z.real > 0 and Z.imag < 0
            ),
            None,
        )

        if self.H2_is_rad:
            # l4 is the back angle line
            Z1l4 = Z5.real + self.get_H2()
            Z2l4 = Z1l4 + 1j * L  # Vertical line
            Z4 = inter_line_line(Z1l1, Z2l1, Z1l4, Z2l4)[0]
        else:
            # l5 is the H2 line
            Z1l5 = Z5.real + self.H2
            Z2l5 = Z1l5 + 1j * L  # Vertical line
            Z4 = inter_line_line(Z1l1, Z2l1, Z1l5, Z2l5)[0]

    # Add the points to dictionary
    point_dict = dict()

    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z5
    point_dict["Z6"] = Z5.conjugate()
    point_dict["Z7"] = Z4.conjugate()
    point_dict["Z8"] = Z3.conjugate()
    point_dict["Z9"] = Z2.conjugate()
    point_dict["Z10"] = Z1.conjugate()

    # Add the isolation points
    if self.is_outwards():
        sign = 1
    else:
        sign = -1

    d23 = Z3 - Z2
    d34 = Z4 - Z3
    d45 = Z5 - Z4

    L23_Z1 = Z2 + sign * self.i_bore * d23 / np_abs(d23) * 1j
    L23_Z2 = Z3 + sign * self.i_bore * d23 / np_abs(d23) * 1j

    L34_Z1 = Z3 + sign * self.i_tooth * d34 / np_abs(d34) * 1j
    L34_Z2 = Z4 + sign * self.i_tooth * d34 / np_abs(d34) * 1j

    L45_Z1 = Z4 + sign * self.i_yoke * d45 / np_abs(d45) * 1j
    L45_Z2 = Z5 + sign * self.i_yoke * d45 / np_abs(d45) * 1j

    Z11 = L23_Z1
    Z12 = inter_line_line(L23_Z1, L23_Z2, L34_Z1, L34_Z2)[0]
    Z13 = inter_line_line(L34_Z1, L34_Z2, L45_Z1, L45_Z2)[0]

    Z14 = next(
        (
            Z
            for Z in inter_line_circle(
                L45_Z1, L45_Z2, Ryoke - sign * self.H3 - sign * self.i_yoke
            )
            if Z.real > 0 and Z.imag < 0
        ),
        None,
    )

    point_dict["Z11"] = Z11
    point_dict["Z12"] = Z12
    point_dict["Z13"] = Z13
    point_dict["Z14"] = Z14
    point_dict["Z15"] = Z14.conjugate()
    point_dict["Z16"] = Z13.conjugate()
    point_dict["Z17"] = Z12.conjugate()
    point_dict["Z18"] = Z11.conjugate()

    # Add additional isolation points needed to create surface_opening surfaces
    Z1_l_tan = 0 - self.i_tan / 2 * 1j
    Z2_l_tan = L - self.i_tan / 2 * 1j

    if self.i_tan < self.W2:
        Z14_i_tan = next(
            (
                Z
                for Z in inter_line_circle(Z1_l_tan, Z2_l_tan, np_abs(Z14), 0j)
                if Z.real >= 0 and Z.imag <= 0
            ),
            None,
        )
    else:
        Z14_i_tan = inter_line_line(Z1_l_tan, Z2_l_tan, Z13, Z14)[0]

    if np_abs(Z11 - Z11.conjugate()) > self.i_tan:
        Z11_i_tan = inter_line_line(Z1_l_tan, Z2_l_tan, Z11, Z11.conjugate())[0]
    else:
        Z11_i_tan = inter_line_line(Z1_l_tan, Z2_l_tan, Z11, Z12)[0]

    point_dict["Z14*"] = Z14_i_tan
    point_dict["Z15*"] = Z14_i_tan.conjugate()
    point_dict["Z11*"] = Z11_i_tan
    point_dict["Z18*"] = Z11_i_tan.conjugate()

    # fig, ax = plt.subplots()

    # # Iterate over point_dict and plot points with annotations
    # for key, value in point_dict.items():
    #     ax.plot(value.real, value.imag, "ro")  # Plot the points as red dots
    #     ax.text(
    #         value.real, value.imag, key, fontsize=12, color="red"
    #     )  # Annotate each point

    # # Set labels and title
    # ax.set_xlabel("Real part")
    # ax.set_ylabel("Imaginary part")
    # ax.set_title("Points")
    # ax.grid(True)

    # # Display plot
    # plt.axis("equal")  # To maintain aspect ratio
    # plt.show()

    return point_dict
