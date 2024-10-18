# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW31B import SlotW31B
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Winding import Winding
from numpy import exp, pi, radians

mm = 1e-3
DELTA = 1e-4

slotW31B_test = list()

lam = LamSlotWind(
    Rint=17e-3, Rext=30e-3, is_internal=False, L1=30e-3, Nrvd=0, is_stator=True
)
lam.slot = SlotW31B(Zs=12, H1=radians(120), H2=radians(90), W2=2e-3, W0=2e-3)

lam.winding = Winding(
    qs=3,
    p=4,
    Nlayer=2,
    coil_pitch=1,
    Lewout=0,
    Ntcoil=9,  # number of turns per coil
    Npcp=1,  # number of parallel circuits per phase
    Nslot_shift_wind=0,
    is_reverse_wind=False,
)
