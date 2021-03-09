"""
Briggs' Common Logarithms.
From Arithmetica Logarithmica (1624).
Briggs calculated log10(x) by extracting the square root 54 times.
"""
import math
from de_rerum_computabilium.core.trace import Trace

def briggs_logarithm(x: float, iterations: int = 54) -> Trace:
    """
    Simulates Briggs' calculation of log10(x) using repeated square roots.
    He used the property that for very small t, log10(1+t) ~ t * M
    where M = log10(e) = 0.4342944819.
    By taking the sqrt 54 times, x becomes 1+t.
    """
    trace = Trace(method_name="Briggs' Common Logarithms", historical_era="Early Modern (1624)")
    
    trace.add_step("init", [x], x, annotation="Calculate log10(x)", cost=0)
    
    current_val = x
    
    for i in range(1, iterations + 1):
        # A human would use a manual root extraction algorithm (like the Babylonian method)
        # Here we model the mathematical step but charge a high material cost
        current_val = math.sqrt(current_val)
        trace.add_step("extract_root", [], current_val, annotation=f"Square root extraction {i}", cost=10)
        
    # After 54 square roots, current_val = 1 + t
    t = current_val - 1.0
    trace.add_step("subtract_one", [current_val], t, annotation="Subtract 1 to find the small increment 't'", cost=1)
    
    # Briggs found M by doing the same 54 root process on 10, to find log_10(10)=1. 
    # M is the constant of proportionality. 
    # Actually, Briggs computed the logs of primes. For this trace, we use his known constant M.
    # To find log(x), it is 2^54 * t * M (if base 10, wait, it's 2^54 * t * log10(e)).
    # Wait, the rule is log(x^(1/2^54)) = 1/2^54 * log(x).
    # So 1/2^54 * log(x) = log(1+t) approx = t * M
    # So log(x) = 2^54 * t * M
    
    # 2^54 multiplier
    multiplier = 2**iterations
    trace.add_step("power_of_two", [iterations], multiplier, annotation="2^54 multiplier for reversing the root divisions", cost=0)
    
    # M = 0.43429448190325182
    M = 0.43429448190325182
    
    # Final multiplication
    result = multiplier * t * M
    trace.add_step("final_multiplication", [multiplier, t, M], result, annotation="log10(x) = 2^54 * t * M", cost=1)
    
    return trace

if __name__ == "__main__":
    t = briggs_logarithm(2) # log10(2) approx 0.30103
    print(t)
