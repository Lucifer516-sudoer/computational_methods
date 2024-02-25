# from decimal import Decimal
# from typing import Literal
from decimal import Decimal
from typing import Any
from sympy import nan, pretty, simplify, Eq, init_printing
# from dataclasses import dataclass

init_printing(use_unicode=True)

# @dataclass
# class NumberToRemember:
#     number: int | float | Decimal
#     x: int | float | Decimal | None = None
#     sign: Literal["+", "-", None] = None


# def fixed_point_iteration_method(
#     function: str,
#     start_range: float | int = -100,
#     stop_range: float | int = 100,
#     verbose: bool = True,
# ):

#     #
#     # Finding the root range
#     #
#     expr = simplify(function)
#     print(f"Given Expression: {expr}\n===============================")
#     prev_number = NumberToRemember(0)
#     root_range = []

#     for i in range(start_range, stop_range + 1):
#         current_number = NumberToRemember(0)
#         current_number.number = expr.subs({"x": i})
#         current_number.x = i
#         if current_number.number >= 0:
#             current_number.sign = "+"
#             print(f"{current_number} is +ve")
#         elif current_number.number <= 0:
#             current_number.sign = "-"
#             print(f"{current_number} is -ve")

#         print("=====================")


#         if prev_number.sign is None:
#             print(f"{prev_number} is None; Now: {current_number}")
#             prev_number = current_number

#         if prev_number.sign != current_number.sign:
#             print(f"{prev_number} is not as {current_number}\nSo adding it to the range list ...")
#             root_range.extend([prev_number.x, current_number.x])
#         print("====================")
#         prev_number = current_number


#     root_range = set(root_range)


# print(fixed_point_iteration_method("x^3 - 2*x + 5"))

e3 = simplify("5/((2*(x**2))*sqrt(2 - 5/x))")
e = simplify("x**3 -2*x +5")

prev_val: Any = None

run = True
for i in range(10):
    cur_val = e3.subs({"x": prev_val or -2.5})
    if prev_val is not None:
        print(f"Current Value: {cur_val}")
        if cur_val == prev_val:
            print(f"g(x) = {cur_val}")
            run = False

    prev_val = cur_val
