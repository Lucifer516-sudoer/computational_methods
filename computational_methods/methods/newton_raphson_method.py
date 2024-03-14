from decimal import Decimal
from typing import Literal
from rich import print
from sympy.parsing.sympy_parser import parse_expr
from sympy import Float, pretty, symbols
from dataclasses import dataclass


@dataclass
class FunctionResult:
    input: int | float | Decimal
    output: int | float | Decimal | None = None
    output_sign: Literal["+", "-", None] = None

    def __repr__(self) -> str:
        return f"f({self.input}) = {self.output} (Sign: {self.output_sign})"


@dataclass
class NumRange:
    start: float | int
    stop: float | int


def nrm(
    function: str,
    num_range: NumRange,
    decimal_places: int,
):
    fx = parse_expr(s=function, evaluate=False)  # raw func
    simplified_fx = fx.simplify()
    diff_fx = fx.diff()
    # Printing out the information to the user

    # Print `Given` to the screen

    print(f"Given function: f(x) => \n{pretty(fx)}")
    print()
    print(f"Simplified function: f(x) => \n{pretty(simplified_fx)}")
    print()
    print(f"Now: f'(x) => \n{pretty(diff_fx)}")
    print()

    #
    # Step 1
    #
    # Checking the root range
    # by substituting values like 0, 1, 2,3 ... 
    prev_number = None

    print("=====================")
    print(
        f"Now checking for the root range:\nGiven Range: {num_range.start} -> {num_range.stop}"
    )

    # Root range
    root_range: list[FunctionResult] = []

    for number in range(num_range.start, num_range.stop + 1):
        res = float(simplified_fx.subs({"x": number}))
        current_number = FunctionResult(
            input=number,
            output=round(res, decimal_places),
            output_sign="+" if float(res) >= 0 else "-",
        )
        prev_number = current_number if prev_number is None else prev_number
        print(current_number)
        print()
        if prev_number.output_sign != current_number.output_sign:
            print(f"Sign change found between: {prev_number} & {current_number}")
            root_range.extend([prev_number, current_number])
            break
        else:
            prev_number = current_number

    #
    # Step 2
    #
    # finding x0
    x0 = round(
        ((int(root_range[0].input) + int(root_range[1].input)) / 2), decimal_places
    )
    root_found: bool = False

    xn = symbols("x")
    x = xn - (fx / diff_fx)
    iteration: int = 0

    print("By Newton-Raphson Method:")
    print(f"[bold blue]{pretty(x)}[/]")
    print("Now, finding the root:")
    while not root_found:
        current_output = round(float(x.subs({"x": x0})), decimal_places)
        print(f"\tx_[bold italic green]{iteration}[/] = {x0}")

        if current_output == x0:
            root_found = True
            print()
            print(f"Root found: [bold yellow]{current_output}[/]")

        x0 = current_output
        iteration += 1


if __name__ == "__main__":
    nrm("(3*x) - cos(x) - 1", num_range=NumRange(0, 10), decimal_places=6)
