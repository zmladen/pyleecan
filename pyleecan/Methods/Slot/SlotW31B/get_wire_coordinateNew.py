import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def get_wire_coordinateNew(self, is_debug=False):

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

    colors = ["red", "green", "blue", "orange"]
    for ii, surface in enumerate(surf_Wind):

        wires = surface._get_wire_coordinate(Wwire, self.is_outwards())

        if is_debug:
            for point in wires:
                ax.plot(point.real, point.imag, "ko", markersize=1)
                red_circle = Circle(
                    (point.real, point.imag),
                    Wwire / 2,
                    color=colors[ii],
                    fill=False,
                    linewidth=2,
                )
                ax.add_patch(red_circle)

    if is_debug:
        plt.axis("equal")
        plt.show()
