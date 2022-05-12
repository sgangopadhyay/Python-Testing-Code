import pytest
from suman import Guvi 
import pytest

@pytest.mark.first
@pytest.mark.parametrize("input,output",[(2,4), (3,9), (10, 100), (4,16)])
def test_first(input,output):
    assert Guvi().NumberSquare(input) == output


@pytest.mark.second 
@pytest.mark.parametrize("input,output", [(1,'ODD'),(2,'EVEN'),(3,'ODD'),(4,'EVEN')])
def test_second(input,output):
    assert Guvi().odd_even(input) == output