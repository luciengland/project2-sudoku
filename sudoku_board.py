from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        rows = []
        for row in range(1, 10):
            cells = []
            for column in range(1, 10):
                value = self.sudoku.get((row, column), "-")
                cells.append(str(value))
            rows.append(
                " ".join(cells[:3])
                + "  "
                + " ".join(cells[3:6])
                + "  "
                + " ".join(cells[6:])
            )

        return "\n\n".join(
            "\n".join(rows[start:start + 3]) for start in range(0, 9, 3)
        )

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        # get all atoms
        atoms = model.symbols(shown=True)
        # get row, column, value of each atom
        for atom in atoms:
            row = atom.arguments[0].number
            column = atom.arguments[1].number
            value = atom.arguments[2].number
            # store value using row/column key
            sudoku[(row,column)] = value
        return cls(sudoku)
