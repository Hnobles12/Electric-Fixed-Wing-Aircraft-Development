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
