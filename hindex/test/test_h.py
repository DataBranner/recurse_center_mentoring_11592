import pytest
import random
import sys
sys.path.append('..')
import hindex

params = [
         ([1, 1, 3, 4, 7, 12], 3),
         ([1, 1, 2, 7, 9, 12], 3),
         ([1, 1, 1, 1, 1], 1),
         ([1, 1, 2, 2], 2),
         ([4], 1),
         ([0, 0, 0, 0], 0),
         ([-1, -2, -3], -1),
         ([-3, -2, -1], -1),
#        ([1, 7, 3, 12, 2, 1, 1], 3),
         ]

@pytest.mark.parametrize('arg1, arg2', params)
def test_h(arg1, arg2):
    assert hindex.hindex(arg1) == arg2

def test_empty():
    with pytest.raises(ValueError):
        hindex.hindex([]) 

randlists = [[random.randint(1, 30) for x in range(10)] for i in range(100)]
@pytest.mark.parametrize('randlist', randlists)
def test_rand(randlist):
    assert isinstance(hindex.hindex(randlist), int)
