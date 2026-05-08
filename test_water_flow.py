# Author: Hagot Coriantumr Viana Castro

from pytest import approx
import pytest
from water_flow import (
    water_column_height, 
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction
)

def test_water_column_height():
    assert water_column_height(0, 0) == approx(0)
    assert water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.286870, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    assert reynolds_number(0.048692, 1.65) == approx(80069)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])