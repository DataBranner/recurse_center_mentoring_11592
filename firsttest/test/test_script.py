import sys
import pytest
sys.path.append('..')
import script

params = range(10)

@pytest.mark.parametrize("n", params)
def test_squares(n):
    assert script.squares(n) == n * n

