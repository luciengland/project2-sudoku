import clingo

from sudoku_board import Sudoku


def format_model(model: clingo.solving.Model) -> str:
    """Return a Clingo Sudoku model in the formatted board layout."""
    return str(Sudoku.from_model(model))
