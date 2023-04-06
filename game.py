
import random
import math
import exception


actions = [0,1,2]

class Player():
    game_score = random.randint(25,50)


    def __init__(self, name) -> None:
        self.name = name
        self.previus_action = -1


    def make_move(self,action):
        self.current_move = action


    def commit_move(self):
        self.previus_action = self.current_move
        if self.current_move == 0:
                
            Player.game_score //= 2

            if(Player.game_score == 0):
                Player.game_score = 1
            
        elif self.current_move == 1:
            Player.game_score += 2

        elif self.current_move == 2:
            Player.game_score -= 2
        

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.isHuman = False

    def minimax(self,depth, ai_turn):
        if Player.game_score == 0 or depth == 0:
            return Player.game_score
        
        if ai_turn: 
            score = -math.inf
            for operation in actions:
                super().make_move(operation)
                super().commit_move()
                val = self.minimax(depth -1 , False)
                score = max(score, val)
            return score
        
        else:
            score = +math.inf
            for operation in actions:
                super().make_move(operation)
                super().commit_move()
                val = self.minimax(depth -1 , True)
                score = min(score, val)
            return score

    def make_move(self):
        score = -math.inf
        best_operation = None
        game_score = Player.game_score
        # print(game_score)
        for operation in actions:
            super().make_move(operation)
            val = self.minimax(5,False)
            super().commit_move()
            print(val)
            if val > score:
                score = val
                best_operation = operation

        Player.game_score = game_score
        super().make_move(best_operation)

        super().commit_move()


        print(f"{self.name} выбирает {best_operation}" )



class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.isHuman = True

    def make_move(self):
        flag = True
        while flag:
            try:
                self._make_move(int(input("Выбери действие(0 - Делить на 2, 1 - Плюс 2, 2 - Минус 2): ")))
            except exception.IncorecctAction as IA:
                continue

            except exception.UsedActionTwice as UAT:
                continue
            flag= False

    def _make_move(self, action_from:int):
        print(self.name + " Твой ход!")
        action = -1

        if  action_from > 3 or action_from < 0:
            raise exception.IncorecctAction

        action = action_from
        super().make_move(action)
        if self.current_move == self.previus_action:
            print("Нельзя использовать эту команду дважды!")
            raise exception.UsedActionTwice
        
        super().commit_move()


class Game:
    def __init__(self) -> None:
        self.players = []


    def createHumanPlayer(self, name):
        return Human(name)

    def createAiPlayer(self,name):
        return AI(name)


    def switch_turn(self):
        self.players.reverse()
        # current_player, second_player = second_player, current_player

    def winner(self):
        print(self.players[0].name + " Ты выйграл!!!")


    def isGameOver(self):
        if Player.game_score == 0:
            return True

    def getGameScore(self):
        return Player.game_score
    
    def getCurrentPlayer(self) -> Player:
        return self.players[0]


    def play(self): # terminal use 
        flag = True
        while flag:

            print("|" + "Игровой счет: " + str(Player.game_score)+ "|")
            print("------------------")
            self.getCurrentPlayer().make_move()
            
            if self.isGameOver():
                flag = False

            self.switch_turn()
        self.winner()
        

if __name__ == "__main__":
    Game().play()