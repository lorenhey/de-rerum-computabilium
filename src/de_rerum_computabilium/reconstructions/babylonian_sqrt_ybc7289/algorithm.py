"""
Babylonian Calculation of √2 (YBC 7289).
"""
from fractions import Fraction
from de_rerum_computabilium.core.trace import Trace
from de_rerum_computabilium.core.arithmetic import Sexagesimal

def to_sexagesimal_string(frac: Fraction, precision: int=4) -> str:
    integer_part = int(frac)
    remainder = frac - integer_part
    fractions_list = []
    for _ in range(precision):
        remainder *= 60
        digit = int(remainder)
        fractions_list.append(str(digit))
        remainder -= Fraction(digit)
    return f"{integer_part};" + ",".join(fractions_list)

def babylonian_sqrt(S: int, initial_guess: Fraction, iterations: int = 2, precision: int = 4) -> Trace:
    trace = Trace(method_name="Babylonian Square Root", historical_era="Old Babylonian (c. 1800-1600 BC)")
    
    S_frac = Fraction(S)
    x = initial_guess
    
    trace.add_step(
        operation="initial_guess",
        operands=[S_frac],
        result=x,
        precision=to_sexagesimal_string(x, precision),
        cost=0
    )
    
    for i in range(iterations):
        # S / x (requires table lookup historically, we simulate cost 1)
        div = S_frac / x
        trace.add_step("divide", [S_frac, x], div, to_sexagesimal_string(div, precision), annotation="Historical lookup of reciprocal and multiply", cost=2)
        
        # x + S / x
        add = x + div
        trace.add_step("add", [x, div], add, to_sexagesimal_string(add, precision), cost=1)
        
        # multiply by 1/2 (which is 0;30)
        x = Fraction(1, 2) * add
        trace.add_step("halve", [add], x, to_sexagesimal_string(x, precision), cost=1)
        
    return trace

if __name__ == "__main__":
    t = babylonian_sqrt(2, Fraction(3, 2), iterations=2)
    print(t)
