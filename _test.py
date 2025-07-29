import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

# Testing the square function 
def test_square():
    assert square(2)==4, "Test failed: Square of 2 should be four"
    assert square(3)==9, "Test failed: Square of 3 should be nine"
# Testing the Cube function 
def test_cube():
    assert cube(2)==8, "Test failed: Cube of 2 should be eigth"
    assert cube(3)==27, "Test failed: Cube of 3 should be twenty-seven"
# Testing the fifth_power number
def test_fifth_power():
    assert fifth_power(2)==32, "Test failed: Fifth_power of 2 should be 32"
    assert fifth_power(3)==243, "Test failed: Fifth_power should be 243"

# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")

