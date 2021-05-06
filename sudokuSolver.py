import time
import tkinter as tk
import screenReader

count = 0

# defining unsolved board
unsolved_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# saving working copy of board to solve on
grid = unsolved_board
solved_board = grid


class SudokuDisplay(tk.Frame):
    def __init__(self, master=None):
        # initialize window and canvas
        super().__init__(master)
        self.master = master
        master.geometry("600x600")
        self.pack(fill="both", expand=True, side="top")
        self.create_widgets()

    def create_widgets(self):
        # creates solve and quit buttons
        self.solve_btn = tk.Button(self, text="Solve\n(click me)", fg="green", command=solve)
        self.solve_btn.pack(side="top")

        self.quit_btn = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_btn.pack(side="top")

        self.get_board = tk.Button(self, text="Get Board", fg="blue", command=get_board)
        self.get_board.pack(side="top")

def draw_board():
        # function draws the sudoku grid

        # draws vertical lines
        canvas.create_line(0, 50, 0, 500)

        canvas.create_line(50, 50, 50, 500)
        canvas.create_line(100, 50, 100, 500)
        canvas.create_line(150, 50, 150, 500)
        canvas.create_line(200, 50, 200, 500)
        canvas.create_line(250, 50, 250, 500)
        canvas.create_line(300, 50, 300, 500)
        canvas.create_line(350, 50, 350, 500)
        canvas.create_line(400, 50, 400, 500)
        canvas.create_line(450, 50, 450, 500)
        canvas.create_line(500, 50, 500, 500)

        # draws horizontal lines
        canvas.create_line(50, 0, 500, 0)
        canvas.create_line(50, 50, 500, 50)
        canvas.create_line(50, 100, 500, 100)
        canvas.create_line(50, 150, 500, 150)
        canvas.create_line(50, 200, 500, 200)
        canvas.create_line(50, 250, 500, 250)
        canvas.create_line(50, 300, 500, 300)
        canvas.create_line(50, 350, 500, 350)
        canvas.create_line(50, 400, 500, 400)
        canvas.create_line(50, 450, 500, 450)
        canvas.create_line(50, 500, 500, 500)

        canvas.pack(fill=tk.BOTH, expand=1)


def get_board():
    # uses screen capture to get a sudoku board
    global grid
    grid = screenReader.getBoard()
    fill_board(grid)


def fill_board(board):
    # put all board values into a long array, as they're stored as a 2d array
    canvas.delete("all")
    draw_board()

    values = []
    for element1 in board:
        for element2 in element1:
            values.append(element2)

    # offset labels because of the size of each text
    lblx = 25
    lbly = 25
    for i in range(81):
        if i % 9 == 0:
            lblx = 25
            lbly += 50
        lblx += 50
        text = values[i]
        if values[i] == 0:
            text = None
        label1 = tk.Label(canvas, text=text, fg="black", font=("Helvetica", 25))
        canvas.create_window(lblx, lbly, window=label1)

    canvas.pack(fill=tk.BOTH, expand=1)

def solve():
    # solves current grid sudoku board and returns product
    fill_board(solve_grid())

def solve_grid():
    # solves sudoku board
    global grid
    global count
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                count += 1
                return
    solved_board = grid
    grid = unsolved_board
    return solved_board


def is_possible(y, x, n):
    # checks vertically and horizontally if the number exists
    for i in range(0, 9):
        if grid[y][i] == n or grid[i][x] == n:
            return False

    # checks all blocks inside of square if number exists
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


if __name__ == '__main__':
    # creating display instance
    root = tk.Tk()
    app = SudokuDisplay(master=root)
    canvas = tk.Canvas(app)

    # displaying board
    draw_board()

    # filling board with unsolved problem
    fill_board(grid)

    app.mainloop()
