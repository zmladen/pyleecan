import matplotlib.pyplot as plt
from numpy import pi, exp, radians, degrees, abs as np_abs

from ....Classes.Arc1 import Arc1
from ....Classes.Arc2 import Arc2
from ....Classes.Arc3 import Arc3
from ....Classes.LamSlot import LamSlot
from ....Classes.Segment import Segment
from ....definitions import config_dict
from ....Functions.Plot import (
    ARROW_COLOR,
    ARROW_WIDTH,
    MAIN_LINE_COLOR,
    MAIN_LINE_STYLE,
    MAIN_LINE_WIDTH,
    P_FONT_SIZE,
    SC_FONT_SIZE,
    SC_LINE_COLOR,
    SC_LINE_STYLE,
    SC_LINE_WIDTH,
    TEXT_BOX,
    plot_quote,
)
from ....Methods import ParentMissingError

MAGNET_COLOR = config_dict["PLOT"]["COLOR_DICT"]["MAGNET_COLOR"]


def plot_schematics(
    self,
    is_default=False,
    is_return_default=False,
    is_add_point_label=False,
    is_add_schematics=True,
    is_add_main_line=True,
    type_add_active=1,
    save_path=None,
    is_show_fig=True,
    fig=None,
    ax=None,
):
    """Plot the schematics of the slot

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object
    is_default : bool
        True: plot default schematics, else use current slot values
    is_return_default : bool
        True: return the default lamination used for the schematics (skip plot
    is_add_point_label : bool
        True to display the name of the points (Z1, Z2....)
    is_add_schematics : bool
        True to display the schematics information (W0, H0...)
    is_add_main_line : bool
        True to display "main lines" (slot opening and 0x axis)
    type_add_active : int
        0: No active surface, 1: active surface as winding, 2: active surface as magnet, 3: active surface as winding + wedges
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    is_show_fig : bool
        To call show at the end of the method
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data

    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the schematics
    ax : Matplotlib.axes.Axes object
        Axis containing the schematics
    -------
    lam : LamSlot
        Default lamination used for the schematics
    """

    # Use some default parameter
    if is_default:
        slot = type(self)(Zs=12)
        lam = LamSlot(
            Rint=0.015, Rext=0.03, is_internal=False, is_stator=True, slot=slot
        )
        if is_return_default:
            return lam
        else:
            return slot.plot_schematics(
                is_default=False,
                is_return_default=False,
                is_add_point_label=is_add_point_label,
                is_add_schematics=is_add_schematics,
                is_add_main_line=is_add_main_line,
                type_add_active=type_add_active,
                save_path=save_path,
                is_show_fig=is_show_fig,
                fig=fig,
                ax=ax,
            )
    else:
        # Getting the main plot
        if self.parent is None:
            raise ParentMissingError("Error: The slot is not inside a Lamination")
        lam = self.parent
        fig, ax = lam.plot(
            alpha=pi / self.Zs, is_show_fig=False, fig=fig, ax=ax
        )  # center slot on Ox axis
        point_dict = self._comp_point_coordinate()
        if self.is_outwards():
            sign = 1
        else:
            sign = -1

        # Adding point label
        if is_add_point_label:
            for name, Z in point_dict.items():
                ax.text(
                    Z.real,
                    Z.imag,
                    name,
                    fontsize=P_FONT_SIZE,
                    bbox=TEXT_BOX,
                )

        # Adding schematics
        if is_add_schematics:
            # W0
            line = Segment(point_dict["Z1"], point_dict["Z10"])
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W0",
                offset_label=self.H0 * 0.2,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # W1
            Znorm = (
                1j
                * (point_dict["Z4"] - point_dict["Z3"])
                / np_abs((point_dict["Z4"] - point_dict["Z3"]))
            )
            line = Segment(point_dict["Z3"], point_dict["Z3"] - self.W1 * Znorm)
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="W1",
                offset_label=self.W1 * 0.2,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # W2
            line = Segment(
                point_dict["Z5"] + self.H3 / 2, point_dict["Z6"] + self.H3 / 2
            )
            line.plot(
                fig=fig,
                ax=ax,
                label="W2",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=1 * self.W0 * 0.15,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H0
            line = Segment(point_dict["Z10"], point_dict["Z9"])
            line.plot(
                fig=fig,
                ax=ax,
                label="H0",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=1j * self.W0 * 0.15,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

            # H1 [rad]
            line = Arc2(
                begin=point_dict["Z3"]
                + (point_dict["Z2"] - point_dict["Z3"]) * (3 / 4),
                center=point_dict["Z3"],
                angle=-self.H1,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="H1 [rad]",
                offset_label=-1j * sign * line.comp_radius() * 0.15,
                fontsize=SC_FONT_SIZE,
            )
            # H1 [m]
            line = Segment(point_dict["Z2"], point_dict["Z2"] + self.get_H1())
            line.plot(
                fig=fig,
                ax=ax,
                label="H1",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=1j * self.get_H1() * 0.7,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )
            # H2 [rad]
            line = Arc2(
                begin=point_dict["Z4"] + (point_dict["Z5"] - point_dict["Z4"]) / 2,
                center=point_dict["Z4"],
                angle=self.H2,  # - 2 * pi / self.Zs
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="H2 [rad]",
                offset_label=-1j * sign * line.comp_radius() * 0.15,
                fontsize=SC_FONT_SIZE,
            )
            # H2 [m]
            line = Segment(point_dict["Z5"], point_dict["Z5"] - self.get_H2())
            line.plot(
                fig=fig,
                ax=ax,
                label="H2 [m]",
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                offset_label=1j * self.get_H2() * 0.7,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

            # i_yoke
            Z1 = point_dict["Z15"]
            Z2 = point_dict["Z16"]
            Zm = (Z1 + Z2) / 2
            Znorm = 1j * (Z2 - Z1) / np_abs(Z1 - Z2)
            line = Segment(
                Zm,
                Zm - self.i_yoke * Znorm,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="i_yoke",
                offset_label=self.i_yoke * 0.5j,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

            # i_tooth
            Z1 = point_dict["Z12"]
            Z2 = point_dict["Z13"]
            Zm = (Z1 + Z2) / 2
            Znorm = 1j * (Z2 - Z1) / np_abs(Z1 - Z2)
            line = Segment(
                Zm,
                Zm - self.i_tooth * Znorm,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="i_tooth",
                offset_label=self.i_tooth * 0.5j,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

            # i_bore
            Z1 = point_dict["Z17"]
            Z2 = point_dict["Z18"]
            Zm = (Z1 + Z2) / 2
            Znorm = 1j * (Z2 - Z1) / np_abs(Z1 - Z2)
            line = Segment(
                Zm,
                Zm - self.i_bore * Znorm,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="i_bore",
                offset_label=self.i_bore * 0.5j,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

            # i_tan
            Z1 = (
                point_dict["Z11"].real + point_dict["Z15"].real
            ) / 2 - self.i_tan / 2 * 1j
            Z2 = (
                point_dict["Z11"].real + point_dict["Z15"].real
            ) / 2 + self.i_tan / 2 * 1j

            line = Segment(Z1, Z2)
            line.plot(
                fig=fig,
                ax=ax,
                color=ARROW_COLOR,
                linewidth=ARROW_WIDTH,
                label="i_tan",
                offset_label=self.i_tan * 0.25,
                is_arrow=True,
                fontsize=SC_FONT_SIZE,
            )

        if is_add_main_line:
            # Ox axis
            line = Segment(0, lam.Rext * 1.5)
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # Top arc
            line = Arc1(
                begin=point_dict["Z1"],
                end=point_dict["Z10"],
                radius=self.get_Rbo(),
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # Bot Arc
            line = Arc1(
                begin=abs(point_dict["Z5"]) * exp(-1j * pi / 4),
                end=abs(point_dict["Z5"]) * exp(1j * pi / 4),
                radius=abs(point_dict["Z5"]),
                is_trigo_direction=True,
            )
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # H0 lines
            line = Segment(0, point_dict["Z1"])
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            line = Segment(0, point_dict["Z10"])
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )
            # H1 lines
            line = Segment(point_dict["Z2"], point_dict["Z9"])
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )

            # H2 lines
            line = Segment(point_dict["Z4"], point_dict["Z7"])
            line.plot(
                fig=fig,
                ax=ax,
                color=MAIN_LINE_COLOR,
                linestyle=MAIN_LINE_STYLE,
                linewidth=MAIN_LINE_WIDTH,
            )

        if type_add_active in [1, 3]:  # Wind and Wedge
            is_add_wedge = type_add_active == 3
            self.plot_active(
                fig=fig, ax=ax, is_show_fig=False, is_add_wedge=is_add_wedge
            )
        elif type_add_active == 2:  # Magnet
            self.plot_active(
                fig=fig,
                ax=ax,
                is_show_fig=False,
                enforced_default_color=MAGNET_COLOR,
            )

        # Zooming and cleaning
        W = (
            max(
                np_abs(point_dict["Z3"] - point_dict["Z8"]),
                np_abs(point_dict["Z4"] - point_dict["Z7"]),
            )
            * 0.6
        )
        Rint = min(point_dict["Z5"].real, point_dict["Z1"].real)
        Rext = max(point_dict["Z5"].real, point_dict["Z1"].real)

        ax.axis("equal")
        ax.set_xlim(Rint, Rext)
        ax.set_ylim(-W, W)
        manager = plt.get_current_fig_manager()
        if manager is not None:
            manager.set_window_title(type(self).__name__ + " Schematics")
        ax.set_title("")
        ax.get_legend().remove()
        ax.set_axis_off()
        fig.tight_layout()

        # Save / Show
        if save_path is not None:
            fig.savefig(save_path)
            plt.close(fig=fig)

        if is_show_fig:
            fig.show()
        return fig, ax
