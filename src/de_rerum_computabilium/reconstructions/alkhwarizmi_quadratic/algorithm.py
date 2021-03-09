"""
Al-Khwarizmi's Completing the Square.
From The Compendious Book on Calculation by Completion and Balancing (c. 820 AD).
Solves x^2 + px = q geometrically.
"""
import math
from de_rerum_computabilium.core.trace import Trace

def al_khwarizmi_quadratic(p: float, q: float) -> Trace:
    """
    Solves x^2 + px = q using the geometric steps of Al-Khwarizmi.
    He describes it as squares and roots equaling numbers.
    """
    trace = Trace(method_name="Completing the Square", historical_era="Islamic Golden Age (c. 820 AD)")
    
    trace.add_step("init_equation", [p, q], f"x^2 + {p}x = {q}", annotation="Roots and squares equal to numbers", cost=0)
    
    # "You halve the number of roots"
    half_p = p / 2.0
    trace.add_step("halve_roots", [p], half_p, annotation="Halve the number of roots (p/2)", cost=1)
    
    # "Multiply this by itself"
    square_half_p = half_p * half_p
    trace.add_step("square_half_roots", [half_p], square_half_p, annotation="Square the halved roots (p/2)^2", cost=1)
    
    # "Add this to the numbers"
    total_area = square_half_p + q
    trace.add_step("add_to_numbers", [square_half_p, q], total_area, annotation="Add the squared half-roots to the constant q (Completing the geometric square)", cost=1)
    
    # "Extract the root of this"
    root_area = math.sqrt(total_area)
    trace.add_step("extract_root", [total_area], root_area, annotation="Take the square root of the completed square", cost=5) # Sqrt is expensive historically
    
    # "Subtract from this half the number of roots"
    x = root_area - half_p
    trace.add_step("subtract_half_roots", [root_area, half_p], x, annotation="Subtract the half-roots to find x", cost=1)
    
    return trace

if __name__ == "__main__":
    t = al_khwarizmi_quadratic(10, 39) # Al-Khwarizmi's famous example: x^2 + 10x = 39 (solution x=3)
    print(t)
