
import random
import math
import exception


actions = [0,1,2]

class Player():
    game_score = random.randint(25,50)



    @staticmethod
    def reset_game_score():
        Player.game_score = random.randint(25,50)


    def __init__(self, name) -> None:
        self.name = name
        self.previus_action = -1


    def make_move(self,action):
        self.current_move = action


    def commit_move(self):
        self.previus_action = self.current_move
        if self.current_move == 0:

            Player.game_score -= 4

            # Player.game_score //= 2

            # if(Player.game_score == 0):
            #     Player.game_score = 1
            
        elif self.current_move == 1:
            Player.game_score += 2

        elif self.current_move == 2:
            Player.game_score -= 3

        

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.isHuman = False

    def get_oppositive_action(self, action):
        if action == 0:
            return 1
        elif action == 1:
            return 2
        else:
            return 0
        
    def score(self, ai_turn, depth:int):
        if ai_turn:
            return 10 - depth
        else:
            return depth -10                       
    

    def minimax(self,depth, ai_turn):
        if Player.game_score == 0 or depth == 0:
            return self.score(ai_turn, depth)
        
        score = []
        moves = []

        for operation in actions:
            if operation != self.previus_action:
                super().make_move(operation)
                super().commit_move()
                score.append(self.score(ai_turn,depth))
                turn = True if ai_turn == False else False
                self.minimax(depth - 1 , turn)
                moves.append(operation)

        if ai_turn:
            max_score = score.index(max(score))
            move = moves[max_score]
            print(score[max_score])
            return score[max_score]

        else:
            max_score = score.index(min(score))
            move = moves[max_score]
            return score[max_score]

        # if ai_turn: 
        #     score = -math.inf
        #     for operation in actions:
        #         print("Operation: " + str(operation))
        #         if operation != self.previus_action:
        #             super().make_move(operation)
        #             super().commit_move()
        #             val = self.minimax(depth - 1 , False)
        #             score = max(score, val)
        #     return score
        
        # else:
        #     score = +math.inf
        #     for operation in actions:
        #         if operation != self.previus_action:
        #             super().make_move(operation)
        #             super().commit_move()
        #             val = self.minimax(depth - 1 , True)
        #             # print(val)
        #             score = min(score, val)
        #     return score

    def make_move(self):
        score = -math.inf
        best_operation = None
        game_score = Player.game_score

        for operation in actions:
            print("-------------------")
            super().make_move(operation)
            val = self.minimax(10,False)
            print("val внешний: " + str(val))
            super().commit_move()
            if val > score:
                score = val
                best_operation = operation

        # for val in self.minimax(10,False):
        #     print(val)


        # print(best_operation)
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
                self._make_move(int(input("Выбери действие(0 - Минус 4, 1 - Плюс 2, 2 - Минус 3): ")))
            except exception.IncorecctAction as IA:
                continue

            except exception.UsedActionTwice as UAT:
                continue
            flag= False

    def _make_move(self, action_from:int):
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
            
            if self.game_logic.getGameScore == 0:
                flag = False

            self.game_logic.switch_turn()
        
        self.winner()


        

if __name__ == "__main__":
    Terminal_play().play()