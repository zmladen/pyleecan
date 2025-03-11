from ....Functions.init_fig import init_fig
from ....definitions import config_dict
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from numpy import array


ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]
PHASE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
# SLOT_COLOR = config_dict["PLOT"]["COLOR_DICT"]["SLOT_COLOR"]


def plot(
    self,
    wind_mat=None,
    fig=None,
    ax=None,
    is_show_fig=True,
    is_show_wires=True,
    enforced_default_color=None,
):
    """Plot the Slot in a matplotlib fig

    Parameters
    ----------
    self : Slot
        A Slot object
    wind_mat : numpy.ndarray
        A matrix [Nrad,Ntan,Zs,qs] representing the active (Default value = None)
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)
    is_show_wires : bool
        If True, plot the wires inside the slots (Default = False)
    enforced_default_color : str
        If not None enforce the active color (when wind_mat is None)
    Returns
    -------
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """
    surf = self.get_surface()

    # Display the result
    (fig, ax, patch_leg, label_leg) = init_fig(fig, ax)
    ax.set_xlabel("[m]")
    ax.set_ylabel("[m]")
    ax.set_title("Slot")

    # Add the slot to the fig
    if self.get_is_stator:
        patches = surf.get_patches(color="white")  # STATOR_COLOR
    else:
        patches = surf.get_patch(color=ROTOR_COLOR)
    for patch in patches:
        ax.add_patch(patch)

    if wind_mat is None:  # Default : Only one zone monocolor
        Nrad, Ntan, qs, Zs = 1, 1, 1, self.Zs
    else:
        (Nrad, Ntan, Zs, qs) = wind_mat.shape

    surf_list = self.build_geometry_active(Nrad, Ntan)

    patches = list()
    for ii in range(len(surf_list)):
        # Compute the coordinate for one zone
        point_list = list()
        for curve in surf_list[ii].get_lines():
            point_list.extend(curve.discretize().tolist())
        point_list = array(point_list)

        if wind_mat is None or len(surf_list) != Ntan * Nrad:
            x, y = point_list.real, point_list.imag
            patches.append(Polygon(list(zip(x, y)), color=enforced_default_color))
        else:
            x, y = point_list.real, point_list.imag
            patches.append(Polygon(list(zip(x, y)), color="k", fill=None))

    # Add the active area to the fig
    for patch in patches:
        ax.add_patch(patch)

    if is_show_wires:
        # List to collect all patches and corresponding colors
        all_patches = []
        all_colors = []

        for surface in surf_list:
            w_cord = surface.comp_conductor_centers(self.get_Wins_cond())
            conductor = self.get_conductor()

            for wire in w_cord:
                # Set conductor origin to wire position
                conductor.origin = wire
                # Get the patches from the conductor's plot method
                conductor_patches = conductor.plot(return_patches=True)

                # Add all patches and their colors to the lists
                for patch in conductor_patches:
                    all_patches.append(patch)
                    all_colors.append(patch.get_facecolor())

        # Use PatchCollection for all patches with their respective colors
        patch_collection = PatchCollection(
            all_patches, facecolor=all_colors, edgecolor="none", zorder=2
        )

        # Add the collection to the axis
        ax.add_collection(patch_collection)

    # Axis Setup
    ax.axis("equal")
    if is_show_fig:
        fig.show()
    return fig, ax
