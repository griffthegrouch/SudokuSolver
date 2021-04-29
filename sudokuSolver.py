import tkinter as tk

count = 0
# defining unsolved board
unsolved_board = [
    [5, 3, 0,   0, 7, 0,    0, 0, 0],
    [6, 0, 0,   1, 9, 5,    0, 0, 0],
    [0, 9, 8,   0, 0, 0,    0, 6, 0],

    [8, 0, 0,   0, 6, 0,    0, 0, 3],
    [4, 0, 0,   8, 0, 3,    0, 0, 1],
    [7, 0, 0,   0, 2, 0,    0, 0, 6],

    [0, 6, 0,   0, 0, 0,    2, 8, 0],
    [0, 0, 0,   4, 1, 9,    0, 0, 0],
    [0, 0, 0,   0, 8, 0,    0, 7, 9]
]

# saving working copy of board to solve on
board = unsolved_board


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
        self.solve_btn = tk.Button(self, text="Solve\n(click me)", fg="green", command=self.solve)
        self.solve_btn.pack(side="top")

        self.quit_btn = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_btn.pack(side="top")

    def solve(self):
        print("starting to solve board...")
        solve_board()
        self.fill_board()

    def draw_board(self):
        # function draws the sudoku grid
        global canvas

        colour1 = "#f4fac3"
        colour2 = "#c5faf0"

        canvas.create_rectangle(50, 50, 200, 200,
                                outline="#fb0", fill=colour1)
        canvas.create_rectangle(200, 50, 350, 200,
                                outline="#fb0", fill=colour2)
        canvas.create_rectangle(350, 50, 500, 200,
                                outline="#fb0", fill=colour1)

        canvas.create_rectangle(50, 200, 200, 350,
                                outline="#fb0", fill=colour2)
        canvas.create_rectangle(200, 200, 350, 350,
                                outline="#fb0", fill=colour1)
        canvas.create_rectangle(350, 200, 500, 350,
                                outline="#fb0", fill=colour2)

        canvas.create_rectangle(50, 350, 200, 500,
                                outline="#fb0", fill=colour1)
        canvas.create_rectangle(200, 350, 350, 500,
                                outline="#fb0", fill=colour2)
        canvas.create_rectangle(350, 350, 500, 500,
                                outline="#fb0", fill=colour1)

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

    def fill_board(self):
        # put all board values into a long array, as they're stored as a 2d array
        global canvas
        global board

        values = []
        for element1 in board:
            for element2 in element1:
                values.append(element2)

        # offset labels because of the size of each text
        lblx = 13
        lbly = 5
        for i in range(81):
            if i % 9 == 0:
                lblx = 13
                lbly += 50
            lblx += 50
            text = values[i]
            if values[i] == 0:
                text = None
            label1 = tk.Label(canvas, text=text, fg="black", font=("Helvetica", 25))
            label1.place(x=lblx, y=lbly)

        canvas.pack(fill=tk.BOTH, expand=1)


def solve_board():
    # solves sudoku board
    global board
    global count

    count += 1
    print(count)
    print("working on it!!")
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(y, x, n):
                        board[y][x] = n
                        solve_board()

                        board[y][x] = 0
                return
    print("phew .. done.")

def is_possible(y, x, n):

    global board

    # checks vertically and horizontally if the number exists
    for i in range(9):
        if board[y][i] == n or board[x][i] == n:
            return False

    # checks all blocks inside of square if number exists
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[y0 + i][x0 + j] == n:
                return False
    return True

if __name__ == '__main__':
    # main flow
    # 1 define one sudoku problem
    # 2 save working copy of board
    # 3 draw board
    # 4 fill board with unsolved sudoku problem
    # 5 solve working copy of board
    # 6 display solved board


    # creating display instance
    root = tk.Tk()
    app = SudokuDisplay(master=root)
    canvas = tk.Canvas(app)

    # displaying board
    app.draw_board()

    # filling board with unsolved problem
    app.fill_board()

    app.mainloop()
