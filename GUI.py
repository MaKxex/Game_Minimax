import time
from tkinter import Frame, Tk, Label, Button, LabelFrame,Radiobutton, IntVar, Entry
import webbrowser
from game import Game
import exception

WINDOW_SIZE = 500

class gui:

    def __init__(self):
        self.root = Tk()
        self.game_mode = IntVar() # 0 Human vs Human, 1 Human vs AI
        self.game_logic = Game()
        self.config()
        self.start_page()
        self.root.mainloop()

    def config(self):
        self.width = WINDOW_SIZE
        self.height = WINDOW_SIZE
        self.root.geometry(str(self.width) + "x" + str(self.height))
        self.root.title("Game")
        self.frame = Frame(self.root)
        self.frame.pack(side="top", expand=True, fill="both")

    def clearFrame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    def start_page(self):
        self.clearFrame()
        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))

        lf = LabelFrame(self.frame,text="Welcome")
        Radiobutton(lf, text="Human vs Human",value=0, variable=self.game_mode).pack(padx=10, pady=1)
        Radiobutton(lf, text="Human vs AI",value=1, variable=self.game_mode).pack(padx=10, pady=10)
        Button(lf,text="Rules",command=self.rules_page).pack(padx=10, pady=10)
        Button(lf,text="Play",command=self.set_name).pack(padx=10, pady=10)
        Label(lf, text="Made by: Makxex").pack(pady=10, padx=10)
        link = Label(lf, text="https://github.com/MaKxex")
        link.pack(padx=2, pady=2)
        link.bind("<Button-1>", callback)
        link.configure(underline=True)
        lf.place(anchor="c", relx=.5, rely=.5)

    def rules_page(self):
        self.clearFrame()
        print(self.game_mode.get())
        lf = LabelFrame(self.frame, text="Rules")
        Label(lf,text="adwwadawdadw").pack(padx=10, pady=10)
        Button(lf, text="Back to menu", command=self.start_page).pack(padx=10, pady=10)
        lf.place(anchor="c", relx=.5, rely=.5)


    def set_name(self):
        self.clearFrame()

        players = []

        if self.game_mode.get() == 0:
            players.append(self.game_logic.createHumanPlayer("Player 1"))
            players.append(self.game_logic.createHumanPlayer("Player 2"))
        else:
            players.append(self.game_logic.createHumanPlayer("Player 1"))
            players.append(self.game_logic.createAiPlayer("AI"))
        self.game_logic.players = players

        self.base_window()
            


    def base_window(self):
        self.clearFrame()

        print(self.game_logic.players)


        if self.game_logic.getGameScore() == 0:
            Label(self.frame, text=f"Congratulations {self.game_logic.players[1].name} won!!!").pack(padx=10, pady=10)
            Button(self.frame, text="Back to menu", command=self.start_page).pack(padx=10, pady=10)
        else:   

            print(self.game_logic.getGameScore())
            game_score = self.game_logic.getGameScore()
            player_name = self.game_logic.getCurrentPlayer().name

            Label(self.frame, text="Game score: ").pack(padx=10, pady=10)
            Label(self.frame, text=f"{game_score}").pack(padx=10, pady=10)

            Label(self.frame, text=f"{player_name} turns").pack(padx=10, pady=10)
            Label(self.frame, text="choose action").pack(padx=10, pady=10)
            
            if not self.game_logic.getCurrentPlayer().isHuman:
                self.AI_turn()
            else:
                try:
                    Button(self.frame, text="div 2", command=self.div2).pack(padx=10, pady=10)
                    Button(self.frame, text="add 2", command=self.add2).pack(padx=10, pady=10)
                    Button(self.frame, text="sub 2", command=self.sub2).pack(padx=10, pady=10)
                except exception.UsedActionTwice as UAT:
                    Label(self.frame, text="Use another acrion").pack(padx=10, pady=10)


    def AI_turn(self):
        self.game_logic.getCurrentPlayer().make_move()
        self.game_logic.switch_turn()
        self.base_window()

    def div2(self):
        self.game_logic.getCurrentPlayer()._make_move(0)
        self.game_logic.switch_turn()
        self.base_window()


    def add2(self):
        self.game_logic.getCurrentPlayer()._make_move(1)
        self.game_logic.switch_turn()
        self.base_window()


    def sub2(self):
        self.game_logic.getCurrentPlayer()._make_move(2)
        self.game_logic.switch_turn()
        self.base_window()


if __name__ == "__main__":
    gui()