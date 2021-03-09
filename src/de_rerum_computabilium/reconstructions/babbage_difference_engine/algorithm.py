"""
Charles Babbage's Difference Engine No. 2 (c. 1847-1849).
Polynomial tabulation via method of finite differences.
"""
from de_rerum_computabilium.core.trace import Trace

def babbage_engine(cycles: int, initial_c0: int, initial_c1: int, initial_c2: int) -> Trace:
    """
    Simulates the Odd/Even mechanical pipeline of the Difference Engine.
    For a degree 2 polynomial, e.g., y = x^2 + x + 41.
    """
    trace = Trace(method_name="Babbage Difference Engine No. 2", historical_era="Victorian England (1847-1849)")
    
    C0 = initial_c0 # Odd column (Function value)
    C1 = initial_c1 # Even column (1st Difference)
    C2 = initial_c2 # Odd column (2nd Difference)
    
    trace.add_step("init_registers", [C0, C1, C2], {"C0": C0, "C1": C1, "C2": C2}, cost=0)
    
    for cycle in range(1, cycles + 1):
        # Step 1: Even columns add to Odd columns
        C0 = C0 + C1
        trace.add_step("even_to_odd", [C1], C0, annotation=f"Cycle {cycle}, Step 1: C1 adds to C0", cost=1)
        
        # Step 2: Odd columns add to Even columns
        C1 = C1 + C2
        trace.add_step("odd_to_even", [C2], C1, annotation=f"Cycle {cycle}, Step 2: C2 adds to C1", cost=1)
        
        trace.add_step("print_result", [], C0, annotation=f"Result for x={cycle} is {C0}", cost=0)
        
    return trace

def polynomial_modern(x: int) -> int:
    return x**2 + x + 41

if __name__ == "__main__":
    t = babbage_engine(5, 41, 2, 2)
    print(t)
