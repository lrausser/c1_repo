import pytest
import sys 
#ys.path.insert(0, '/Users/lilyrausser/c1_coursework/lsr34')
from dual import Dual 
import math 

def test_init():
    dual = Dual(3, 4)
    assert dual.real == 3
    assert dual.dual == 4

    dual_default = Dual(3)
    assert dual_default.real == 3
    assert dual_default.dual == 0.0


#test the arithmatic operations
def test_add():
    dual1 = Dual(2, 1)
    dual2 = Dual(3, 2)
    result = dual1 + dual2
    assert result.real == 5
    assert result.dual == 3

    scalar_result = dual1 + Dual(4)
    assert scalar_result.real == 6
    assert scalar_result.dual == 1.0

def test_subtraction():
    dual1 = Dual(2, 1)
    dual2 = Dual(3, 2)
    result = dual1 - dual2 
    assert result.real == -1
    assert result.dual == -1

    scalar_ex = dual1 - Dual(3)
    assert scalar_ex.real == -1
    assert scalar_ex.dual == 1.0

def test_mult():
    dual1 = Dual(2, 1)
    dual2 = Dual(3, 2)
    result = dual1 * dual2
    assert result.real == 6
    assert result.dual == 7

    scalar_ex = dual1 * Dual(3)
    assert scalar_ex.real == 6
    assert scalar_ex.dual == 3.0

def test_div():
    dual1 = Dual(2, 2)
    dual2 = Dual(2, 2)
    result = dual1 / dual2
    assert result.real == 1.0 
    assert result.dual == 0.0 

    scalar_ex = dual1 / Dual(4)
    assert scalar_ex.real == 0.5
    assert scalar_ex.dual == 0.5 

def test_pow():
    dual = Dual(2, 1)
    result = dual ** 2
    assert result.real == 4
    assert result.dual == 4

    with pytest.raises(ValueError):
        Dual(0, 1) ** -1
    with pytest.raises(ValueError):
        dual ** "invalid, include a power value"

def test_sin():
    dual = Dual(math.pi / 5, 1)
    sin_result = dual.sin()
    assert math.isclose(sin_result.real, math.sin(math.pi / 5))
    assert math.isclose(sin_result.dual, math.cos(math.pi / 5))

def test_cos():
    dual = Dual(math.pi / 5, 1)
    cos_result = dual.cos()
    assert math.isclose(cos_result.real, math.cos(math.pi / 5))
    assert math.isclose(cos_result.dual, -math.sin(math.pi / 5))

def test_tan():
    dual = Dual(math.pi / 5, 1)
    tan_result = dual.tan()
    assert math.isclose(tan_result.real, math.tan(math.pi / 5))
    assert math.isclose(tan_result.dual, 1 / (math.cos(math.pi / 5) ** 2))

    with pytest.raises(ValueError):
        Dual(math.pi / 2, 1).tan()

def test_exp():
    dual = Dual(2, 1)
    exp_result = dual.exp()
    assert math.isclose(exp_result.real, math.exp(2))
    assert math.isclose(exp_result.dual, 1 * math.exp(2))
    
def test_log():
    dual = Dual(2, 1)
    log_result = dual.log()
    assert math.isclose(log_result.real, math.log(2))
    assert math.isclose(log_result.dual, 1 / 2)

def test_string_rep():
    dual = Dual(2, 1)
    assert repr(dual) == "Dual(real = 2, dual = 1)"