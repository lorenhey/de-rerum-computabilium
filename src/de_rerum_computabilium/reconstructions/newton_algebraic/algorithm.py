"""
Newton's Original Root Method.
From De analysi per aequationes (1669).
Algebraic substitution method (not the modern calculus version).
"""
import math
from de_rerum_computabilium.core.trace import Trace

def shift_polynomial(coeffs, a, trace, step_num):
    """
    Shifts a polynomial P(x) to P(x + a).
    """
    n = len(coeffs)
    new_coeffs = [0.0] * n
    
    cost = 0
    for i in range(n):
        for k in range(i + 1):
            term = coeffs[i] * math.comb(i, k) * (a ** (i - k))
            new_coeffs[k] += term
            cost += 3 # multiplication, comb lookup, exponentiation
            
    trace.add_step(f"algebraic_expansion_step_{step_num}", [a], new_coeffs, annotation=f"Expand P(var + {a}) algebraically", cost=cost)
    return new_coeffs

def newton_algebraic_method(initial_guess: float, iterations: int = 3) -> Trace:
    """
    Simulates Newton's original 1669 substitution method for y^3 - 2y - 5 = 0.
    """
    trace = Trace(method_name="Newton's Original Algebraic Method", historical_era="Early Modern (1669)")
    
    # y^3 - 2y - 5 = 0
    coeffs = [-5.0, -2.0, 0.0, 1.0]
    
    trace.add_step("init_polynomial", [], coeffs, annotation="Coefficients of y^3 - 2y - 5 = 0", cost=0)
    
    current_coeffs = coeffs.copy()
    root = 0.0
    
    # Newton made manual truncation decisions based on the linear term
    guess = initial_guess
    
    for i in range(1, iterations + 1):
        root += guess
        current_coeffs = shift_polynomial(current_coeffs, guess, trace, i)
        
        c0, c1 = current_coeffs[0], current_coeffs[1]
        
        # Linear approximation: c0 + c1 * next_var = 0
        raw_next = -c0 / c1 if c1 != 0 else 0
        trace.add_step(f"linear_truncation_{i}", [c0, c1], raw_next, annotation="Drop higher order terms to find next correction", cost=2)
        
        # Newton heavily rounded this (e.g. 0.1, -0.0054). We'll keep a few sig figs to simulate human choice
        if raw_next != 0:
            mag = math.floor(math.log10(abs(raw_next)))
            factor = 10 ** (mag - 1)
            rounded = round(raw_next / factor) * factor
        else:
            rounded = 0
            
        trace.add_step(f"human_rounding_{i}", [raw_next], rounded, annotation="Round correction for manageable arithmetic", cost=0)
        guess = rounded
        
    # Apply final correction
    root += guess
    trace.add_step("final_sum", [], root, annotation="Sum all corrections", cost=1)
    
    return trace

if __name__ == "__main__":
    t = newton_algebraic_method(2.0, 3)
    print(t)
