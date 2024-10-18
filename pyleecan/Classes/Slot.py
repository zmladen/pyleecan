# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/Slot.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/Slot
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.Slot.build_geometry_active import build_geometry_active
except ImportError as error:
    build_geometry_active = error

try:
    from ..Methods.Slot.Slot.build_geometry_half_tooth import build_geometry_half_tooth
except ImportError as error:
    build_geometry_half_tooth = error

try:
    from ..Methods.Slot.Slot.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.Slot.comp_angle_active_eq import comp_angle_active_eq
except ImportError as error:
    comp_angle_active_eq = error

try:
    from ..Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.Slot.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.Slot.comp_height_active import comp_height_active
except ImportError as error:
    comp_height_active = error

try:
    from ..Methods.Slot.Slot.comp_height_opening import comp_height_opening
except ImportError as error:
    comp_height_opening = error

try:
    from ..Methods.Slot.Slot.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Slot.Slot.comp_radius_mid_active import comp_radius_mid_active
except ImportError as error:
    comp_radius_mid_active = error

try:
    from ..Methods.Slot.Slot.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.Slot.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Slot.Slot.comp_surface_opening import comp_surface_opening
except ImportError as error:
    comp_surface_opening = error

try:
    from ..Methods.Slot.Slot.comp_surface_wedges import comp_surface_wedges
except ImportError as error:
    comp_surface_wedges = error

try:
    from ..Methods.Slot.Slot.comp_width import comp_width
except ImportError as error:
    comp_width = error

try:
    from ..Methods.Slot.Slot.comp_width_opening import comp_width_opening
except ImportError as error:
    comp_width_opening = error

try:
    from ..Methods.Slot.Slot.convert_to_SlotUD2 import convert_to_SlotUD2
except ImportError as error:
    convert_to_SlotUD2 = error

try:
    from ..Methods.Slot.Slot.get_is_stator import get_is_stator
except ImportError as error:
    get_is_stator = error

try:
    from ..Methods.Slot.Slot.get_name_lam import get_name_lam
except ImportError as error:
    get_name_lam = error

try:
    from ..Methods.Slot.Slot.get_Rbo import get_Rbo
except ImportError as error:
    get_Rbo = error

try:
    from ..Methods.Slot.Slot.get_Ryoke import get_Ryoke
except ImportError as error:
    get_Ryoke = error

try:
    from ..Methods.Slot.Slot.get_surface import get_surface
except ImportError as error:
    get_surface = error

try:
    from ..Methods.Slot.Slot.get_surface_tooth import get_surface_tooth
except ImportError as error:
    get_surface_tooth = error

try:
    from ..Methods.Slot.Slot.get_surface_wedges import get_surface_wedges
except ImportError as error:
    get_surface_wedges = error

try:
    from ..Methods.Slot.Slot.is_outwards import is_outwards
except ImportError as error:
    is_outwards = error

try:
    from ..Methods.Slot.Slot.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Slot.Slot.plot_active import plot_active
except ImportError as error:
    plot_active = error

try:
    from ..Methods.Slot.Slot.set_label import set_label
except ImportError as error:
    set_label = error

try:
    from ..Methods.Slot.Slot.is_airgap_active import is_airgap_active
except ImportError as error:
    is_airgap_active = error

try:
    from ..Methods.Slot.Slot.is_full_pitch_active import is_full_pitch_active
except ImportError as error:
    is_full_pitch_active = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Slot(FrozenClass):
    """Generic class for slot (abstract)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.Slot.build_geometry_active
    if isinstance(build_geometry_active, ImportError):
        build_geometry_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method build_geometry_active: "
                    + str(build_geometry_active)
                )
            )
        )
    else:
        build_geometry_active = build_geometry_active
    # cf Methods.Slot.Slot.build_geometry_half_tooth
    if isinstance(build_geometry_half_tooth, ImportError):
        build_geometry_half_tooth = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method build_geometry_half_tooth: "
                    + str(build_geometry_half_tooth)
                )
            )
        )
    else:
        build_geometry_half_tooth = build_geometry_half_tooth
    # cf Methods.Slot.Slot.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.Slot.comp_angle_active_eq
    if isinstance(comp_angle_active_eq, ImportError):
        comp_angle_active_eq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_angle_active_eq: "
                    + str(comp_angle_active_eq)
                )
            )
        )
    else:
        comp_angle_active_eq = comp_angle_active_eq
    # cf Methods.Slot.Slot.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.Slot.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.Slot.comp_height_active
    if isinstance(comp_height_active, ImportError):
        comp_height_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_height_active: "
                    + str(comp_height_active)
                )
            )
        )
    else:
        comp_height_active = comp_height_active
    # cf Methods.Slot.Slot.comp_height_opening
    if isinstance(comp_height_opening, ImportError):
        comp_height_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_height_opening: "
                    + str(comp_height_opening)
                )
            )
        )
    else:
        comp_height_opening = comp_height_opening
    # cf Methods.Slot.Slot.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method comp_radius: " + str(comp_radius))
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.Slot.comp_radius_mid_active
    if isinstance(comp_radius_mid_active, ImportError):
        comp_radius_mid_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_radius_mid_active: "
                    + str(comp_radius_mid_active)
                )
            )
        )
    else:
        comp_radius_mid_active = comp_radius_mid_active
    # cf Methods.Slot.Slot.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method comp_surface: " + str(comp_surface))
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.Slot.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Slot.Slot.comp_surface_opening
    if isinstance(comp_surface_opening, ImportError):
        comp_surface_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_surface_opening: "
                    + str(comp_surface_opening)
                )
            )
        )
    else:
        comp_surface_opening = comp_surface_opening
    # cf Methods.Slot.Slot.comp_surface_wedges
    if isinstance(comp_surface_wedges, ImportError):
        comp_surface_wedges = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_surface_wedges: "
                    + str(comp_surface_wedges)
                )
            )
        )
    else:
        comp_surface_wedges = comp_surface_wedges
    # cf Methods.Slot.Slot.comp_width
    if isinstance(comp_width, ImportError):
        comp_width = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method comp_width: " + str(comp_width))
            )
        )
    else:
        comp_width = comp_width
    # cf Methods.Slot.Slot.comp_width_opening
    if isinstance(comp_width_opening, ImportError):
        comp_width_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method comp_width_opening: "
                    + str(comp_width_opening)
                )
            )
        )
    else:
        comp_width_opening = comp_width_opening
    # cf Methods.Slot.Slot.convert_to_SlotUD2
    if isinstance(convert_to_SlotUD2, ImportError):
        convert_to_SlotUD2 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method convert_to_SlotUD2: "
                    + str(convert_to_SlotUD2)
                )
            )
        )
    else:
        convert_to_SlotUD2 = convert_to_SlotUD2
    # cf Methods.Slot.Slot.get_is_stator
    if isinstance(get_is_stator, ImportError):
        get_is_stator = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method get_is_stator: " + str(get_is_stator)
                )
            )
        )
    else:
        get_is_stator = get_is_stator
    # cf Methods.Slot.Slot.get_name_lam
    if isinstance(get_name_lam, ImportError):
        get_name_lam = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method get_name_lam: " + str(get_name_lam))
            )
        )
    else:
        get_name_lam = get_name_lam
    # cf Methods.Slot.Slot.get_Rbo
    if isinstance(get_Rbo, ImportError):
        get_Rbo = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method get_Rbo: " + str(get_Rbo))
            )
        )
    else:
        get_Rbo = get_Rbo
    # cf Methods.Slot.Slot.get_Ryoke
    if isinstance(get_Ryoke, ImportError):
        get_Ryoke = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method get_Ryoke: " + str(get_Ryoke))
            )
        )
    else:
        get_Ryoke = get_Ryoke
    # cf Methods.Slot.Slot.get_surface
    if isinstance(get_surface, ImportError):
        get_surface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method get_surface: " + str(get_surface))
            )
        )
    else:
        get_surface = get_surface
    # cf Methods.Slot.Slot.get_surface_tooth
    if isinstance(get_surface_tooth, ImportError):
        get_surface_tooth = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method get_surface_tooth: " + str(get_surface_tooth)
                )
            )
        )
    else:
        get_surface_tooth = get_surface_tooth
    # cf Methods.Slot.Slot.get_surface_wedges
    if isinstance(get_surface_wedges, ImportError):
        get_surface_wedges = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method get_surface_wedges: "
                    + str(get_surface_wedges)
                )
            )
        )
    else:
        get_surface_wedges = get_surface_wedges
    # cf Methods.Slot.Slot.is_outwards
    if isinstance(is_outwards, ImportError):
        is_outwards = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method is_outwards: " + str(is_outwards))
            )
        )
    else:
        is_outwards = is_outwards
    # cf Methods.Slot.Slot.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Slot.Slot.plot_active
    if isinstance(plot_active, ImportError):
        plot_active = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method plot_active: " + str(plot_active))
            )
        )
    else:
        plot_active = plot_active
    # cf Methods.Slot.Slot.set_label
    if isinstance(set_label, ImportError):
        set_label = property(
            fget=lambda x: raise_(
                ImportError("Can't use Slot method set_label: " + str(set_label))
            )
        )
    else:
        set_label = set_label
    # cf Methods.Slot.Slot.is_airgap_active
    if isinstance(is_airgap_active, ImportError):
        is_airgap_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method is_airgap_active: " + str(is_airgap_active)
                )
            )
        )
    else:
        is_airgap_active = is_airgap_active
    # cf Methods.Slot.Slot.is_full_pitch_active
    if isinstance(is_full_pitch_active, ImportError):
        is_full_pitch_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Slot method is_full_pitch_active: "
                    + str(is_full_pitch_active)
                )
            )
        )
    else:
        is_full_pitch_active = is_full_pitch_active
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, Zs=36, wedge_mat=None, is_bore=True, init_dict=None, init_str=None
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
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
            if "wedge_mat" in list(init_dict.keys()):
                wedge_mat = init_dict["wedge_mat"]
            if "is_bore" in list(init_dict.keys()):
                is_bore = init_dict["is_bore"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Zs = Zs
        self.wedge_mat = wedge_mat
        self.is_bore = is_bore

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Slot_str = ""
        if self.parent is None:
            Slot_str += "parent = None " + linesep
        else:
            Slot_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Slot_str += "Zs = " + str(self.Zs) + linesep
        if self.wedge_mat is not None:
            tmp = self.wedge_mat.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Slot_str += "wedge_mat = " + tmp
        else:
            Slot_str += "wedge_mat = None" + linesep + linesep
        Slot_str += "is_bore = " + str(self.is_bore) + linesep
        return Slot_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Zs != self.Zs:
            return False
        if other.wedge_mat != self.wedge_mat:
            return False
        if other.is_bore != self.is_bore:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._Zs != self._Zs:
            if is_add_value:
                val_str = " (self=" + str(self._Zs) + ", other=" + str(other._Zs) + ")"
                diff_list.append(name + ".Zs" + val_str)
            else:
                diff_list.append(name + ".Zs")
        if (other.wedge_mat is None and self.wedge_mat is not None) or (
            other.wedge_mat is not None and self.wedge_mat is None
        ):
            diff_list.append(name + ".wedge_mat None mismatch")
        elif self.wedge_mat is not None:
            diff_list.extend(
                self.wedge_mat.compare(
                    other.wedge_mat,
                    name=name + ".wedge_mat",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._is_bore != self._is_bore:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_bore)
                    + ", other="
                    + str(other._is_bore)
                    + ")"
                )
                diff_list.append(name + ".is_bore" + val_str)
            else:
                diff_list.append(name + ".is_bore")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.Zs)
        S += getsizeof(self.wedge_mat)
        S += getsizeof(self.is_bore)
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

        Slot_dict = dict()
        Slot_dict["Zs"] = self.Zs
        if self.wedge_mat is None:
            Slot_dict["wedge_mat"] = None
        else:
            Slot_dict["wedge_mat"] = self.wedge_mat.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Slot_dict["is_bore"] = self.is_bore
        # The class name is added to the dict for deserialisation purpose
        Slot_dict["__class__"] = "Slot"
        return Slot_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        Zs_val = self.Zs
        if self.wedge_mat is None:
            wedge_mat_val = None
        else:
            wedge_mat_val = self.wedge_mat.copy()
        is_bore_val = self.is_bore
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(Zs=Zs_val, wedge_mat=wedge_mat_val, is_bore=is_bore_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Zs = None
        if self.wedge_mat is not None:
            self.wedge_mat._set_None()
        self.is_bore = None

    def _get_Zs(self):
        """getter of Zs"""
        return self._Zs

    def _set_Zs(self, value):
        """setter of Zs"""
        check_var("Zs", value, "int", Vmin=0)
        self._Zs = value

    Zs = property(
        fget=_get_Zs,
        fset=_set_Zs,
        doc="""slot number

        :Type: int
        :min: 0
        """,
    )

    def _get_wedge_mat(self):
        """getter of wedge_mat"""
        return self._wedge_mat

    def _set_wedge_mat(self, value):
        """setter of wedge_mat"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "wedge_mat"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Material = import_class("pyleecan.Classes", "Material", "wedge_mat")
            value = Material()
        check_var("wedge_mat", value, "Material")
        self._wedge_mat = value

        if self._wedge_mat is not None:
            self._wedge_mat.parent = self

    wedge_mat = property(
        fget=_get_wedge_mat,
        fset=_set_wedge_mat,
        doc="""Material for the wedge, if None no wedge

        :Type: Material
        """,
    )

    def _get_is_bore(self):
        """getter of is_bore"""
        return self._is_bore

    def _set_is_bore(self, value):
        """setter of is_bore"""
        check_var("is_bore", value, "bool")
        self._is_bore = value

    is_bore = property(
        fget=_get_is_bore,
        fset=_set_is_bore,
        doc="""True if the Slot is on the bore radius, False for yoke

        :Type: bool
        """,
    )
