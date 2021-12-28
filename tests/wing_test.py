import pytest

import efwa as ef


@pytest.fixture
def airfoil():
    foil = ef.wings.Airfoil(
        "airfoil", "/home/hnobles12/Documents/TAMU/2022_Spring/AERO_402/Electric-Fixed-Wing-Aircraft-Development/tests/test_data/sd7037_airfoil.csv")
    return foil


def test_alpha_stall(airfoil):
    assert airfoil.alpha_stall == 11.0


def test_cl_max(airfoil):
    assert airfoil.cl_max == 1.2802


@pytest.fixture
def unloaded_airfoil_wing():
    wing = ef.wings.Wing()
    return wing


def test_airfoil_load_err(unloaded_airfoil_wing):
    with pytest.raises(ef.errors.AirfoilNotLoadedErr):
        unloaded_airfoil_wing.check_airfoil_loaded()


@pytest.fixture
def wing():
    wing_obj = ef.wings.Wing(
        airfoil_file="/home/hnobles12/Documents/TAMU/2022_Spring/AERO_402/Electric-Fixed-Wing-Aircraft-Development/tests/test_data/sd7037_airfoil.csv")
    return wing_obj


def test_airfoil_load_on_wing_creation(wing):
    assert wing.foil_loaded
