"""
Merton Mean Speed Theorem.
From the Merton College Calculators (c. 1330s).
"A body moving with a uniformly accelerated velocity covers the same distance as a body moving with a constant velocity equal to the mean of its initial and final velocities."
"""
from de_rerum_computabilium.core.trace import Trace

def merton_mean_speed(v_initial: float, v_final: float, time: float) -> Trace:
    """
    Calculates distance covered under uniform acceleration using the Merton rule.
    """
    trace = Trace(method_name="Merton Mean Speed Theorem", historical_era="High Middle Ages (1330s)")
    
    trace.add_step("init_kinematics", [v_initial, v_final, time], {"vi": v_initial, "vf": v_final, "t": time}, cost=0)
    
    # 1. Calculate Mean Velocity
    v_mean = (v_initial + v_final) / 2.0
    trace.add_step("calculate_mean_velocity", [v_initial, v_final], v_mean, annotation="v_mean = (vi + vf) / 2", cost=2)
    
    # 2. Geometric rectangle area (Distance)
    distance = v_mean * time
    trace.add_step("calculate_distance", [v_mean, time], distance, annotation="distance = v_mean * t (Area of Oresme's rectangle)", cost=1)
    
    return trace

if __name__ == "__main__":
    t = merton_mean_speed(0, 10, 5) # Dist = 25
    print(t)
