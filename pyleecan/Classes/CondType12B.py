# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/CondType12B.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/CondType12B
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
from .Conductor import Conductor

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.CondType12B.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.CondType12B.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Machine.CondType12B.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Machine.CondType12B.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Machine.CondType12B.comp_width import comp_width
except ImportError as error:
    comp_width = error

try:
    from ..Methods.Machine.CondType12B.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.CondType12B.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error

try:
    from ..Methods.Machine.CondType12B.comp_width_wire import comp_width_wire
except ImportError as error:
    comp_width_wire = error

try:
    from ..Methods.Machine.CondType12B.comp_height_wire import comp_height_wire
except ImportError as error:
    comp_height_wire = error

try:
    from ..Methods.Machine.CondType12B.comp_nb_circumferential_wire import (
        comp_nb_circumferential_wire,
    )
except ImportError as error:
    comp_nb_circumferential_wire = error

try:
    from ..Methods.Machine.CondType12B.comp_nb_radial_wire import comp_nb_radial_wire
except ImportError as error:
    comp_nb_radial_wire = error

try:
    from ..Methods.Machine.CondType12B.is_round_wire import is_round_wire
except ImportError as error:
    is_round_wire = error


from numpy import isnan
from ._check import InitUnKnowClassError


class CondType12B(Conductor):
    """parallel stranded conductor consisting of at least a single round wire"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.CondType12B.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use CondType12B method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.CondType12B.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Machine.CondType12B.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Machine.CondType12B.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.CondType12B.comp_width
    if isinstance(comp_width, ImportError):
        comp_width = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method comp_width: " + str(comp_width)
                )
            )
        )
    else:
        comp_width = comp_width
    # cf Methods.Machine.CondType12B.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use CondType12B method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.CondType12B.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method plot_schematics: "
                    + str(plot_schematics)
                )
            )
        )
    else:
        plot_schematics = plot_schematics
    # cf Methods.Machine.CondType12B.comp_width_wire
    if isinstance(comp_width_wire, ImportError):
        comp_width_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method comp_width_wire: "
                    + str(comp_width_wire)
                )
            )
        )
    else:
        comp_width_wire = comp_width_wire
    # cf Methods.Machine.CondType12B.comp_height_wire
    if isinstance(comp_height_wire, ImportError):
        comp_height_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method comp_height_wire: "
                    + str(comp_height_wire)
                )
            )
        )
    else:
        comp_height_wire = comp_height_wire
    # cf Methods.Machine.CondType12B.comp_nb_circumferential_wire
    if isinstance(comp_nb_circumferential_wire, ImportError):
        comp_nb_circumferential_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method comp_nb_circumferential_wire: "
                    + str(comp_nb_circumferential_wire)
                )
            )
        )
    else:
        comp_nb_circumferential_wire = comp_nb_circumferential_wire
    # cf Methods.Machine.CondType12B.comp_nb_radial_wire
    if isinstance(comp_nb_radial_wire, ImportError):
        comp_nb_radial_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method comp_nb_radial_wire: "
                    + str(comp_nb_radial_wire)
                )
            )
        )
    else:
        comp_nb_radial_wire = comp_nb_radial_wire
    # cf Methods.Machine.CondType12B.is_round_wire
    if isinstance(is_round_wire, ImportError):
        is_round_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType12B method is_round_wire: " + str(is_round_wire)
                )
            )
        )
    else:
        is_round_wire = is_round_wire
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Wwire=0.015,
        Wins_cond=None,
        Nwppc=1,
        Wins_wire=0,
        Kwoh=0.5,
        origin=0,
        cond_mat=-1,
        ins_mat=-1,
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
            if "Wwire" in list(init_dict.keys()):
                Wwire = init_dict["Wwire"]
            if "Wins_cond" in list(init_dict.keys()):
                Wins_cond = init_dict["Wins_cond"]
            if "Nwppc" in list(init_dict.keys()):
                Nwppc = init_dict["Nwppc"]
            if "Wins_wire" in list(init_dict.keys()):
                Wins_wire = init_dict["Wins_wire"]
            if "Kwoh" in list(init_dict.keys()):
                Kwoh = init_dict["Kwoh"]
            if "origin" in list(init_dict.keys()):
                origin = init_dict["origin"]
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.Wwire = Wwire
        self.Wins_cond = Wins_cond
        self.Nwppc = Nwppc
        self.Wins_wire = Wins_wire
        self.Kwoh = Kwoh
        self.origin = origin
        # Call Conductor init
        super(CondType12B, self).__init__(cond_mat=cond_mat, ins_mat=ins_mat)
        # The class is frozen (in Conductor init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        CondType12B_str = ""
        # Get the properties inherited from Conductor
        CondType12B_str += super(CondType12B, self).__str__()
        CondType12B_str += "Wwire = " + str(self.Wwire) + linesep
        CondType12B_str += "Wins_cond = " + str(self.Wins_cond) + linesep
        CondType12B_str += "Nwppc = " + str(self.Nwppc) + linesep
        CondType12B_str += "Wins_wire = " + str(self.Wins_wire) + linesep
        CondType12B_str += "Kwoh = " + str(self.Kwoh) + linesep
        CondType12B_str += "origin = " + str(self.origin) + linesep
        return CondType12B_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Conductor
        if not super(CondType12B, self).__eq__(other):
            return False
        if other.Wwire != self.Wwire:
            return False
        if other.Wins_cond != self.Wins_cond:
            return False
        if other.Nwppc != self.Nwppc:
            return False
        if other.Wins_wire != self.Wins_wire:
            return False
        if other.Kwoh != self.Kwoh:
            return False
        if other.origin != self.origin:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Conductor
        diff_list.extend(
            super(CondType12B, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._Wwire is not None
            and self._Wwire is not None
            and isnan(other._Wwire)
            and isnan(self._Wwire)
        ):
            pass
        elif other._Wwire != self._Wwire:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Wwire) + ", other=" + str(other._Wwire) + ")"
                )
                diff_list.append(name + ".Wwire" + val_str)
            else:
                diff_list.append(name + ".Wwire")
        if (
            other._Wins_cond is not None
            and self._Wins_cond is not None
            and isnan(other._Wins_cond)
            and isnan(self._Wins_cond)
        ):
            pass
        elif other._Wins_cond != self._Wins_cond:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Wins_cond)
                    + ", other="
                    + str(other._Wins_cond)
                    + ")"
                )
                diff_list.append(name + ".Wins_cond" + val_str)
            else:
                diff_list.append(name + ".Wins_cond")
        if other._Nwppc != self._Nwppc:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Nwppc) + ", other=" + str(other._Nwppc) + ")"
                )
                diff_list.append(name + ".Nwppc" + val_str)
            else:
                diff_list.append(name + ".Nwppc")
        if (
            other._Wins_wire is not None
            and self._Wins_wire is not None
            and isnan(other._Wins_wire)
            and isnan(self._Wins_wire)
        ):
            pass
        elif other._Wins_wire != self._Wins_wire:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Wins_wire)
                    + ", other="
                    + str(other._Wins_wire)
                    + ")"
                )
                diff_list.append(name + ".Wins_wire" + val_str)
            else:
                diff_list.append(name + ".Wins_wire")
        if (
            other._Kwoh is not None
            and self._Kwoh is not None
            and isnan(other._Kwoh)
            and isnan(self._Kwoh)
        ):
            pass
        elif other._Kwoh != self._Kwoh:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Kwoh) + ", other=" + str(other._Kwoh) + ")"
                )
                diff_list.append(name + ".Kwoh" + val_str)
            else:
                diff_list.append(name + ".Kwoh")
        if other._origin != self._origin:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._origin)
                    + ", other="
                    + str(other._origin)
                    + ")"
                )
                diff_list.append(name + ".origin" + val_str)
            else:
                diff_list.append(name + ".origin")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Conductor
        S += super(CondType12B, self).__sizeof__()
        S += getsizeof(self.Wwire)
        S += getsizeof(self.Wins_cond)
        S += getsizeof(self.Nwppc)
        S += getsizeof(self.Wins_wire)
        S += getsizeof(self.Kwoh)
        S += getsizeof(self.origin)
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

        # Get the properties inherited from Conductor
        CondType12B_dict = super(CondType12B, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        CondType12B_dict["Wwire"] = self.Wwire
        CondType12B_dict["Wins_cond"] = self.Wins_cond
        CondType12B_dict["Nwppc"] = self.Nwppc
        CondType12B_dict["Wins_wire"] = self.Wins_wire
        CondType12B_dict["Kwoh"] = self.Kwoh
        if self.origin is None:
            CondType12B_dict["origin"] = None
        elif isinstance(self.origin, float):
            CondType12B_dict["origin"] = self.origin
        else:
            CondType12B_dict["origin"] = str(self.origin)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        CondType12B_dict["__class__"] = "CondType12B"
        return CondType12B_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        Wwire_val = self.Wwire
        Wins_cond_val = self.Wins_cond
        Nwppc_val = self.Nwppc
        Wins_wire_val = self.Wins_wire
        Kwoh_val = self.Kwoh
        origin_val = self.origin
        if self.cond_mat is None:
            cond_mat_val = None
        else:
            cond_mat_val = self.cond_mat.copy()
        if self.ins_mat is None:
            ins_mat_val = None
        else:
            ins_mat_val = self.ins_mat.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            Wwire=Wwire_val,
            Wins_cond=Wins_cond_val,
            Nwppc=Nwppc_val,
            Wins_wire=Wins_wire_val,
            Kwoh=Kwoh_val,
            origin=origin_val,
            cond_mat=cond_mat_val,
            ins_mat=ins_mat_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Wwire = None
        self.Wins_cond = None
        self.Nwppc = None
        self.Wins_wire = None
        self.Kwoh = None
        self.origin = None
        # Set to None the properties inherited from Conductor
        super(CondType12B, self)._set_None()

    def _get_Wwire(self):
        """getter of Wwire"""
        return self._Wwire

    def _set_Wwire(self, value):
        """setter of Wwire"""
        check_var("Wwire", value, "float", Vmin=0)
        self._Wwire = value

    Wwire = property(
        fget=_get_Wwire,
        fset=_set_Wwire,
        doc="""cf schematics, single strand diameter without insulation

        :Type: float
        :min: 0
        """,
    )

    def _get_Wins_cond(self):
        """getter of Wins_cond"""
        return self._Wins_cond

    def _set_Wins_cond(self, value):
        """setter of Wins_cond"""
        check_var("Wins_cond", value, "float", Vmin=0)
        self._Wins_cond = value

    Wins_cond = property(
        fget=_get_Wins_cond,
        fset=_set_Wins_cond,
        doc="""(advanced) cf schematics, conductor diameter

        :Type: float
        :min: 0
        """,
    )

    def _get_Nwppc(self):
        """getter of Nwppc"""
        return self._Nwppc

    def _set_Nwppc(self, value):
        """setter of Nwppc"""
        check_var("Nwppc", value, "int", Vmin=1)
        self._Nwppc = value

    Nwppc = property(
        fget=_get_Nwppc,
        fset=_set_Nwppc,
        doc="""number of strands in parallel per conductor

        :Type: int
        :min: 1
        """,
    )

    def _get_Wins_wire(self):
        """getter of Wins_wire"""
        return self._Wins_wire

    def _set_Wins_wire(self, value):
        """setter of Wins_wire"""
        check_var("Wins_wire", value, "float", Vmin=0)
        self._Wins_wire = value

    Wins_wire = property(
        fget=_get_Wins_wire,
        fset=_set_Wins_wire,
        doc="""(advanced) cf schematics, winding strand insulation thickness

        :Type: float
        :min: 0
        """,
    )

    def _get_Kwoh(self):
        """getter of Kwoh"""
        return self._Kwoh

    def _set_Kwoh(self, value):
        """setter of Kwoh"""
        check_var("Kwoh", value, "float", Vmin=0)
        self._Kwoh = value

    Kwoh = property(
        fget=_get_Kwoh,
        fset=_set_Kwoh,
        doc="""winding overhang factor which describes the fact that random round wire end-windings can be more or less compressed (0.5 for small motors, 0.8 for large motors) - can be used to tune the average turn length (relevant if type_cond==1)

        :Type: float
        :min: 0
        """,
    )

    def _get_origin(self):
        """getter of origin"""
        return self._origin

    def _set_origin(self, value):
        """setter of origin"""
        if isinstance(value, str):
            value = complex(value)
        check_var("origin", value, "complex")
        self._origin = value

    origin = property(
        fget=_get_origin,
        fset=_set_origin,
        doc="""origin point of the conductor

        :Type: complex
        """,
    )
