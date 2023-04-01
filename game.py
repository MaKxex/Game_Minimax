import random

class Player:
    game_score = random.randint(25,50)
    def __init__(self, name) -> None:
        self.name = name
        self.previus_action = -1


    def make_move(self,action):
        self.previus_action = action
        if action == 0:
            Player.game_score //= 2
        elif action == 1:
            Player.game_score += 2
        elif action == 3:
            Player.game_score -= 2
        


class AI(Player):
    def make_move(self):
        pass

class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_move(self):
        print(self.name + " Твой ход!")
        action = -1
        while action < 0 or action > 2:
            try:
                action = int(input("Выбери действие(0 - Делить на 2, 1 - Плюс 2, 2 - Минус 2): "))
            except Exception as e:
                pass
        super().make_move(action)

class Game:
    def __init__(self) -> None:
        self.players = [Human("player 1"), Human("player 2")]


    
    def play(self):
        flag = True

        current_player = self.players[0]
        second_player = self.players[1]


        while flag:
            
            print(current_player.previus_action)


            if (current_player.previus_action != -1):
                if (current_player.previus_action == second_player.previus_action) :
                    print("Нельзя использовать эту команду дважды!")
                    continue

            
            print("Игровой счёт: " + str(Player.game_score) + "\n")
            current_player.make_move()

            if Player.game_score == 0:
                flag = False
                break

            current_player, second_player = second_player, current_player

        print(current_player.name + " Ты выйграл!!!")
        
Game().play()