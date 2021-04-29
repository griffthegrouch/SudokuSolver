import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True, side="top")
        self.create_widgets()
        master.geometry("600x600")
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

    def draw_lines(self, canv):
        # function draws the sudoku grid

        colour1 = "#f4fac3"
        colour2 = "#c5faf0"

        canv.create_rectangle(50, 50, 200, 200,
                                outline="#fb0", fill=colour1)
        canv.create_rectangle(200, 50, 350, 200,
                                outline="#fb0", fill=colour2)
        canv.create_rectangle(350, 50, 500, 200,
                                outline="#fb0", fill=colour1)

        canv.create_rectangle(50, 200, 200, 350,
                                outline="#fb0", fill=colour2)
        canv.create_rectangle(200, 200, 350, 350,
                                outline="#fb0", fill=colour1)
        canv.create_rectangle(350, 200, 500, 350,
                                outline="#fb0", fill=colour2)

        canv.create_rectangle(50, 350, 200, 500,
                                outline="#fb0", fill=colour1)
        canv.create_rectangle(200, 350, 350, 500,
                                outline="#fb0", fill=colour2)
        canv.create_rectangle(350, 350, 500, 500,
                                outline="#fb0", fill=colour1)

        # draws vertical lines
        canv.create_line(0, 50, 0, 500)

        canv.create_line(50, 50, 50, 500)
        canv.create_line(100, 50, 100, 500)
        canv.create_line(150, 50, 150, 500)
        canv.create_line(200, 50, 200, 500)
        canv.create_line(250, 50, 250, 500)
        canv.create_line(300, 50, 300, 500)
        canv.create_line(350, 50, 350, 500)
        canv.create_line(400, 50, 400, 500)
        canv.create_line(450, 50, 450, 500)
        canv.create_line(500, 50, 500, 500)

        # draws horizontal lines
        canv.create_line(50, 0, 500, 0)
        canv.create_line(50, 50, 500, 50)
        canv.create_line(50, 100, 500, 100)
        canv.create_line(50, 150, 500, 150)
        canv.create_line(50, 200, 500, 200)
        canv.create_line(50, 250, 500, 250)
        canv.create_line(50, 300, 500, 300)
        canv.create_line(50, 350, 500, 350)
        canv.create_line(50, 400, 500, 400)
        canv.create_line(50, 450, 500, 450)
        canv.create_line(50, 500, 500, 500)

        canv.pack(fill=tk.BOTH, expand=1)

    def fill_board(self, board, canv) :
        # put all board values into a long array, as they're stored as a 2d array
        values = []
        for element1 in board:
            for element2 in element1:
                values.append(element2)

        # offset labels because of the size of each text
        lblx = 13
        lbly = 5
        for i in range(81):
            if ( i % 9 == 0):
                lblx = 13
                lbly += 50
            lblx += 50
            text = values[i]
            if(values[i] == 0):
                text = None
            label1 = tk.Label(canv, text=text, fg="black", font=("Helvetica", 25))
            label1.place(x=lblx, y=lbly)

        canv.pack(fill=tk.BOTH, expand=1)

#
# if __name__ == '__main__':
#
#     board1 = [
#         ['5', '3', 0, 0, '7', 0, 0, 0, 0],
#         ['6', 0, 0, '1', '9', '5', 0, 0, 0],
#         [0, '9', '8', 0, 0, 0, 0, '6', 0],
#
#         ['8', 0, 0, 0, '6', 0, 0, 0, '3'],
#         ['4', 0, 0, '8', 0, '3', 0, 0, '1'],
#         ['7', 0, 0, 0, '2', 0, 0, 0, '6'],
#
#         [0, '6', 0, 0, 0, 0, '2', '8', 0],
#         [0, 0, 0, '4', '1', '9', 0, 0, 0],
#         [0, 0, 0, 0, '8', 0, 0, '7', '9']
#     ]
#
#     root = tk.Tk()
#     app = Application(master=root)
#     canvas = tk.Canvas(app)
#     app.draw_lines(canvas)
#
#     app.fill_board(board1, canvas)
#
#     app.mainloop()
