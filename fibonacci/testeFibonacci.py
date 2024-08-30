import pytest
from fibonacci import fibonacci  

def test_fibonacci_sequence():
    
    assert fibonacci(0) == True
    assert fibonacci(1) == True
    assert fibonacci(2) == True
    assert fibonacci(3) == True
    assert fibonacci(5) == True
    assert fibonacci(8) == True
    assert fibonacci(13) == True
    assert fibonacci(21) == True
    assert fibonacci(34) == True
    assert fibonacci(55) == True

def test_non_fibonacci_sequence():
    
    assert fibonacci(4) == False
    assert fibonacci(6) == False
    assert fibonacci(7) == False
    assert fibonacci(9) == False
    assert fibonacci(10) == False
    assert fibonacci(14) == False
    assert fibonacci(22) == False
    assert fibonacci(35) == False

if __name__ == "__main__":
    pytest.main()
