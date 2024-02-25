from typer import Typer
from rich import print
from computational_methods.methods.newton_raphson_method import NumRange, nrm

app = Typer()


@app.command()
def solve_by_nrm(
    function: str,
    start: int= -10,
    stop: int= 10,
    decimal_places: int = 4,
):
    nrm(
        function=function,
        num_range=NumRange(start, stop),
        decimal_places=decimal_places,
    )


@app.command()
def about():
    print("Author: Harish. V" "Version: 0.0.1" "App Name: Computational Methods")

app()