from Ejercicio41.main import summation

def test_summation_positive():
    assert summation(1) == 1
    assert summation(5) == 15
    assert summation(10) == 55

def test_summation_negative():
    assert summation(-5) == None

