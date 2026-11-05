import clingo
import clingo.application

# solver using clingo app class
class SudokuApp(clingo.application.Application):
    def main(self, control, files):
        # load sudoku files
        for file in files:
            control.load(file)
        # rules for solving sudoku
        sudoku_rules = """
            % /every cell contains one number between 1-9
            1 { sudoku(X,Y,N) : N=1..9 } 1 :- X=1..9, Y=1..9.
            % /don't change initial values 
            sudoku(X,Y,N) :- initial(X,Y,N).
            % no duplicate numbers in a row
            :- sudoku(X,Y1,N), sudoku(X,Y2,N), Y1 != Y2.
            % no duplicate numbers in a column
            :- sudoku(X1,Y,N), sudoku(X2,Y,N), X1 != X2.
            % no duplicate numbers in same 3x3 subgrid
            :- sudoku(X1,Y1,N), sudoku(X2,Y2,N), 
                    (X1-1)/3 == (X2-1)/3, (Y1-1)/3 == (Y2-1)/3, X1 < X2.
            #show sudoku/3.
        """

        # add sudoku rules to clingo program
        control.add("base", [], sudoku_rules)
        control.ground([("base", [])])
        # solve sudoku
        control.solve()
    # sort the output
    def print_model(self, model, printer):
        # get all atoms
        atoms = model.symbols(shown=True)
        # sort by row and columns
        sorted_atoms = sorted(atoms, key=lambda atom: (atom.arguments[0].number, atom.arguments[1].number))
        # print separated by spaces
        print(" ".join(str(atom) for atom in sorted_atoms))

if __name__ == "__main__":
    clingo.application.clingo_main(SudokuApp())

