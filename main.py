import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe v2.0")
        self.root.resizable(True, False)
        self.root.wm_minsize(500, False)

        self.root.configure(bg="black")

        self.x_score = 0
        self.o_score = 0
        self.current_player = "X"
        self.count = 0

        self.menu_bar()

        self.display_score()
        self.display_label("Ready to play?")
        self.display_board()

    def menu_bar(self):
        self.menu_bar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menu_bar, tearoff=0)
        self.filemenu.add_command(label="Play Again", command=self.play_again)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.filemenu)
        self.root.config(menu=self.menu_bar)

    def display_score(self):
        display_frame = tk.Frame(self.root, bg="black")
        display_frame.pack()

        self.score = tk.Label(
            display_frame,
            text=f"X : {self.x_score}\t\tO : {self.o_score}",
            fg="white",
            bg="black",
            font=("Montserrat", 18),
        )
        self.score.grid(row=0, columnspan=5, pady=15)

    def display_label(self, initial_text):
        display_frame = tk.Frame(self.root, bg="black")
        display_frame.pack()

        self.label = tk.Label(
            display_frame,
            text=initial_text,
            bg="black",
            fg="white",
            width=25,
            font=("Montserrat", 26),
        )
        self.label.grid(row=1, columnspan=3, pady=10)

    def display_board(self):
        button_frame = tk.Frame(self.root, relief=tk.RAISED, bg="black")
        button_frame.pack(pady=45)

        self.buttons = []

        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    button_frame,
                    text=" ",
                    height=2,
                    width=3,
                    font=("Montserrat", 40),
                    command=lambda row=row, col=col: self.on_button_click(
                        self.buttons[row * 3 + col]
                    ),
                )
                button.grid(row=row, column=col)
                self.buttons.append(button)

    def on_button_click(self, button):
        if button["text"] == " " and self.current_player == "X":
            button["text"] = "X"
            self.current_player = "O"
            button["fg"] = "red"
            self.count += 1
            self.label.config(text=f"{self.current_player}' turn")
            self.check_winner()

        elif button["text"] == " " and self.current_player == "O":
            button["text"] = "O"
            self.current_player = "X"
            button["fg"] = "blue"
            self.label.config(text=f"{self.current_player}' turn")
            self.count += 1
            self.check_winner()
        else:
            messagebox.showwarning("Tic-Tac-Toe", "This field is already populated.")

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # rows
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # columns
            [0, 4, 8],
            [2, 4, 6],  # diagonals
        ]

        for combination in winning_combinations:
            symbol1 = self.buttons[combination[0]]["text"]
            symbol2 = self.buttons[combination[1]]["text"]
            symbol3 = self.buttons[combination[2]]["text"]

            if symbol1 == symbol2 == symbol3 != " ":
                self.label.config(text=f"{symbol1} wins!")

                if symbol1 == "X":
                    self.x_score += 1
                else:
                    self.o_score += 1

                self.score.config(text=f"X : {self.x_score}\t\tO : {self.o_score}")
                self.disable_all_buttons()

            if self.count == 9:
                self.label.config(text="Draw!")
                self.disable_all_buttons()

    def play_again(self):
        for button in self.buttons:
            button.configure(state="normal", text=" ")
            self.count = 0
            self.current_player = "X"
            self.label.config(text=f"{self.current_player}' turn")

    def disable_all_buttons(self):
        for button in self.buttons:
            button.configure(state="disabled")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = TicTacToe()
    app.run()
