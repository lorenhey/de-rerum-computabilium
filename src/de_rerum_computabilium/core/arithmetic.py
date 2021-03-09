"""
Historical arithmetic types.
"""
from typing import List, Union

class Sexagesimal:
    """
    Represents a base-60 number, often used in Babylonian and Hellenistic astronomy.
    Stored as a list of integers, where the index defines the power of 60.
    For simplicity, we'll store it as (integer_part, fractional_part).
    integer_part is [..., 60^1, 60^0]
    fractional_part is [60^-1, 60^-2, ...]
    """
    def __init__(self, integer_part: List[int], fractional_part: List[int]):
        self.integer_part = integer_part
        self.fractional_part = fractional_part

    @classmethod
    def from_float(cls, value: float, precision: int = 4):
        """Convert a modern float to Sexagesimal up to `precision` fractional places."""
        integer_val = int(value)
        
        int_parts = []
        if integer_val == 0:
            int_parts = [0]
        else:
            temp = integer_val
            while temp > 0:
                int_parts.insert(0, temp % 60)
                temp //= 60
                
        frac_parts = []
        rem = value - integer_val
        for _ in range(precision):
            rem *= 60
            part = int(rem)
            frac_parts.append(part)
            rem -= part
            
        return cls(int_parts, frac_parts)
        
    def to_float(self) -> float:
        val = 0.0
        # Integer part
        for i, digit in enumerate(reversed(self.integer_part)):
            val += digit * (60 ** i)
        # Fractional part
        for i, digit in enumerate(self.fractional_part):
            val += digit * (60 ** -(i + 1))
        return val

    def __str__(self):
        int_str = ",".join(str(d) for d in self.integer_part)
        if self.fractional_part:
            frac_str = ",".join(str(d) for d in self.fractional_part)
            return f"{int_str};{frac_str}"
        return int_str

    def __repr__(self):
        return f"Sexagesimal({self})"

class FixedDecimal:
    """
    Historical fixed-precision decimal arithmetic.
    Used for 17th-19th century table makers where intermediate calculations
    are rounded/truncated to a specific number of decimal places.
    """
    def __init__(self, value: float, places: int = 7):
        self.places = places
        # Store as integer to avoid float issues
        self._internal = int(round(value * (10 ** places)))

    def to_float(self) -> float:
        return self._internal / (10 ** self.places)

    def __add__(self, other):
        if not isinstance(other, FixedDecimal) or self.places != other.places:
            raise ValueError("Must add FixedDecimal of same precision")
        res = FixedDecimal(0, self.places)
        res._internal = self._internal + other._internal
        return res

    def __sub__(self, other):
        if not isinstance(other, FixedDecimal) or self.places != other.places:
            raise ValueError("Must subtract FixedDecimal of same precision")
        res = FixedDecimal(0, self.places)
        res._internal = self._internal - other._internal
        return res

    def __mul__(self, other):
        # Multiplication in fixed point usually requires rounding the result back to `places`
        if not isinstance(other, FixedDecimal) or self.places != other.places:
            raise ValueError("Must multiply FixedDecimal of same precision")
        res = FixedDecimal(0, self.places)
        # (A * 10^p) * (B * 10^p) = (A*B) * 10^2p
        # To get back to 10^p, we divide by 10^p and round
        temp = self._internal * other._internal
        # round half away from zero
        res._internal = int(round(temp / (10 ** self.places)))
        return res

    def __str__(self):
        s = str(abs(self._internal)).zfill(self.places + 1)
        sign = "-" if self._internal < 0 else ""
        return f"{sign}{s[:-self.places]}.{s[-self.places:]}"
