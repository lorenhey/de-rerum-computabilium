"""
Egyptian Multiplication.
From the Rhind Mathematical Papyrus (c. 1550 BC).
Uses repeated doubling and halving to multiply two numbers.
"""
from de_rerum_computabilium.core.trace import Trace

def egyptian_multiplication(a: int, b: int) -> Trace:
    """
    Multiply a and b using the Egyptian method of halving and doubling.
    """
    trace = Trace(method_name="Egyptian Multiplication", historical_era="Ancient Egypt (c. 1550 BC)")
    
    trace.add_step("init_operands", [a, b], {"left": a, "right": b}, cost=0)
    
    left = a
    right = b
    
    table = []
    
    # Doubling phase
    while left >= 1:
        table.append((left, right))
        trace.add_step("halve_and_double", [left, right], {"left": left, "right": right}, cost=1)
        left = left // 2
        right = right * 2
        
    # Addition phase
    result = 0
    components = []
    for l, r in table:
        if l % 2 != 0:
            result += r
            components.append(r)
            trace.add_step("accumulate", [result - r, r], result, annotation=f"Left is odd ({l}), add {r} to total", cost=1)
            
    trace.add_step("final_result", components, result, annotation="Final sum of selected right column values", cost=0)
    
    return trace

if __name__ == "__main__":
    t = egyptian_multiplication(23, 15)
    print(t)
