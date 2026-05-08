from kinetics import calculate_kinetic_energy, calculate_potential_energy
import pytest

def test_calculate_kinetic_energy():
   
    # Standard case
    assert calculate_kinetic_energy(10, 2) == 20.0
    # Zero velocity
    assert calculate_kinetic_energy(5, 0) == 0.0
    # Small decimals
    assert calculate_kinetic_energy(0.5, 4) == 4.0

def test_calculate_potential_energy():
    
    # Standard case (10kg * 9.80665g * 2m)
    assert calculate_potential_energy(10, 2) == pytest.approx(196.133, 0.01)
    # Zero height
    assert calculate_potential_energy(50, 0) == 0.0

def test_negative_values():
    
    with pytest.raises(ValueError):
        calculate_kinetic_energy(-5, 10)
    with pytest.raises(ValueError):
        calculate_potential_energy(10, -2)