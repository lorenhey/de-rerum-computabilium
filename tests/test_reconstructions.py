import pytest
from fractions import Fraction
from de_rerum_computabilium.reconstructions.babylonian_sqrt_ybc7289.algorithm import babylonian_sqrt
from de_rerum_computabilium.reconstructions.jiuzhang_suanshu_cuberoot.algorithm import chinese_cube_root
from de_rerum_computabilium.reconstructions.euclid_gcd.algorithm import euclidean_algorithm_historical
from de_rerum_computabilium.reconstructions.babbage_difference_engine.algorithm import babbage_engine
from de_rerum_computabilium.reconstructions.ptolemy_chords.algorithm import ptolemy_chords_reconstruction

def test_babylonian_sqrt():
    trace = babylonian_sqrt(2, Fraction(3, 2), iterations=2)
    # The known exact precision in base 60 for the second iteration
    assert trace.steps[-1].precision == "1;24,51,10,35,15,0,0,0,0,0"[:len(trace.steps[-1].precision)]
    assert float(trace.steps[-1].result) > 1.414
    assert float(trace.steps[-1].result) < 1.415

def test_chinese_cube_root():
    trace = chinese_cube_root(1860872)
    assert trace.steps[-1].result == 123
    
def test_euclid_gcd():
    trace = euclidean_algorithm_historical(1071, 462)
    assert trace.steps[-1].result == 21
    
def test_babbage_engine():
    # y = x^2 + x + 41. At x=5, y=25 + 5 + 41 = 71
    trace = babbage_engine(5, 41, 2, 2)
    assert trace.steps[-1].result == 71

def test_ptolemy_chords():
    trace = ptolemy_chords_reconstruction()
    # Crd(60) = 60
    assert trace.steps[0].result == 60.0
