"""
Galton's Quincunx (Galton Board).
Simulation of Sir Francis Galton's mechanical device (c. 1873) to demonstrate the normal distribution.
"""
import random
from de_rerum_computabilium.core.trace import Trace

def galton_quincunx(beans: int, rows: int) -> Trace:
    """
    Simulates the mechanical dropping of beans through a quincunx.
    """
    trace = Trace(method_name="Galton's Quincunx", historical_era="Victorian England (c. 1873)")
    
    bins = [0] * (rows + 1)
    
    trace.add_step("init_quincunx", [beans, rows], {"bins": bins}, cost=0)
    
    for bean in range(beans):
        position = 0
        for row in range(rows):
            # Mechanical decision: bounce left (0) or right (1)
            bounce = random.choice([0, 1])
            position += bounce
        
        bins[position] += 1
        trace.add_step(f"drop_bean_{bean}", [], position, annotation=f"Bean {bean} lands in bin {position}", cost=rows)
        
    trace.add_step("read_distribution", [], bins, annotation="Final mechanical distribution of beans", cost=0)
    
    return trace

if __name__ == "__main__":
    t = galton_quincunx(100, 10)
    print(t)
