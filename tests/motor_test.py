import pytest

import efwa as ef

from efwa.conversions import *


@pytest.fixture
def motor():
    return ef.motor.Motor(rpm=5000, diameter=in2m(18),
                          pitch=in2m(9), density=1.112)


def test_thrust_calculation(motor):
    assert abs(motor.calc_thrust() - 21.85153551627929) < 1e-6


def test_rpm_calculation(motor):
    thrust = motor.calc_thrust()
    assert abs(motor.calc_rpm(thrust) - 5000) < 1e-6
