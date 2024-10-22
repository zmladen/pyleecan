# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotW31B.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotW31B
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotW31B._comp_line_dict import _comp_line_dict
except ImportError as error:
    _comp_line_dict = error

try:
    from ..Methods.Slot.SlotW31B._comp_point_coordinate import _comp_point_coordinate
except ImportError as error:
    _comp_point_coordinate = error

try:
    from ..Methods.Slot.SlotW31B.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotW31B.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotW31B.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotW31B.get_H1 import get_H1
except ImportError as error:
    get_H1 = error

try:
    from ..Methods.Slot.SlotW31B.get_H2 import get_H2
except ImportError as error:
    get_H2 = error

try:
    from ..Methods.Slot.SlotW31B.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotW31B.comp_surface_opening import comp_surface_opening
except ImportError as error:
    comp_surface_opening = error

try:
    from ..Methods.Slot.SlotW31B.get_surface_active import get_surface_active
except ImportError as error:
    get_surface_active = error

try:
    from ..Methods.Slot.SlotW31B.get_surface_opening import get_surface_opening
except ImportError as error:
    get_surface_opening = error

try:
    from ..Methods.Slot.SlotW31B.build_geometry_active import build_geometry_active
except ImportError as error:
    build_geometry_active = error

try:
    from ..Methods.Slot.SlotW31B.get_wire_coordinate import get_wire_coordinate
except ImportError as error:
    get_wire_coordinate = error

try:
    from ..Methods.Slot.SlotW31B.get_wire_coordinateNew import get_wire_coordinateNew
except ImportError as error:
    get_wire_coordinateNew = error

try:
    from ..Methods.Slot.SlotW31B.get_Wwire import get_Wwire
except ImportError as error:
    get_Wwire = error

try:
    from ..Methods.Slot.SlotW31B.get_dim_wind import get_dim_wind
except ImportError as error:
    get_dim_wind = error

try:
    from ..Methods.Slot.SlotW31B.get_conductor import get_conductor
except ImportError as error:
    get_conductor = error

try:
    from ..Methods.Slot.SlotW31B.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error

try:
    from ..Methods.Slot.SlotW31B.plot_active import plot_active
except ImportError as error:
    plot_active = error


from numpy import isnan
from ._check import InitUnKnowClassError


class SlotW31B(Slot):
    """Open slot with back width and back angle"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotW31B._comp_line_dict
    if isinstance(_comp_line_dict, ImportError):
        _comp_line_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method _comp_line_dict: " + str(_comp_line_dict)
                )
            )
        )
    else:
        _comp_line_dict = _comp_line_dict
    # cf Methods.Slot.SlotW31B._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW31B.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotW31B.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW31B method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotW31B.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW31B.get_H1
    if isinstance(get_H1, ImportError):
        get_H1 = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW31B method get_H1: " + str(get_H1))
            )
        )
    else:
        get_H1 = get_H1
    # cf Methods.Slot.SlotW31B.get_H2
    if isinstance(get_H2, ImportError):
        get_H2 = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW31B method get_H2: " + str(get_H2))
            )
        )
    else:
        get_H2 = get_H2
    # cf Methods.Slot.SlotW31B.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotW31B.comp_surface_opening
    if isinstance(comp_surface_opening, ImportError):
        comp_surface_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method comp_surface_opening: "
                    + str(comp_surface_opening)
                )
            )
        )
    else:
        comp_surface_opening = comp_surface_opening
    # cf Methods.Slot.SlotW31B.get_surface_active
    if isinstance(get_surface_active, ImportError):
        get_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method get_surface_active: "
                    + str(get_surface_active)
                )
            )
        )
    else:
        get_surface_active = get_surface_active
    # cf Methods.Slot.SlotW31B.get_surface_opening
    if isinstance(get_surface_opening, ImportError):
        get_surface_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method get_surface_opening: "
                    + str(get_surface_opening)
                )
            )
        )
    else:
        get_surface_opening = get_surface_opening
    # cf Methods.Slot.SlotW31B.build_geometry_active
    if isinstance(build_geometry_active, ImportError):
        build_geometry_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method build_geometry_active: "
                    + str(build_geometry_active)
                )
            )
        )
    else:
        build_geometry_active = build_geometry_active
    # cf Methods.Slot.SlotW31B.get_wire_coordinate
    if isinstance(get_wire_coordinate, ImportError):
        get_wire_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method get_wire_coordinate: "
                    + str(get_wire_coordinate)
                )
            )
        )
    else:
        get_wire_coordinate = get_wire_coordinate
    # cf Methods.Slot.SlotW31B.get_wire_coordinateNew
    if isinstance(get_wire_coordinateNew, ImportError):
        get_wire_coordinateNew = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method get_wire_coordinateNew: "
                    + str(get_wire_coordinateNew)
                )
            )
        )
    else:
        get_wire_coordinateNew = get_wire_coordinateNew
    # cf Methods.Slot.SlotW31B.get_Wwire
    if isinstance(get_Wwire, ImportError):
        get_Wwire = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW31B method get_Wwire: " + str(get_Wwire))
            )
        )
    else:
        get_Wwire = get_Wwire
    # cf Methods.Slot.SlotW31B.get_dim_wind
    if isinstance(get_dim_wind, ImportError):
        get_dim_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method get_dim_wind: " + str(get_dim_wind)
                )
            )
        )
    else:
        get_dim_wind = get_dim_wind
    # cf Methods.Slot.SlotW31B.get_conductor
    if isinstance(get_conductor, ImportError):
        get_conductor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method get_conductor: " + str(get_conductor)
                )
            )
        )
    else:
        get_conductor = get_conductor
    # cf Methods.Slot.SlotW31B.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method plot_schematics: " + str(plot_schematics)
                )
            )
        )
    else:
        plot_schematics = plot_schematics
    # cf Methods.Slot.SlotW31B.plot_active
    if isinstance(plot_active, ImportError):
        plot_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW31B method plot_active: " + str(plot_active)
                )
            )
        )
    else:
        plot_active = plot_active
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        W0=0.0015,
        W1=0.004,
        W2=0.004,
        H0=0.001,
        H1=2.04,
        H2=1.5708,
        H3=0.002,
        H1_is_rad=True,
        H2_is_rad=True,
        i_bore=0.0004,
        i_tooth=0.0005,
        i_yoke=0.0006,
        i_tan=0.0005,
        i_rad=0.0005,
        Zs=36,
        wedge_mat=None,
        is_bore=True,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "H3" in list(init_dict.keys()):
                H3 = init_dict["H3"]
            if "H1_is_rad" in list(init_dict.keys()):
                H1_is_rad = init_dict["H1_is_rad"]
            if "H2_is_rad" in list(init_dict.keys()):
                H2_is_rad = init_dict["H2_is_rad"]
            if "i_bore" in list(init_dict.keys()):
                i_bore = init_dict["i_bore"]
            if "i_tooth" in list(init_dict.keys()):
                i_tooth = init_dict["i_tooth"]
            if "i_yoke" in list(init_dict.keys()):
                i_yoke = init_dict["i_yoke"]
            if "i_tan" in list(init_dict.keys()):
                i_tan = init_dict["i_tan"]
            if "i_rad" in list(init_dict.keys()):
                i_rad = init_dict["i_rad"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
            if "wedge_mat" in list(init_dict.keys()):
                wedge_mat = init_dict["wedge_mat"]
            if "is_bore" in list(init_dict.keys()):
                is_bore = init_dict["is_bore"]
        # Set the properties (value check and convertion are done in setter)
        self.W0 = W0
        self.W1 = W1
        self.W2 = W2
        self.H0 = H0
        self.H1 = H1
        self.H2 = H2
        self.H3 = H3
        self.H1_is_rad = H1_is_rad
        self.H2_is_rad = H2_is_rad
        self.i_bore = i_bore
        self.i_tooth = i_tooth
        self.i_yoke = i_yoke
        self.i_tan = i_tan
        self.i_rad = i_rad
        # Call Slot init
        super(SlotW31B, self).__init__(Zs=Zs, wedge_mat=wedge_mat, is_bore=is_bore)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotW31B_str = ""
        # Get the properties inherited from Slot
        SlotW31B_str += super(SlotW31B, self).__str__()
        SlotW31B_str += "W0 = " + str(self.W0) + linesep
        SlotW31B_str += "W1 = " + str(self.W1) + linesep
        SlotW31B_str += "W2 = " + str(self.W2) + linesep
        SlotW31B_str += "H0 = " + str(self.H0) + linesep
        SlotW31B_str += "H1 = " + str(self.H1) + linesep
        SlotW31B_str += "H2 = " + str(self.H2) + linesep
        SlotW31B_str += "H3 = " + str(self.H3) + linesep
        SlotW31B_str += "H1_is_rad = " + str(self.H1_is_rad) + linesep
        SlotW31B_str += "H2_is_rad = " + str(self.H2_is_rad) + linesep
        SlotW31B_str += "i_bore = " + str(self.i_bore) + linesep
        SlotW31B_str += "i_tooth = " + str(self.i_tooth) + linesep
        SlotW31B_str += "i_yoke = " + str(self.i_yoke) + linesep
        SlotW31B_str += "i_tan = " + str(self.i_tan) + linesep
        SlotW31B_str += "i_rad = " + str(self.i_rad) + linesep
        return SlotW31B_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotW31B, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.W1 != self.W1:
            return False
        if other.W2 != self.W2:
            return False
        if other.H0 != self.H0:
            return False
        if other.H1 != self.H1:
            return False
        if other.H2 != self.H2:
            return False
        if other.H3 != self.H3:
            return False
        if other.H1_is_rad != self.H1_is_rad:
            return False
        if other.H2_is_rad != self.H2_is_rad:
            return False
        if other.i_bore != self.i_bore:
            return False
        if other.i_tooth != self.i_tooth:
            return False
        if other.i_yoke != self.i_yoke:
            return False
        if other.i_tan != self.i_tan:
            return False
        if other.i_rad != self.i_rad:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Slot
        diff_list.extend(
            super(SlotW31B, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._W0 is not None
            and self._W0 is not None
            and isnan(other._W0)
            and isnan(self._W0)
        ):
            pass
        elif other._W0 != self._W0:
            if is_add_value:
                val_str = " (self=" + str(self._W0) + ", other=" + str(other._W0) + ")"
                diff_list.append(name + ".W0" + val_str)
            else:
                diff_list.append(name + ".W0")
        if (
            other._W1 is not None
            and self._W1 is not None
            and isnan(other._W1)
            and isnan(self._W1)
        ):
            pass
        elif other._W1 != self._W1:
            if is_add_value:
                val_str = " (self=" + str(self._W1) + ", other=" + str(other._W1) + ")"
                diff_list.append(name + ".W1" + val_str)
            else:
                diff_list.append(name + ".W1")
        if (
            other._W2 is not None
            and self._W2 is not None
            and isnan(other._W2)
            and isnan(self._W2)
        ):
            pass
        elif other._W2 != self._W2:
            if is_add_value:
                val_str = " (self=" + str(self._W2) + ", other=" + str(other._W2) + ")"
                diff_list.append(name + ".W2" + val_str)
            else:
                diff_list.append(name + ".W2")
        if (
            other._H0 is not None
            and self._H0 is not None
            and isnan(other._H0)
            and isnan(self._H0)
        ):
            pass
        elif other._H0 != self._H0:
            if is_add_value:
                val_str = " (self=" + str(self._H0) + ", other=" + str(other._H0) + ")"
                diff_list.append(name + ".H0" + val_str)
            else:
                diff_list.append(name + ".H0")
        if (
            other._H1 is not None
            and self._H1 is not None
            and isnan(other._H1)
            and isnan(self._H1)
        ):
            pass
        elif other._H1 != self._H1:
            if is_add_value:
                val_str = " (self=" + str(self._H1) + ", other=" + str(other._H1) + ")"
                diff_list.append(name + ".H1" + val_str)
            else:
                diff_list.append(name + ".H1")
        if (
            other._H2 is not None
            and self._H2 is not None
            and isnan(other._H2)
            and isnan(self._H2)
        ):
            pass
        elif other._H2 != self._H2:
            if is_add_value:
                val_str = " (self=" + str(self._H2) + ", other=" + str(other._H2) + ")"
                diff_list.append(name + ".H2" + val_str)
            else:
                diff_list.append(name + ".H2")
        if (
            other._H3 is not None
            and self._H3 is not None
            and isnan(other._H3)
            and isnan(self._H3)
        ):
            pass
        elif other._H3 != self._H3:
            if is_add_value:
                val_str = " (self=" + str(self._H3) + ", other=" + str(other._H3) + ")"
                diff_list.append(name + ".H3" + val_str)
            else:
                diff_list.append(name + ".H3")
        if other._H1_is_rad != self._H1_is_rad:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._H1_is_rad)
                    + ", other="
                    + str(other._H1_is_rad)
                    + ")"
                )
                diff_list.append(name + ".H1_is_rad" + val_str)
            else:
                diff_list.append(name + ".H1_is_rad")
        if other._H2_is_rad != self._H2_is_rad:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._H2_is_rad)
                    + ", other="
                    + str(other._H2_is_rad)
                    + ")"
                )
                diff_list.append(name + ".H2_is_rad" + val_str)
            else:
                diff_list.append(name + ".H2_is_rad")
        if (
            other._i_bore is not None
            and self._i_bore is not None
            and isnan(other._i_bore)
            and isnan(self._i_bore)
        ):
            pass
        elif other._i_bore != self._i_bore:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._i_bore)
                    + ", other="
                    + str(other._i_bore)
                    + ")"
                )
                diff_list.append(name + ".i_bore" + val_str)
            else:
                diff_list.append(name + ".i_bore")
        if (
            other._i_tooth is not None
            and self._i_tooth is not None
            and isnan(other._i_tooth)
            and isnan(self._i_tooth)
        ):
            pass
        elif other._i_tooth != self._i_tooth:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._i_tooth)
                    + ", other="
                    + str(other._i_tooth)
                    + ")"
                )
                diff_list.append(name + ".i_tooth" + val_str)
            else:
                diff_list.append(name + ".i_tooth")
        if (
            other._i_yoke is not None
            and self._i_yoke is not None
            and isnan(other._i_yoke)
            and isnan(self._i_yoke)
        ):
            pass
        elif other._i_yoke != self._i_yoke:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._i_yoke)
                    + ", other="
                    + str(other._i_yoke)
                    + ")"
                )
                diff_list.append(name + ".i_yoke" + val_str)
            else:
                diff_list.append(name + ".i_yoke")
        if (
            other._i_tan is not None
            and self._i_tan is not None
            and isnan(other._i_tan)
            and isnan(self._i_tan)
        ):
            pass
        elif other._i_tan != self._i_tan:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._i_tan) + ", other=" + str(other._i_tan) + ")"
                )
                diff_list.append(name + ".i_tan" + val_str)
            else:
                diff_list.append(name + ".i_tan")
        if (
            other._i_rad is not None
            and self._i_rad is not None
            and isnan(other._i_rad)
            and isnan(self._i_rad)
        ):
            pass
        elif other._i_rad != self._i_rad:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._i_rad) + ", other=" + str(other._i_rad) + ")"
                )
                diff_list.append(name + ".i_rad" + val_str)
            else:
                diff_list.append(name + ".i_rad")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Slot
        S += super(SlotW31B, self).__sizeof__()
        S += getsizeof(self.W0)
        S += getsizeof(self.W1)
        S += getsizeof(self.W2)
        S += getsizeof(self.H0)
        S += getsizeof(self.H1)
        S += getsizeof(self.H2)
        S += getsizeof(self.H3)
        S += getsizeof(self.H1_is_rad)
        S += getsizeof(self.H2_is_rad)
        S += getsizeof(self.i_bore)
        S += getsizeof(self.i_tooth)
        S += getsizeof(self.i_yoke)
        S += getsizeof(self.i_tan)
        S += getsizeof(self.i_rad)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Slot
        SlotW31B_dict = super(SlotW31B, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        SlotW31B_dict["W0"] = self.W0
        SlotW31B_dict["W1"] = self.W1
        SlotW31B_dict["W2"] = self.W2
        SlotW31B_dict["H0"] = self.H0
        SlotW31B_dict["H1"] = self.H1
        SlotW31B_dict["H2"] = self.H2
        SlotW31B_dict["H3"] = self.H3
        SlotW31B_dict["H1_is_rad"] = self.H1_is_rad
        SlotW31B_dict["H2_is_rad"] = self.H2_is_rad
        SlotW31B_dict["i_bore"] = self.i_bore
        SlotW31B_dict["i_tooth"] = self.i_tooth
        SlotW31B_dict["i_yoke"] = self.i_yoke
        SlotW31B_dict["i_tan"] = self.i_tan
        SlotW31B_dict["i_rad"] = self.i_rad
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotW31B_dict["__class__"] = "SlotW31B"
        return SlotW31B_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        W0_val = self.W0
        W1_val = self.W1
        W2_val = self.W2
        H0_val = self.H0
        H1_val = self.H1
        H2_val = self.H2
        H3_val = self.H3
        H1_is_rad_val = self.H1_is_rad
        H2_is_rad_val = self.H2_is_rad
        i_bore_val = self.i_bore
        i_tooth_val = self.i_tooth
        i_yoke_val = self.i_yoke
        i_tan_val = self.i_tan
        i_rad_val = self.i_rad
        Zs_val = self.Zs
        if self.wedge_mat is None:
            wedge_mat_val = None
        else:
            wedge_mat_val = self.wedge_mat.copy()
        is_bore_val = self.is_bore
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            W0=W0_val,
            W1=W1_val,
            W2=W2_val,
            H0=H0_val,
            H1=H1_val,
            H2=H2_val,
            H3=H3_val,
            H1_is_rad=H1_is_rad_val,
            H2_is_rad=H2_is_rad_val,
            i_bore=i_bore_val,
            i_tooth=i_tooth_val,
            i_yoke=i_yoke_val,
            i_tan=i_tan_val,
            i_rad=i_rad_val,
            Zs=Zs_val,
            wedge_mat=wedge_mat_val,
            is_bore=is_bore_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.W1 = None
        self.W2 = None
        self.H0 = None
        self.H1 = None
        self.H2 = None
        self.H3 = None
        self.H1_is_rad = None
        self.H2_is_rad = None
        self.i_bore = None
        self.i_tooth = None
        self.i_yoke = None
        self.i_tan = None
        self.i_rad = None
        # Set to None the properties inherited from Slot
        super(SlotW31B, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    W0 = property(
        fget=_get_W0,
        fset=_set_W0,
        doc="""Slot opening.

        :Type: float
        :min: 0
        """,
    )

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0)
        self._W1 = value

    W1 = property(
        fget=_get_W1,
        fset=_set_W1,
        doc="""Slot tooth thickness.

        :Type: float
        :min: 0
        """,
    )

    def _get_W2(self):
        """getter of W2"""
        return self._W2

    def _set_W2(self, value):
        """setter of W2"""
        check_var("W2", value, "float", Vmin=0)
        self._W2 = value

    W2 = property(
        fget=_get_W2,
        fset=_set_W2,
        doc="""Slot back width.

        :Type: float
        :min: 0
        """,
    )

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    H0 = property(
        fget=_get_H0,
        fset=_set_H0,
        doc="""Slot tip height.

        :Type: float
        :min: 0
        """,
    )

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    H1 = property(
        fget=_get_H1,
        fset=_set_H1,
        doc="""Slot height or angle  (See Schematics)

        :Type: float
        :min: 0
        """,
    )

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    H2 = property(
        fget=_get_H2,
        fset=_set_H2,
        doc="""Slot back height or angle  (See Schematics)

        :Type: float
        :min: 0
        """,
    )

    def _get_H3(self):
        """getter of H3"""
        return self._H3

    def _set_H3(self, value):
        """setter of H3"""
        check_var("H3", value, "float", Vmin=0)
        self._H3 = value

    H3 = property(
        fget=_get_H3,
        fset=_set_H3,
        doc="""Slot yoke thickness.

        :Type: float
        :min: 0
        """,
    )

    def _get_H1_is_rad(self):
        """getter of H1_is_rad"""
        return self._H1_is_rad

    def _set_H1_is_rad(self, value):
        """setter of H1_is_rad"""
        check_var("H1_is_rad", value, "bool")
        self._H1_is_rad = value

    H1_is_rad = property(
        fget=_get_H1_is_rad,
        fset=_set_H1_is_rad,
        doc="""H1 unit, 0 for m, 1 for rad

        :Type: bool
        """,
    )

    def _get_H2_is_rad(self):
        """getter of H2_is_rad"""
        return self._H2_is_rad

    def _set_H2_is_rad(self, value):
        """setter of H2_is_rad"""
        check_var("H2_is_rad", value, "bool")
        self._H2_is_rad = value

    H2_is_rad = property(
        fget=_get_H2_is_rad,
        fset=_set_H2_is_rad,
        doc="""H2 unit, 0 for m, 1 for rad

        :Type: bool
        """,
    )

    def _get_i_bore(self):
        """getter of i_bore"""
        return self._i_bore

    def _set_i_bore(self, value):
        """setter of i_bore"""
        check_var("i_bore", value, "float", Vmin=0)
        self._i_bore = value

    i_bore = property(
        fget=_get_i_bore,
        fset=_set_i_bore,
        doc="""Slot bore isolation thickness.

        :Type: float
        :min: 0
        """,
    )

    def _get_i_tooth(self):
        """getter of i_tooth"""
        return self._i_tooth

    def _set_i_tooth(self, value):
        """setter of i_tooth"""
        check_var("i_tooth", value, "float", Vmin=0)
        self._i_tooth = value

    i_tooth = property(
        fget=_get_i_tooth,
        fset=_set_i_tooth,
        doc="""Slot tooth isolation thickness.

        :Type: float
        :min: 0
        """,
    )

    def _get_i_yoke(self):
        """getter of i_yoke"""
        return self._i_yoke

    def _set_i_yoke(self, value):
        """setter of i_yoke"""
        check_var("i_yoke", value, "float", Vmin=0)
        self._i_yoke = value

    i_yoke = property(
        fget=_get_i_yoke,
        fset=_set_i_yoke,
        doc="""Slot yoke isolation thickness.

        :Type: float
        :min: 0
        """,
    )

    def _get_i_tan(self):
        """getter of i_tan"""
        return self._i_tan

    def _set_i_tan(self, value):
        """setter of i_tan"""
        check_var("i_tan", value, "float", Vmin=0)
        self._i_tan = value

    i_tan = property(
        fget=_get_i_tan,
        fset=_set_i_tan,
        doc="""Slot isolation between tangential layers.

        :Type: float
        :min: 0
        """,
    )

    def _get_i_rad(self):
        """getter of i_rad"""
        return self._i_rad

    def _set_i_rad(self, value):
        """setter of i_rad"""
        check_var("i_rad", value, "float", Vmin=0)
        self._i_rad = value

    i_rad = property(
        fget=_get_i_rad,
        fset=_set_i_rad,
        doc="""Slot isolation between radial layers.

        :Type: float
        :min: 0
        """,
    )
