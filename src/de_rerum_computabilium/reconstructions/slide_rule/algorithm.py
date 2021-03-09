"""
Slide Rule Multiplication.
Simulates reading and manipulating a standard slide rule (c. 17th-20th Century).
"""
import math
from de_rerum_computabilium.core.trace import Trace

def slide_rule_multiply(a: float, b: float) -> Trace:
    """
    Simulates multiplying a and b on a slide rule.
    The user aligns the index (1) of the C scale with 'a' on the D scale,
    then reads the D scale under 'b' on the C scale.
    Precision is mechanically limited to about 3 significant digits.
    """
    trace = Trace(method_name="Slide Rule Multiplication", historical_era="17th-20th Century")
    
    trace.add_step("init_problem", [a, b], {"a": a, "b": b}, cost=0)
    
    # 1. Normalize to [1, 10)
    def normalize(val):
        power = math.floor(math.log10(val))
        norm = val / (10 ** power)
        return norm, power
        
    norm_a, p_a = normalize(a)
    norm_b, p_b = normalize(b)
    
    trace.add_step("mental_normalization", [a, b], {"norm_a": norm_a, "norm_b": norm_b, "powers": p_a + p_b}, annotation="Mental arithmetic to find order of magnitude", cost=1)
    
    # 2. Physical alignment
    # Slide C index to 'norm_a' on D
    # Physically, this means adding distances proportional to log10
    dist_a = math.log10(norm_a)
    dist_b = math.log10(norm_b)
    
    trace.add_step("align_c_index", [norm_a], dist_a, annotation="Move C index to 'a' on D scale", cost=1)
    
    # 3. Read result
    total_dist = dist_a + dist_b
    if total_dist >= 1.0:
        total_dist -= 1.0
        p_b += 1 # mentally track the scale wrap
        trace.add_step("wrap_scale", [], total_dist, annotation="Cursor wraps around, mental +1 to power", cost=1)
        
    # Read the D scale at total_dist
    read_val = 10 ** total_dist
    
    # Simulate human visual precision (about 3 sig figs)
    read_val_rounded = round(read_val, 2)
    trace.add_step("read_cursor", [total_dist], read_val_rounded, annotation="Read value from D scale visually (limited precision)", cost=1)
    
    # 4. Apply mental order of magnitude
    final_result = read_val_rounded * (10 ** (p_a + p_b))
    trace.add_step("apply_magnitude", [read_val_rounded, p_a + p_b], final_result, annotation="Apply mental magnitude to reading", cost=1)
    
    return trace

if __name__ == "__main__":
    t = slide_rule_multiply(2.5, 3.2)
    print(t)
