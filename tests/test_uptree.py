import pytest
import random

def test_coin_flip_neuron():
    from ctm_project.classes.UpTree import UpTree
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    result = UpTree.coin_flip_neuron(a, b)
    assert result in [a, b]