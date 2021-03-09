"""
Ptolemy's Table of Chords (Almagest).
Constructing the trigonometric table in base-60 (c. 150 AD).
"""
import math
from de_rerum_computabilium.core.trace import Trace

def to_sexagesimal(value: float) -> str:
    integer_part = int(value)
    remainder = value - integer_part
    minutes_full = remainder * 60
    minutes = int(minutes_full)
    seconds_full = (minutes_full - minutes) * 60
    seconds = round(seconds_full)
    return f"{integer_part}; {minutes:02d}, {seconds:02d}"

def ptolemy_chords_reconstruction() -> Trace:
    trace = Trace(method_name="Ptolemy's Table of Chords", historical_era="Hellenistic Astronomy (c. 150 AD)")
    results = {}
    
    # Base geometric chords
    results[60] = 60.0
    trace.add_step("geometric_base", [], 60.0, annotation="Hexagon Crd(60)", cost=0)
    
    # Decagon (36 degrees)
    crd_36 = math.sqrt(4500) - 30
    results[36] = crd_36
    trace.add_step("decagon_geometry", [], crd_36, precision=to_sexagesimal(crd_36), annotation="Crd(36) via Golden Ratio", cost=3)
    
    # Pentagon (72 degrees)
    crd_72 = math.sqrt(9000 - 1800 * math.sqrt(5))
    results[72] = crd_72
    trace.add_step("pentagon_geometry", [crd_36], crd_72, precision=to_sexagesimal(crd_72), annotation="Crd(72) via s5^2 = s6^2 + s10^2", cost=4)
    
    def crd_sup(crd_A): 
        return math.sqrt(120**2 - crd_A**2)
        
    def crd_diff(crd_A, crd_B):
        # Difference Formula from Ptolemy's Theorem
        return (crd_A * crd_sup(crd_B) - crd_B * crd_sup(crd_A)) / 120.0
        
    def crd_half(crd_A):
        # Half-Angle Formula
        return math.sqrt(60 * (120 - crd_sup(crd_A)))
        
    # Extract Crd(12)
    results[12] = crd_diff(results[72], results[60])
    trace.add_step("ptolemy_difference", [results[72], results[60]], results[12], precision=to_sexagesimal(results[12]), annotation="Crd(12) = Crd(72 - 60)", cost=8)
    
    # Repeated half-angles down to 0.75
    angles = [12, 6, 3, 1.5, 0.75]
    for i in range(len(angles)-1):
        results[angles[i+1]] = crd_half(results[angles[i]])
        trace.add_step("ptolemy_half_angle", [results[angles[i]]], results[angles[i+1]], precision=to_sexagesimal(results[angles[i+1]]), annotation=f"Crd({angles[i+1]})", cost=5)
        
    # Aristarchus's inequality
    lower_bound = (2/3) * results[1.5]
    upper_bound = (4/3) * results[0.75]
    
    results[1] = (lower_bound + upper_bound) / 2
    trace.add_step("aristarchus_inequality", [lower_bound, upper_bound], results[1], precision=to_sexagesimal(results[1]), annotation="Crd(1) interpolation", cost=2)
    
    return trace

if __name__ == '__main__':
    t = ptolemy_chords_reconstruction()
    print(t)
