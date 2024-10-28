from matplotlib.patches import Circle, Patch
from ....Functions.init_fig import init_fig
from ....definitions import config_dict

COND_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][0].copy()
INS_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][1].copy()
COND_INS_COLOR = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][2].copy()
# Remove alpha from phases
COND_COLOR[3] = 1
INS_COLOR[3] = 1
COND_INS_COLOR[3] = 1


from matplotlib.patches import Circle, Patch


def plot(self, is_show_fig=True, fig=None, ax=None, return_patches=False):
    """Plot a Conductor in a matplotlib fig or return patches for efficient plotting.

    Parameters
    ----------
    self : CondType12
        A CondType12 object
    is_show_fig : bool
        To call show at the end of the method
    fig : Matplotlib.figure.Figure
        Existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    return_patches : bool
        If True, return the patches for later use in PatchCollection

    Returns
    -------
    fig : Matplotlib.figure.Figure or list of patches
        Figure containing the plot or list of patches (if return_patches=True)
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """
    patches_list = []

    # Conductor insulation
    insulation_circle = Circle(
        (self.origin.real, self.origin.imag),
        self.comp_width() / 2,
        color=COND_INS_COLOR,
    )
    patches_list.append(insulation_circle)

    for center in self.comp_wire_centers():
        # Adjust center by origin
        center = (center[0] + self.origin.real, center[1] + self.origin.imag)
        Rins = self.Wwire / 2 + self.Wins_wire
        wire_insulation_circle = Circle(center, Rins, color=INS_COLOR)
        wire_circle = Circle(center, self.Wwire / 2, color=COND_COLOR)
        patches_list.append(wire_insulation_circle)
        patches_list.append(wire_circle)

    if return_patches:
        return patches_list

    # Display the figure
    (fig, ax, _, _) = init_fig(fig=fig, ax=ax)
    for patch in patches_list:
        ax.add_patch(patch)

    # Axis Setup
    ax.axis("equal")
    ax_lim = self.comp_width() / 2 + self.comp_width() / 10
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)

    # Legend
    patch_leg = [
        Patch(color=COND_INS_COLOR),
        Patch(color=INS_COLOR),
        Patch(color=COND_COLOR),
    ]
    label_leg = ["Coil insulation", "Wire insulation", "Active wire section"]
    ax.legend(patch_leg, label_leg)

    if is_show_fig:
        fig.show()

    return fig, ax


class NotPlotableError(Exception):
    """ """

    pass
