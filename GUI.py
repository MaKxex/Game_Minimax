import time
from tkinter import Frame, Tk, Label, Button, LabelFrame,Radiobutton, IntVar, Entry
import webbrowser
from game import Game

WINDOW_SIZE = [200,290]

class gui:

    def __init__(self):
        self.root = Tk()
        self.game_mode = IntVar() # 0 Human vs Human, 1 Human vs AI
        self.game_logic = Game()
        self.config()
        self.start_page()
        self.root.mainloop()

    def config(self):
        self.width = WINDOW_SIZE[0]
        self.height = WINDOW_SIZE[1]
        self.root.geometry(str(self.width) + "x" + str(self.height))
        self.root.title("Game")
        self.frame = Frame(self.root)
        self.frame.pack(side="top", expand=True, fill="both")

    def clearFrame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    def start_page(self):
        self.root.geometry(str(self.width) + "x" + str(self.height))
        self.clearFrame()
        self.game_logic.reset()

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
        self.root.geometry(str(500) + "x" + str(500))
        Label(lf,text="The game generates a score around 60,\n and players are allowed to make moves by decreasing a\n number by any of its positive integer divisors.\n Each time a player makes a move, he chooses a \ndivisor of the number and reduces it by that divisor. \nThe player who cannot make a move loses. \nThe goal of the game is to stay in the game as long as possible, \navoiding situations that could lead to defeat.").pack(padx=10, pady=10)
        Button(lf, text="Back to menu", command=self.start_page).pack(padx=10, pady=10)
        lf.place(anchor="c", relx=.5, rely=.5)


    def set_name(self):
        self.clearFrame()

        players = []

        if len(self.game_logic.players) == 0:
            if self.game_mode.get() == 0:
                players.append(self.game_logic.createHumanPlayer("Player 1"))
                players.append(self.game_logic.createHumanPlayer("Player 2"))
            else:
                players.append(self.game_logic.createHumanPlayer("Human"))
                players.append(self.game_logic.createAiPlayer("AI"))

            self.game_logic.players = players

        Label(self.frame, text=f"First Turn: {self.game_logic.players[0].name}").pack(padx=10, pady=10)
        Button(self.frame, text=f"Change first move", command=self.revers_turn).pack(padx=10, pady=10)
        Button(self.frame, text=f"Back", command=self.start_page).pack(padx=10, pady=10)
        Button(self.frame, text=f"Play", command=self.base_window).pack(padx=10, pady=10)
            
    def revers_turn(self):
        self.game_logic.players.reverse()
        self.set_name()
        


    def input_handle(self, event):

        self.game_logic.getCurrentPlayer()._make_move(int(self.inputF.get()))
        self.game_logic.switch_turn()
        self.base_window()


    def base_window(self):
        self.clearFrame()

        if self.game_logic.getGameScore() == 0:
            Label(self.frame, text=f"Congratulations {self.game_logic.players[0].name} won!!!").pack(padx=10, pady=10)
            Button(self.frame, text="Back to menu", command=self.start_page).pack(padx=10, pady=10)
        else:
            game_score = self.game_logic.getGameScore()
            player_name = self.game_logic.getCurrentPlayer().name

            Label(self.frame, text="Game score: ").pack(padx=10, pady=10)
            Label(self.frame, text=f"{game_score}").pack(padx=10, pady=10)

            Label(self.frame, text=f"{player_name} turns").pack(padx=10, pady=10)


            if False in [x.isHuman for x in self.game_logic.players]:
                if self.game_logic.getCurrentPlayer().isHuman:
                    turn = "None"
                    if self.game_logic.players[1].previus_action != -1:
                        turn = self.game_logic.players[1].previus_action
                    Label(self.frame, text=f"Last AI turn: {turn}").pack(padx=10, pady=10)
           
            Label(self.frame, text="choose action").pack(padx=10, pady=10)
            
            if not self.game_logic.getCurrentPlayer().isHuman:
                self.AI_turn()
            else:
                self.inputF = Entry(self.frame)
                self.inputF.pack(padx=10, pady=10)
                self.inputF.bind("<Return>", self.input_handle)
                self.inputF.focus_set()
                Button(self.frame, text="Back to menu", command=self.start_page).pack(padx=10, pady=10)


    def AI_turn(self):
        self.game_logic.getCurrentPlayer()._make_move()
        self.game_logic.switch_turn()
        self.base_window()



if __name__ == "__main__":
    gui()