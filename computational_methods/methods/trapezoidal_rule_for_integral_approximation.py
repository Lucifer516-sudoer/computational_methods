"""
Trapezoidal Rule:
    This method is used to approximate an integral function

     b
    /
    | f(x) dx = (h / 2) * [(y0 + yn) + 2(y1 + y2 + y3 + ... + yn-1)]
    |
    /
    a

"""

from typing import Any
from sympy import symbols


class FunctionTable:
    def __init__(
        self, x_values: list[int | float | Any], y_values: list[int | float | Any]
    ) -> None:
        self.x_values: list[int | float | Any] = x_values
        self.y_values: list[int | float | Any] = y_values

    
    @property
    def mapping(self):
        return dict(
            zip(self.x_values,
                self.y_values)
        )