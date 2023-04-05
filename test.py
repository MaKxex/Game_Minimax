import sys


class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def make_move(self, action):
        if action == "div2":
            self.value //= 2
        elif action == "add2":
            self.value += 2
        elif action == "sub2":
            self.value -= 2


class HumanPlayer(Player):
    def make_move(self):
        valid_input = False
        while not valid_input:
            action = input(f"{self.name}, make your move (div2, add2, sub2): ")
            if action in ["div2", "add2", "sub2"]:
                super().make_move(action)
                valid_input = True
            else:
                print("Invalid input. Please enter div2, add2, or sub2.")


class ComputerPlayer(Player):
    def minimax(self,depth, is_max):
        if depth == 0 or self.value == 0:
            return self.value

        if is_max:
            best_value = float('-inf')
            for action in ["div2", "add2", "sub2"]:
                super().make_move(action)
                value = self.minimax(depth -1,False)
                # super().make_move(self.opposite_action(action))
                best_value = max(best_value, value)
            return best_value
        else:
            best_value = float('inf')
            for action in ["div2", "add2", "sub2"]:
                super().make_move(action)
                value = self.minimax(depth -1,True)
                # super().make_move(self.opposite_action(action))
                best_value = min(best_value, value)
            return best_value

    def opposite_action(self, action):
        if action == "div2":
            return "add2"
        elif action == "add2":
            return "sub2"
        elif action == "sub2":
            return "add2"

    def make_move(self):
        best_value = float('-inf')
        best_action = None
        for action in ["div2", "add2", "sub2"]:
            super().make_move(action)
            value = self.minimax(16,False)
            super().make_move(self.opposite_action(action))
            if value > best_value:
                best_value = value
                best_action = action
        super().make_move(best_action)
        print(f"{self.name} makes move: {best_action}")



class Game:
    def __init__(self):
        self.players = [HumanPlayer("Player 1", 1), ComputerPlayer("Computer", 2)]
        self.current_player = self.players[0]
        self.other_player = self.players[1]
        self.game_over = False
        self.winner = None

    def play(self):
        self.current_player.set_value(10)
        self.other_player.set_value(10)
        while not self.game_over:
            print(self.current_player.name + ": "+ str(self.current_player.value))
            self.current_player.make_move()
            if self.current_player.get_value() == 0:
                self.winner = self.current_player
                self.game_over = True
                break
            self.current_player, self.other_player = self.other_player, self.current_player
        print(f"Game over! Winner: {self.winner.name}")



game = Game()
game.play()