
import random
import math
import exception


class Player():
    game_score = random.randint(60,73)

    @staticmethod
    def reset_game_score():
        Player.game_score = random.randint(60,73)



    def __init__(self, name) -> None:
        self.name = name
        self.previus_action = -1


    def make_move(self,action):
        self.current_move = action


    def commit_move(self):
        self.previus_action = self.current_move
        Player.game_score -= self.current_move

        

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.isHuman = False
        
    def score(self, ai_turn):
        if ai_turn:
            return 10
        else:
            return - 10                       
    

    def get_prime_divisors(self,n): #find divisors 
        i = 2
        while i * i <= n:
            if n % i == 0:
                n /= i
                yield i
            else:
                i += 1

        if n > 1:
            yield int(n)


    def minimax(self,depth, ai_turn):
        if Player.game_score == 0:
            return self.score(ai_turn)


        if ai_turn: 
            score = -math.inf
            for operation in self.get_prime_divisors(Player.game_score):
                super().make_move(operation)
                super().commit_move()
                val = self.minimax(depth - 1 , False)
                score = min(score, val)
            return score
        
        else:
            score = +math.inf
            for operation in self.get_prime_divisors(Player.game_score):
                super().make_move(operation)
                super().commit_move()
                val = self.minimax(depth - 1 , True)
                # print(val)
                score = max(score, val)
            return score
        
    def make_move(self):
        print(f"{self.name} выбирает {self._make_move()}" )

    def _make_move(self):
        score = -math.inf
        best_operation = None
        game_score = Player.game_score

        for operation in self.get_prime_divisors(Player.game_score):
            super().make_move(operation)
            val = self.minimax(10,False)
            # print("val внешний: " + str(val))
            super().commit_move()
            if val > score:
                score = val
                best_operation = operation

        Player.game_score = game_score
        super().make_move(best_operation)
        super().commit_move()
        return best_operation




class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.isHuman = True

    def make_move(self):
        flag = True
        while flag:
            try:
                self._make_move(int(input("Введите положительный делитель счета (в том числе единицу или на само это число счета): ")))
            except exception.IncorecctAction as IA:
                continue

            flag= False

    def _make_move(self, action_from:int):
        action = -1

        if action_from == 0 or Player.game_score % action_from != 0:
            raise exception.IncorecctAction

        action = action_from
        super().make_move(action)

        # if self.current_move == self.previus_action:
        #     print("Нельзя использовать эту команду дважды!")
        #     raise exception.UsedActionTwice
        
        super().commit_move()


class Game:
    def __init__(self) -> None:
        self.players = []


    def reset(self):
        self.players = []
        Player.reset_game_score()


    def createHumanPlayer(self, name):
        return Human(name)

    def createAiPlayer(self,name):
        return AI(name)


    def switch_turn(self):
        self.players.reverse()
        # current_player, second_player = second_player, current_player

    def isGameOver(self):
        if Player.game_score == 0:
            return True

    def getGameScore(self):
        return Player.game_score
    
    def getCurrentPlayer(self) -> Player:
        return self.players[0]




class Terminal_play:
    def __init__(self) -> None:
        self.game_logic = Game()


    def ask_mode(self):
        val = -1
        while val < 0 or val > 1:
            val = int(input("Выберите режим игры (0 - Человек с Человеком, 1 - Человек с AI): "))

        self.set_players(val)

    def winner(self):
        print(self.game_logic.getCurrentPlayer().name+ " Ты выйграл!!!")

    def set_players(self, mode:int):
        players = []
        
        if mode == 0:
            players.append(self.game_logic.createHumanPlayer("Player 1"))
            players.append(self.game_logic.createHumanPlayer("Player 2"))
        else:
            players.append(self.game_logic.createHumanPlayer("Player 1"))
            players.append(self.game_logic.createAiPlayer("AI"))


        self.game_logic.players = players


    def play(self): # terminal use 
        flag = True

        self.ask_mode()

        while flag:
            print("------------------")
            print(self.game_logic.getCurrentPlayer().name + " Твой ход!")
            print("|" + "Игровой счет: " + str(Player.game_score)+ "|")

            if self.game_logic.getCurrentPlayer().isHuman:
                self.game_logic.getCurrentPlayer().make_move()

            else:
                self.game_logic.getCurrentPlayer().make_move()
            if self.game_logic.getGameScore() == 0:
                flag = False

            self.game_logic.switch_turn()
        
        self.winner()


        

if __name__ == "__main__":
    Terminal_play().play()