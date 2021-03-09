"""
John Napier's Logarithms Construction (1614/1619).
"""
import math
from de_rerum_computabilium.core.trace import Trace

class NapierTableBuilder:
    def __init__(self, radius: int = 10_000_000):
        self.radius = radius
        self.trace = Trace(method_name="Napier's Logarithm Table Construction", historical_era="Early Modern (1614)")

    def build_first_table(self):
        """First table: 101 values. Proportion: 1 - 1/10^7"""
        table = [float(self.radius)]
        self.trace.add_step("init_first_table", [self.radius], table[0], cost=0)
        
        for i in range(1, 101):
            prev = table[-1]
            # historically: a subtraction and shifting decimal point
            sub_val = prev / 10_000_000
            new_val = prev - sub_val
            table.append(new_val)
            self.trace.add_step("subtract_proportion", [prev, 10_000_000], new_val, annotation=f"First table row {i}", cost=1)
            
        return table

    def build_second_table(self):
        """Second table: 51 values. Proportion: 1 - 1/10^5"""
        table = [float(self.radius)]
        self.trace.add_step("init_second_table", [self.radius], table[0], cost=0)
        
        for i in range(1, 51):
            prev = table[-1]
            sub_val = prev / 100_000
            new_val = prev - sub_val
            table.append(new_val)
            self.trace.add_step("subtract_proportion", [prev, 100_000], new_val, annotation=f"Second table row {i}", cost=1)
            
        return table
        
    def build_third_table_skeleton(self):
        """Third table: 69 columns, 21 rows (just demonstrating the first few)."""
        columns = []
        col_start = float(self.radius)
        # We only do 3 columns here to avoid massive trace sizes in test
        for c in range(3):
            col = [col_start]
            for r in range(1, 21):
                prev = col[-1]
                sub_val = prev / 2000
                new_val = prev - sub_val
                col.append(new_val)
                self.trace.add_step("subtract_proportion", [prev, 2000], new_val, annotation=f"Third table col {c} row {r}", cost=1)
            columns.append(col)
            # Next column
            col_start = col_start - col_start / 100
            self.trace.add_step("subtract_proportion", [col_start, 100], col_start, annotation=f"Third table col {c+1} start", cost=1)
            
        return columns

def modern_napier_log(x: float, radius: int = 10_000_000) -> float:
    return radius * math.log(radius / x)

if __name__ == "__main__":
    builder = NapierTableBuilder()
    builder.build_first_table()
    builder.build_second_table()
    builder.build_third_table_skeleton()
    print(f"Total manual subtractions logged: {builder.trace.total_cost()}")
