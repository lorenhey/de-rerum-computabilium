"""
William Shanks' Calculation of Pi to 707 digits.
From 1873, using Machin's formula and integer math.
"""
from de_rerum_computabilium.core.trace import Trace

def shanks_pi(digits: int = 100) -> Trace:
    """
    Simulates Shanks' exact manual worksheet process using integer arithmetic.
    """
    trace = Trace(method_name="William Shanks' Pi", historical_era="Victorian England (1873)")
    
    guard_digits = 10
    precision = digits + guard_digits
    scale = 10 ** precision
    
    trace.add_step("init_scale", [digits, guard_digits], scale, annotation="Establish base scale (10^digits+guard) to use integer arithmetic", cost=0)
    
    # Series 1: 1/5
    term_5 = scale // 5
    sum_5 = term_5
    n = 1
    
    while True:
        n += 2
        term_5 = term_5 // 25
        if term_5 == 0:
            break
        current_term = term_5 // n
        trace.add_step(f"series_1_term_{n}", [], current_term, annotation=f"Divide previous term by 25, then by {n}", cost=2)
        
        if (n // 2) % 2 == 1:
            sum_5 -= current_term
            trace.add_step(f"series_1_sub_{n}", [sum_5 + current_term, current_term], sum_5, annotation="Subtract alternating term", cost=1)
        else:
            sum_5 += current_term
            trace.add_step(f"series_1_add_{n}", [sum_5 - current_term, current_term], sum_5, annotation="Add alternating term", cost=1)
            
    sum_5 = 16 * sum_5
    trace.add_step("series_1_mult_16", [sum_5 // 16], sum_5, annotation="Multiply Series 1 sum by 16", cost=1)
    
    # Series 2: 1/239
    term_239 = scale // 239
    sum_239 = term_239
    n = 1
    
    while True:
        n += 2
        term_239 = term_239 // 57121 # 239^2
        if term_239 == 0:
            break
        current_term = term_239 // n
        trace.add_step(f"series_2_term_{n}", [], current_term, annotation=f"Divide previous term by 57121, then by {n}", cost=2) # Very expensive division historically
        
        if (n // 2) % 2 == 1:
            sum_239 -= current_term
            trace.add_step(f"series_2_sub_{n}", [sum_239 + current_term, current_term], sum_239, annotation="Subtract alternating term", cost=1)
        else:
            sum_239 += current_term
            trace.add_step(f"series_2_add_{n}", [sum_239 - current_term, current_term], sum_239, annotation="Add alternating term", cost=1)
            
    sum_239 = 4 * sum_239
    trace.add_step("series_2_mult_4", [sum_239 // 4], sum_239, annotation="Multiply Series 2 sum by 4", cost=1)
    
    # Combine
    pi_scaled = sum_5 - sum_239
    trace.add_step("combine_series", [sum_5, sum_239], pi_scaled, annotation="pi_scaled = sum_5 - sum_239", cost=1)
    
    # Remove guard digits
    pi_scaled = pi_scaled // (10 ** guard_digits)
    
    # Format
    pi_str = str(pi_scaled)
    result = pi_str[0] + "." + pi_str[1:]
    
    trace.add_step("format_result", [], result, annotation="Remove guard digits and place decimal", cost=0)
    
    return trace

if __name__ == "__main__":
    t = shanks_pi(20)
    print(t)
