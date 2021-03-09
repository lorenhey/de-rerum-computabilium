"""
Runge-Kutta Method (Classical RK4).
Based on Kutta's 1901 worksheet formulation with intermediate rounding.
"""
from typing import Callable
from de_rerum_computabilium.core.trace import Trace
from de_rerum_computabilium.core.arithmetic import FixedDecimal

def runge_kutta_historical(y0: float, h: float, decimals: int = 5) -> Trace:
    """
    Simulates the 1901 Kutta worksheet procedure for dy/dx = y.
    Intermediate roundings replicate human computation constraints.
    """
    trace = Trace(method_name="Kutta's 1901 Worksheet (RK4)", historical_era="Early 20th Century (1901)")
    
    y = FixedDecimal(y0, decimals)
    step = FixedDecimal(h, decimals)
    two = FixedDecimal(2.0, decimals)
    six = FixedDecimal(6.0, decimals)
    
    trace.add_step("init_worksheet", [y.to_float(), step.to_float()], {"y": y.to_float(), "h": step.to_float()}, cost=0)
    
    # In fixed decimal, we simulate:
    # 1. First increment
    # f(y) = y, so delta_1 = y * h
    delta_1 = y * step
    trace.add_step("delta_prime", [y.to_float(), step.to_float()], delta_1.to_float(), annotation="Δ' = f(x, y) * h", cost=1)
    
    # 2. Second increment
    # y_inter_1 = y + delta_1 / 2
    delta_1_half = FixedDecimal(delta_1.to_float() / 2.0, decimals) # Human division by 2
    y_inter_1 = y + delta_1_half
    delta_2 = y_inter_1 * step
    trace.add_step("delta_double_prime", [y_inter_1.to_float(), step.to_float()], delta_2.to_float(), annotation="Δ'' = f(x+h/2, y+Δ'/2) * h", cost=3)
    
    # 3. Third increment
    delta_2_half = FixedDecimal(delta_2.to_float() / 2.0, decimals)
    y_inter_2 = y + delta_2_half
    delta_3 = y_inter_2 * step
    trace.add_step("delta_triple_prime", [y_inter_2.to_float(), step.to_float()], delta_3.to_float(), annotation="Δ''' = f(x+h/2, y+Δ''/2) * h", cost=3)
    
    # 4. Fourth increment
    y_inter_3 = y + delta_3
    delta_4 = y_inter_3 * step
    trace.add_step("delta_quad_prime", [y_inter_3.to_float(), step.to_float()], delta_4.to_float(), annotation="Δ'''' = f(x+h, y+Δ''') * h", cost=2)
    
    # 5. Accumulation
    # sum = delta_1 + 2*delta_2 + 2*delta_3 + delta_4
    d2_doubled = delta_2 * two
    d3_doubled = delta_3 * two
    sum_deltas = delta_1 + d2_doubled + d3_doubled + delta_4
    delta_y = FixedDecimal(sum_deltas.to_float() / 6.0, decimals) # Human division by 6
    trace.add_step("accumulation", [delta_1.to_float(), delta_2.to_float(), delta_3.to_float(), delta_4.to_float()], delta_y.to_float(), annotation="Δy = (Δ' + 2Δ'' + 2Δ''' + Δ'''') / 6", cost=6)
    
    # 6. Next state
    y_new = y + delta_y
    trace.add_step("final_state", [y.to_float(), delta_y.to_float()], y_new.to_float(), annotation="y_new = y + Δy", cost=1)
    
    return trace

if __name__ == "__main__":
    t = runge_kutta_historical(1.0, 0.1)
    print(t)
