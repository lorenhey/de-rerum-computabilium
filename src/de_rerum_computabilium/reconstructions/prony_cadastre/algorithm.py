"""
Gaspard de Prony's Cadastre Tables.
The factory model of human computing (1790s).
Simulates the "third tier" of computers who only performed additions of finite differences.
"""
from de_rerum_computabilium.core.trace import Trace

def prony_cadastre_tier3(start_y: float, start_d1: float, start_d2: float, start_d3: float, steps: int) -> Trace:
    """
    Simulates the 3rd tier of de Prony's human computers.
    Given initial differences, they compute the next 'steps' values of the function using ONLY additions.
    """
    trace = Trace(method_name="de Prony's Cadastre (Tier 3)", historical_era="French Revolution (1790s)")
    
    y = start_y
    d1 = start_d1
    d2 = start_d2
    d3 = start_d3
    
    trace.add_step("init_differences", [y, d1, d2, d3], {"y": y, "d1": d1, "d2": d2, "d3": d3}, annotation="Receive initial values from Tier 2 mathematicians", cost=0)
    
    results = [y]
    
    for step in range(1, steps + 1):
        # Human addition from right to left (highest difference to lowest)
        d2 = d2 + d3
        trace.add_step(f"add_d3_to_d2_step_{step}", [d2 - d3, d3], d2, annotation="d2 = d2 + d3", cost=1)
        
        d1 = d1 + d2
        trace.add_step(f"add_d2_to_d1_step_{step}", [d1 - d2, d2], d1, annotation="d1 = d1 + d2", cost=1)
        
        y = y + d1
        trace.add_step(f"add_d1_to_y_step_{step}", [y - d1, d1], y, annotation="y = y + d1", cost=1)
        
        results.append(y)
        
    trace.add_step("submit_manuscript", [], results, annotation="Hand results to Tier 1 for printing", cost=0)
    
    return trace

if __name__ == "__main__":
    t = prony_cadastre_tier3(0.0, 0.01, -0.0001, 0.000001, 5)
    print(t)
