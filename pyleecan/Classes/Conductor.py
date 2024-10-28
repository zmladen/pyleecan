# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Conductor.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Conductor
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
    from ..Methods.Machine.Conductor.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.Conductor.comp_skin_effect_resistance import (
        comp_skin_effect_resistance,
    )
except ImportError as error:
    comp_skin_effect_resistance = error

try:
    from ..Methods.Machine.Conductor.comp_skin_effect_inductance import (
        comp_skin_effect_inductance,
    )
except ImportError as error:
    comp_skin_effect_inductance = error

try:
    from ..Methods.Machine.Conductor.comp_temperature_effect import (
        comp_temperature_effect,
    )
except ImportError as error:
    comp_temperature_effect = error

try:
    from ..Methods.Machine.Conductor.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Conductor(FrozenClass):
    """abstact class for conductors"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Conductor.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Conductor method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.Conductor.comp_skin_effect_resistance
    if isinstance(comp_skin_effect_resistance, ImportError):
        comp_skin_effect_resistance = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Conductor method comp_skin_effect_resistance: "
                    + str(comp_skin_effect_resistance)
                )
            )
        )
    else:
        comp_skin_effect_resistance = comp_skin_effect_resistance
    # cf Methods.Machine.Conductor.comp_skin_effect_inductance
    if isinstance(comp_skin_effect_inductance, ImportError):
        comp_skin_effect_inductance = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Conductor method comp_skin_effect_inductance: "
                    + str(comp_skin_effect_inductance)
                )
            )
        )
    else:
        comp_skin_effect_inductance = comp_skin_effect_inductance
    # cf Methods.Machine.Conductor.comp_temperature_effect
    if isinstance(comp_temperature_effect, ImportError):
        comp_temperature_effect = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Conductor method comp_temperature_effect: "
                    + str(comp_temperature_effect)
                )
            )
        )
    else:
        comp_temperature_effect = comp_temperature_effect
    # cf Methods.Machine.Conductor.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Conductor method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, cond_mat=-1, ins_mat=-1, init_dict=None, init_str=None):
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
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.cond_mat = cond_mat
        self.ins_mat = ins_mat

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Conductor_str = ""
        if self.parent is None:
            Conductor_str += "parent = None " + linesep
        else:
            Conductor_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.cond_mat is not None:
            tmp = self.cond_mat.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Conductor_str += "cond_mat = " + tmp
        else:
            Conductor_str += "cond_mat = None" + linesep + linesep
        if self.ins_mat is not None:
            tmp = self.ins_mat.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Conductor_str += "ins_mat = " + tmp
        else:
            Conductor_str += "ins_mat = None" + linesep + linesep
        return Conductor_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.cond_mat != self.cond_mat:
            return False
        if other.ins_mat != self.ins_mat:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.cond_mat is None and self.cond_mat is not None) or (
            other.cond_mat is not None and self.cond_mat is None
        ):
            diff_list.append(name + ".cond_mat None mismatch")
        elif self.cond_mat is not None:
            diff_list.extend(
                self.cond_mat.compare(
                    other.cond_mat,
                    name=name + ".cond_mat",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.ins_mat is None and self.ins_mat is not None) or (
            other.ins_mat is not None and self.ins_mat is None
        ):
            diff_list.append(name + ".ins_mat None mismatch")
        elif self.ins_mat is not None:
            diff_list.extend(
                self.ins_mat.compare(
                    other.ins_mat,
                    name=name + ".ins_mat",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.cond_mat)
        S += getsizeof(self.ins_mat)
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

        Conductor_dict = dict()
        if self.cond_mat is None:
            Conductor_dict["cond_mat"] = None
        else:
            Conductor_dict["cond_mat"] = self.cond_mat.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.ins_mat is None:
            Conductor_dict["ins_mat"] = None
        else:
            Conductor_dict["ins_mat"] = self.ins_mat.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        Conductor_dict["__class__"] = "Conductor"
        return Conductor_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.cond_mat is None:
            cond_mat_val = None
        else:
            cond_mat_val = self.cond_mat.copy()
        if self.ins_mat is None:
            ins_mat_val = None
        else:
            ins_mat_val = self.ins_mat.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(cond_mat=cond_mat_val, ins_mat=ins_mat_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.cond_mat is not None:
            self.cond_mat._set_None()
        if self.ins_mat is not None:
            self.ins_mat._set_None()

    def _get_cond_mat(self):
        """getter of cond_mat"""
        return self._cond_mat

    def _set_cond_mat(self, value):
        """setter of cond_mat"""
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
                "pyleecan.Classes", value.get("__class__"), "cond_mat"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Material = import_class("pyleecan.Classes", "Material", "cond_mat")
            value = Material()
        check_var("cond_mat", value, "Material")
        self._cond_mat = value

        if self._cond_mat is not None:
            self._cond_mat.parent = self

    cond_mat = property(
        fget=_get_cond_mat,
        fset=_set_cond_mat,
        doc="""Material of the conductor

        :Type: Material
        """,
    )

    def _get_ins_mat(self):
        """getter of ins_mat"""
        return self._ins_mat

    def _set_ins_mat(self, value):
        """setter of ins_mat"""
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
                "pyleecan.Classes", value.get("__class__"), "ins_mat"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Material = import_class("pyleecan.Classes", "Material", "ins_mat")
            value = Material()
        check_var("ins_mat", value, "Material")
        self._ins_mat = value

        if self._ins_mat is not None:
            self._ins_mat.parent = self

    ins_mat = property(
        fget=_get_ins_mat,
        fset=_set_ins_mat,
        doc="""Material of the insulation

        :Type: Material
        """,
    )
