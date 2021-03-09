"""
Prosthaphaeresis.
Multiplication via trigonometric tables (Tycho Brahe / Wittich, c. 1580s).
"""
import math
from de_rerum_computabilium.core.trace import Trace

class ProsthaphaeresisComputer:
    def __init__(self, radius: int = 10**7, resolution_minutes: int = 1):
        self.R = radius
        self.resolution = resolution_minutes
        self.table = {}
        self.trace = Trace(method_name="Prosthaphaeresis", historical_era="Late Renaissance (c. 1580s)")
        
        # Precompute the integer cosine table to simulate the historical artifact
        for minutes in range(0, 180 * 60 + 1, self.resolution):
            angle_rad = math.radians(minutes / 60.0)
            self.table[minutes] = int(round(self.R * math.cos(angle_rad)))

    def _reverse_lookup(self, value: int) -> int:
        best_angle = min(self.table.keys(), key=lambda k: abs(self.table[k] - value))
        self.trace.add_step("reverse_lookup", [value], best_angle, annotation="Find angle for scaled value", cost=1)
        return best_angle

    def multiply(self, X: float, Y: float) -> Trace:
        # Scaling
        def scale(val: float):
            power = math.floor(math.log10(val)) if val > 0 else 0
            target_digits = math.floor(math.log10(self.R))
            shift = target_digits - power - 1
            scaled_val = int(val * (10 ** shift))
            return scaled_val, shift

        x, x_shift = scale(X)
        y, y_shift = scale(Y)
        
        self.trace.add_step("scale", [X, Y], (x, y), annotation="Scale inputs to table range", cost=0)
        
        A = self._reverse_lookup(x)
        B = self._reverse_lookup(y)
        
        S = A + B
        D = abs(A - B)
        self.trace.add_step("angle_arithmetic", [A, B], (S, D), annotation="Sum and difference of angles", cost=2)
        
        u = self.table[S]
        v = self.table[D]
        self.trace.add_step("forward_lookup", [S, D], (u, v), annotation="Lookup cosines of S and D", cost=2)
        
        z = (u + v) // 2
        self.trace.add_step("prosthesis", [u, v], z, annotation="Add and halve (the multiplication core)", cost=2)
        
        result = z * self.R / (10 ** (x_shift + y_shift))
        self.trace.add_step("descale", [z], result, annotation="Adjust decimal point for final result", cost=0)
        
        return self.trace

if __name__ == "__main__":
    computer = ProsthaphaeresisComputer()
    t = computer.multiply(314.15, 271.82)
    print(t)
