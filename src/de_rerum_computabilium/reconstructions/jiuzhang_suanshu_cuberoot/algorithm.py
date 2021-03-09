"""
Ancient Chinese Cube Root Extraction (Kai Lifang Shu).
From "The Nine Chapters on the Mathematical Art" (Jiuzhang Suanshu).
"""
from de_rerum_computabilium.core.trace import Trace

def chinese_cube_root(N: int) -> Trace:
    trace = Trace(method_name="Kai Lifang Shu (Cube Root)", historical_era="Han Dynasty China (c. 1st century CE)")
    
    shi = N
    shang = 0
    fangfa = 0
    lianfa = 0
    xiafa = 1
    
    trace.add_step("init_board", [N], {"shi": shi, "shang": shang, "fangfa": fangfa, "lianfa": lianfa, "xiafa": xiafa}, cost=0)
    
    # Align Xiafa
    while xiafa * 1000 <= shi:
        xiafa *= 1000
        trace.add_step("shift_xiafa", [xiafa], xiafa, annotation="Shift left 3 columns", cost=0)

    step_num = 1
    while xiafa >= 1:
        # Find highest digit b
        b = 0
        divisor = 0
        for test_b in range(1, 10):
            test_divisor = fangfa + test_b * lianfa + (test_b**2) * xiafa
            if test_divisor * test_b <= shi:
                b = test_b
                divisor = test_divisor
            else:
                break
                
        trace.add_step("find_digit", [shi, fangfa, lianfa, xiafa], b, annotation=f"Digit found: {b}", cost=1)
        
        # Execute subtraction
        shi -= divisor * b
        shang = shang * 10 + b
        
        trace.add_step("subtract_volume", [divisor, b], shi, annotation="shi -= divisor * b", cost=1)
        
        # Coefficient Update
        fangfa = divisor + b * lianfa + 2 * (b**2) * xiafa
        lianfa = lianfa + 3 * b * xiafa
        
        trace.add_step("update_coefficients", [b], {"fangfa": fangfa, "lianfa": lianfa}, cost=3)
        
        # Place Value Shift
        fangfa //= 10
        lianfa //= 100
        xiafa //= 1000
        
        trace.add_step("shift_board", [], {"fangfa": fangfa, "lianfa": lianfa, "xiafa": xiafa}, cost=0)
        step_num += 1
        
    trace.add_step("final_result", [], shang, annotation=f"Remainder: {shi}", cost=0)
    return trace

if __name__ == "__main__":
    t = chinese_cube_root(1860872)
    print(t)
