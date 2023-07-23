import tkinter as tk


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe v2.0")
        self.root.resizable(False, False)

    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
