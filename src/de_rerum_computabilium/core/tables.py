"""
Historical table engines.
Simulates printed tables and finite difference computations.
"""
from typing import List, Callable, Tuple
import math

class DifferenceTable:
    """
    Computes and stores the finite differences of a sequence.
    Used for Babbage's difference engine and historical interpolation.
    """
    def __init__(self, values: List[float], order: int = 3):
        self.columns = [values]
        for _ in range(order):
            prev_col = self.columns[-1]
            if len(prev_col) <= 1:
                break
            new_col = [prev_col[i+1] - prev_col[i] for i in range(len(prev_col)-1)]
            self.columns.append(new_col)

    def print_table(self):
        max_len = len(self.columns[0])
        for i in range(max_len):
            row = []
            for col in self.columns:
                if i < len(col):
                    row.append(f"{col[i]:.6f}")
                else:
                    row.append("")
            print("\t".join(row))

class LookupTable:
    """
    A simulated printed table.
    Records cost of lookups and interpolations.
    """
    def __init__(self, name: str, domain: List[float], values: List[float]):
        self.name = name
        self.domain = domain
        self.values = values
        if len(domain) != len(values):
            raise ValueError("Domain and values must have same length")

    def lookup_nearest(self, x: float) -> Tuple[float, int]:
        """Returns the nearest tabulated value and the cost (1 lookup)."""
        # Bisection or linear scan (historical scan is O(N) or index-based)
        # We simulate index-based O(1) human lookup for well-structured tables.
        # But we record 1 unit of labor.
        nearest_idx = min(range(len(self.domain)), key=lambda i: abs(self.domain[i] - x))
        return self.values[nearest_idx], 1

    def lookup_linear_interpolate(self, x: float) -> Tuple[float, int]:
        """Returns interpolated value and cost (1 lookup + 1 diff + 1 mul + 1 add)."""
        # Find bracketing indices
        if x <= self.domain[0]:
            return self.values[0], 1
        if x >= self.domain[-1]:
            return self.values[-1], 1
            
        for i in range(len(self.domain) - 1):
            if self.domain[i] <= x <= self.domain[i+1]:
                x0, x1 = self.domain[i], self.domain[i+1]
                y0, y1 = self.values[i], self.values[i+1]
                
                # Formula: y = y0 + (x - x0) * (y1 - y0) / (x1 - x0)
                # Historical interpolation cost: lookup y0, y1 (or diff), calculate fraction.
                t = (x - x0) / (x1 - x0)
                y = y0 + t * (y1 - y0)
                # Cost: 2 lookups, 1 subtraction, 1 multiplication, 1 addition (approx 5)
                return y, 5
        return 0.0, 0
