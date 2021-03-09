"""
Madhava's Sine Series.
From the Kerala School of Mathematics (14th Century).
Evaluates the Taylor expansion of Sine using historical scaling.
"""
import math
from de_rerum_computabilium.core.trace import Trace

def madhava_sine(arc_minutes: float, radius: float = 3437.75, terms: int = 5) -> Trace:
    """
    Computes R * sin(arc/R) tracing Madhava's historical accumulation.
    """
    trace = Trace(method_name="Madhava Sine Series", historical_era="14th-Century Kerala (India)")
    
    trace.add_step("init_geometry", [arc_minutes, radius], {"arc": arc_minutes, "R": radius}, cost=0)
    
    R_sin = 0.0
    current_term = arc_minutes
    R_sin += current_term
    
    trace.add_step("term_1", [arc_minutes], current_term, annotation="First term is simply the arc", cost=1)
    
    for i in range(1, terms):
        divisor = (2 * i) * (2 * i + 1)
        
        # current_term = -current_term * (arc_minutes**2) / (radius**2) / divisor
        # The historical method multiplied by s^2, divided by R^2, divided by factorial increments.
        arc_sq = arc_minutes ** 2
        r_sq = radius ** 2
        
        step_val = (current_term * arc_sq) / r_sq / divisor
        current_term = -step_val
        
        R_sin += current_term
        
        trace.add_step(f"term_{i+1}", [arc_sq, r_sq, divisor], current_term, annotation=f"Accumulate term {i+1} via Horner-like iteration", cost=4) # mult, div, div, add/sub
        
    trace.add_step("final_sine", [], R_sin, annotation="Final calculated R * Sine", cost=0)
    
    return trace

if __name__ == "__main__":
    t = madhava_sine(1800) # approx 30 degrees
    print(t)
