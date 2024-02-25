
# from decimal import Decimal
# from typing import Literal
# from rich import print
# from sympy.parsing.sympy_parser import parse_expr
# from sympy import pretty, symbols, diff
# from dataclasses import dataclass

# @dataclass
# class FunctionResult:
#     input_value: int | float | Decimal
#     output_value: int | float | Decimal | None = None
#     output_sign: Literal["+", "-", None] = None

#     def __repr__(self) -> str:
#         return f"f({self.input_value}) = {self.output_value} (Sign: {self.output_sign})"

# @dataclass
# class NumRange:
#     start: float | int
#     stop: float | int

# def get_derivative(expression):
#     return diff(expression)

# def evaluate_function(expression, x_value):
#     return expression.subs({"x": x_value})

# def find_root_range(expression, num_range):
#     prev_result = None
#     root_range = []

#     for x_value in range(num_range.start, num_range.stop + 1):
#         output_value = evaluate_function(expression, x_value)
#         current_result = FunctionResult(
#             input_value=x_value,
#             output_value=output_value,
#             output_sign="+" if output_value >= 0 else "-"
#         )

#         if prev_result and prev_result.output_sign != current_result.output_sign:
#             print(f"Sign change found between: {prev_result} & {current_result}")
#             root_range.extend([prev_result, current_result])
#             break

#         prev_result = current_result

#     return root_range

# def newton_raphson_iteration(expression, x_value):
#     xn = symbols("x")
#     derivative = get_derivative(expression)
#     iteration_formula = xn - (expression / derivative)

#     return round(float(iteration_formula.subs({"x": x_value})), 4)

# def nrm(function_str, num_range=NumRange(-10, 10), decimal_places=4, tolerance=1e-8):
#     function_expression = parse_expr(function_str, evaluate=False)
    
#     print(f"Given function: f(x) => \n{pretty(function_expression)}")

#     simplified_expression = function_expression.simplify()
#     print(f"Simplified function: f(x) => \n{pretty(simplified_expression)}")

#     root_range = find_root_range(simplified_expression, num_range)
#     if not root_range:
#         print("No root range found within the given range.")
#         return

#     x0 = round((root_range[0].input_value + root_range[1].input_value) / 2, decimal_places)
#     print(f"Initial guess (x0): {x0}")

#     iteration_count = 0
#     root_found = False

#     while not root_found:
#         current_output = newton_raphson_iteration(function_expression, x0)
#         print(f"Iteration: x_{iteration_count} = {current_output}")

#         if abs(current_output - x0) < tolerance:
#             root_found = True
#             print(f"Root found: {current_output}")
#         x0 = current_output
#         iteration_count += 1

# # nrm("x**3 - 6*x + 4", num_range=NumRange(0, 10))

# nrm("(x*(log(x))) - 1.2", num_range=NumRange(0, 10), decimal_places=6)

from decimal import Decimal
from typing import Literal
from rich import print
from sympy.parsing.sympy_parser import parse_expr
from sympy import pretty, symbols, diff, log
from dataclasses import dataclass

@dataclass
class FunctionResult:
    input_value: int | float | Decimal
    output_value: int | float | Decimal | None = None
    output_sign: Literal["+", "-", None] = None

    def __repr__(self) -> str:
        return f"f({self.input_value}) = {self.output_value} (Sign: {self.output_sign})"

@dataclass
class NumRange:
    start: float | int
    stop: float | int

def get_derivative(expression):
    return diff(expression)

def evaluate_function(expression, x_value):
    try:
        return expression.subs({"x": x_value})
    except Exception as e:
        print(f"Error evaluating function at x={x_value}: {e}")
        return None

def find_root_range(expression, num_range):
    prev_result = None
    root_range = []

    for x_value in range(num_range.start, num_range.stop + 1):
        output_value = evaluate_function(expression, x_value)

        if output_value is None:
            continue  # Skip invalid values

        current_result = FunctionResult(
            input_value=x_value,
            output_value=float(output_value),
            output_sign="+" if float(output_value) >= 0 else "-"
        )

        if prev_result and prev_result.output_sign != current_result.output_sign:
            print(f"Sign change found between: {prev_result} & {current_result}")
            root_range.extend([prev_result, current_result])
            break

        prev_result = current_result

    return root_range

def newton_raphson_iteration(expression, x_value):
    xn = symbols("x")
    derivative = get_derivative(expression)

    try:
        iteration_formula = xn - (expression / derivative)
        new_x_value = round(float(iteration_formula.subs({"x": x_value})), 4)
        return new_x_value
    except Exception as e:
        print(f"Error during iteration at x={x_value}: {e}")
        return None

def nrm(function_str, num_range=NumRange(-10, 10), decimal_places=4, tolerance=1e-8):
    function_expression = parse_expr(function_str, evaluate=False)
    
    print(f"Given function: f(x) => \n{pretty(function_expression)}")

    simplified_expression = function_expression.simplify()
    print(f"Simplified function: f(x) => \n{pretty(simplified_expression)}")

    root_range = find_root_range(simplified_expression, num_range)
    if not root_range:
        print("No root range found within the given range.")
        return

    x0 = round((root_range[0].input_value + root_range[1].input_value) / 2, decimal_places)
    print(f"Initial guess (x0): {x0}")

    iteration_count = 0
    root_found = False

    while not root_found:
        current_output = newton_raphson_iteration(function_expression, x0)
        if current_output is None:
            break  # Stop if an error occurred during iteration

        print(f"Iteration: x_{iteration_count} = {current_output}")

        if abs(current_output - x0) < tolerance:
            root_found = True
            print(f"Root found: {current_output}")
        x0 = current_output
        iteration_count += 1

nrm("(x*(log(x))) - 1.2", num_range=NumRange(0, 10))
