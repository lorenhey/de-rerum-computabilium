"""
Suanpan (Chinese Abacus) Addition.
Traces the physical bead movements.
"""
from de_rerum_computabilium.core.trace import Trace

class SuanpanColumn:
    def __init__(self):
        self.heaven = 0 # 0 to 2 (each worth 5)
        self.earth = 0  # 0 to 5 (each worth 1)
        
    def add(self, value: int, trace: Trace, col_idx: int) -> int:
        carry = 0
        original_val = self.value()
        
        # Add earth beads
        self.earth += (value % 5)
        trace.add_step(f"move_earth_beads_col_{col_idx}", [original_val, value % 5], self.earth, annotation=f"Move {value % 5} earth beads up", cost=1)
        
        if self.earth >= 5:
            self.earth -= 5
            self.heaven += 1
            trace.add_step(f"carry_earth_to_heaven_col_{col_idx}", [], {"earth": self.earth, "heaven": self.heaven}, annotation="Earth beads full, clear 5 earth, move 1 heaven bead down", cost=1)
            
        # Add heaven beads
        self.heaven += (value // 5)
        if value // 5 > 0:
            trace.add_step(f"move_heaven_beads_col_{col_idx}", [], self.heaven, annotation=f"Move {value // 5} heaven beads down", cost=1)
            
        if self.heaven >= 2:
            self.heaven -= 2
            carry = 1
            trace.add_step(f"carry_heaven_col_{col_idx}", [], carry, annotation="Heaven beads full (10), clear heaven, carry 1 to next column", cost=1)
            
        return carry
        
    def value(self):
        return self.heaven * 5 + self.earth

def suanpan_addition(a: int, b: int) -> Trace:
    trace = Trace(method_name="Suanpan (Abacus) Addition", historical_era="Ming Dynasty China (c. 14th Century)")
    
    trace.add_step("init", [a, b], {"a": a, "b": b}, cost=0)
    
    # Initialize columns (enough for result)
    max_len = max(len(str(a)), len(str(b))) + 1
    columns = [SuanpanColumn() for _ in range(max_len)]
    
    # Set initial state 'a'
    str_a = str(a)[::-1]
    for i, char in enumerate(str_a):
        val = int(char)
        columns[i].heaven = val // 5
        columns[i].earth = val % 5
        
    trace.add_step("set_initial_state", [a], [c.value() for c in columns][::-1], annotation="Set number 'a' on the abacus", cost=0)
    
    # Add 'b'
    str_b = str(b)[::-1]
    carry = 0
    for i in range(max_len):
        b_val = int(str_b[i]) if i < len(str_b) else 0
        total_to_add = b_val + carry
        if total_to_add > 0:
            trace.add_step(f"processing_col_{i}", [], total_to_add, annotation=f"Adding {total_to_add} to column 10^{i}", cost=0)
            carry = columns[i].add(total_to_add, trace, i)
            
    # Read result
    result = 0
    for i, col in enumerate(columns):
        result += col.value() * (10 ** i)
        
    trace.add_step("read_result", [], result, annotation="Read final bead positions", cost=0)
    
    return trace

if __name__ == "__main__":
    t = suanpan_addition(274, 189)
    print(t)
