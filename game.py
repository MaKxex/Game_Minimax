import random
import math


actions = [1,2]


class Player:
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
    def calc_min(self):
        pass

    def calc_max(self):
        pass

    def minimax(self,depth, ai_turn):
        if Player.game_score == 0 or depth == 0:
            return Player.game_score
        
        if ai_turn: 
            score = -math.inf
            for operation in actions:
                super().make_move(operation)
                if self.previus_action == self.current_move:
                    break
                super().commit_move()
                val = self.minimax(depth -1 , False)
                score = max(score, val)
            return score
        
        else:
            score = +math.inf
            for operation in actions:
                super().make_move(operation)
                if self.previus_action == self.current_move:
                    break
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
            val = self.minimax(15,False)
            # if self.previus_action == self.current_move:
            #     return -math.inf
            super().commit_move()
            if val > score:
                score = val
                best_operation = operation
        # print(game_score)
        # print(best_operation)
        Player.game_score = game_score
        super().make_move(best_operation)

        super().commit_move()


        print(f"{self.name} выбирает {best_operation}" )



class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_move(self):
        print(self.name + " Твой ход!")
        action = -1
        while action < 0 or action > 2:
            try:
                action = int(input("Выбери действие(0 - Делить на 2, 1 - Плюс 2, 2 - Минус 2): "))
                super().make_move(action)
                # print("asd")
                if self.current_move == self.previus_action:
                    print("Нельзя использовать эту команду дважды!")
                    raise Exception
                
                super().commit_move()
            except Exception as e:
                pass


class Game:
    def __init__(self) -> None:
        self.players = [Human("player 1"), Human("Comp 2")]


    
    def play(self):
        flag = True

        current_player = self.players[0]
        second_player = self.players[1]


        while flag:

            print("|" + "Игровой счет: " + str(Player.game_score)+ "|")

            print("------------------")
            current_player.make_move()

            if Player.game_score == 0:
                flag = False
                break

            current_player, second_player = second_player, current_player

        print(current_player.name + " Ты выйграл!!!")
        
Game().play()