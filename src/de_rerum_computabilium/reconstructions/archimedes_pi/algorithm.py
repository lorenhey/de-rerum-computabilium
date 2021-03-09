"""
Archimedes' Pi (Method of Exhaustion).
From Measurement of a Circle (c. 250 BCE).
Using fractional rational bounds for sqrt(3).
"""
from fractions import Fraction
from de_rerum_computabilium.core.trace import Trace

def archimedes_pi() -> Trace:
    """
    Reconstructs Archimedes' rational approximations for Pi (lower bound, inscribed 96-gon).
    """
    trace = Trace(method_name="Archimedes Pi (Method of Exhaustion)", historical_era="Hellenistic Greece (c. 250 BC)")
    
    # Inscribed 96-gon calculations
    # n = 6
    x = Fraction(1351, 780)
    y = Fraction(1560, 780)
    trace.add_step("init_n_6", [], {"x": f"{x.numerator}/{x.denominator}", "y": f"{y.numerator}/{y.denominator}"}, annotation="Initial 6-gon ratios. x is upper bound for sqrt(3)", cost=0)
    
    # n = 12
    x = x + y
    y = Fraction(3013 * 4 + 3, 4 * 780) # 3013 3/4 / 780 (Upper bound root)
    trace.add_step("n_12", [], {"x": f"{x.numerator}/{x.denominator}", "y": f"{y.numerator}/{y.denominator}"}, annotation="Double to 12-gon. y = sqrt(x^2+1) rounded up for strict bound", cost=3)
    
    # n = 24
    # Archimedes reduces fractions manually
    x = Fraction(1823, 240)
    y = Fraction(1838 * 11 + 9, 11 * 240)
    trace.add_step("n_24", [], {"x": f"{x.numerator}/{x.denominator}", "y": f"{y.numerator}/{y.denominator}"}, annotation="Double to 24-gon. Fractional simplification by dividing by 13.", cost=4)
    
    # n = 48
    x = Fraction(1007, 66)
    y = Fraction(1009 * 6 + 1, 6 * 66)
    trace.add_step("n_48", [], {"x": f"{x.numerator}/{x.denominator}", "y": f"{y.numerator}/{y.denominator}"}, annotation="Double to 48-gon. Simplified by dividing by 40.", cost=4)
    
    # n = 96
    x = x + y
    y = Fraction(2017 * 4 + 1, 4 * 66)
    trace.add_step("n_96", [], {"x": f"{x.numerator}/{x.denominator}", "y": f"{y.numerator}/{y.denominator}"}, annotation="Double to 96-gon.", cost=3)
    
    # Lower bound ratio
    pi_lower = 96 / y
    rem_lower = pi_lower.numerator - 3 * pi_lower.denominator
    result_str = f"3 + {rem_lower}/{pi_lower.denominator}"
    
    trace.add_step("final_ratio", [], result_str, annotation="Final ratio of inscribed 96-gon perimeter to diameter", cost=2)
    
    return trace

if __name__ == "__main__":
    t = archimedes_pi()
    print(t)
