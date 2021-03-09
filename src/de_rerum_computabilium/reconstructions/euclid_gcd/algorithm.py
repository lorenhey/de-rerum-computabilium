"""
Euclidean Algorithm (Anthyphaeresis).
From Euclid's Elements, Book VII, Proposition 1 & 2 (c. 300 BC).
"""
from de_rerum_computabilium.core.trace import Trace

def euclidean_algorithm_historical(a: int, b: int) -> Trace:
    """
    Historical Euclidean Algorithm via repeated subtraction (anthyphaeresis).
    Modulo division is a modern shortcut.
    """
    trace = Trace(method_name="Euclidean Algorithm (Anthyphaeresis)", historical_era="Hellenistic Greece (c. 300 BC)")
    
    A, B = a, b
    trace.add_step("init_magnitudes", [A, B], (A, B), annotation="Initial magnitudes", cost=0)
    
    step_num = 1
    while A != B and A > 0 and B > 0:
        if A > B:
            A = A - B
            trace.add_step("subtract", [A + B, B], A, annotation=f"A is greater. A = A - B", cost=1)
        else:
            B = B - A
            trace.add_step("subtract", [B + A, A], B, annotation=f"B is greater. B = B - A", cost=1)
        step_num += 1
        
    result = A if A > 0 else B
    trace.add_step("measure_found", [], result, annotation=f"Common measure found: {result}", cost=0)
    
    return trace

def euclidean_algorithm_modern(a: int, b: int) -> int:
    """Modern modulo-based shortcut."""
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    t = euclidean_algorithm_historical(1071, 462)
    print(t)
