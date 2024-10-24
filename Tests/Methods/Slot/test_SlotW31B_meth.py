# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW31B import SlotW31B
from pyleecan.Classes.Slot import Slot
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Winding import Winding
from numpy import exp, pi, radians

mm = 1e-3
DELTA = 1e-4

slotW31B_test = list()

lam = LamSlotWind(Rint=17e-3, Rext=30e-3, is_internal=False, L1=30e-3, is_stator=True)
lam.slot = SlotW31B(Zs=12, H1=radians(120), H2=radians(90), W2=2e-3, W0=2e-3)

print(lam.slot.comp_surface())

slotW31B_test.append(
    {
        "test_obj": lam,
        "S_exp": 7.801921158634867e-05,
        "Aw": 0.112537,
        "SO_exp": 3.24619910e-05,
        "SW_exp": 3.8834260e-04,
        "H_exp": 0.032438,
    }
)


class Test_SlotW31B_meth(object):
    """pytest for SlotW23 methods"""

    @pytest.mark.parametrize("test_dict", slotW31B_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"].copy()
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check W0
        assert abs(point_dict["Z1"] - point_dict["Z10"]) == pytest.approx(
            test_obj.slot.W0
        )

        # Check H0
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )

    @pytest.mark.parametrize("test_dict", slotW31B_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b) + "  not analytic"
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg


if __name__ == "__main__":
    a = Test_SlotW31B_meth()
    for ii, test_dict in enumerate(slotW31B_test):
        print("Running test for Slot[" + str(ii) + "]")
        a.test_schematics(test_dict)
        a.test_comp_surface(test_dict)
        print("Done")
