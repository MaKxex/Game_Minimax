import math
import random

# Функция, которая определяет, является ли текущее значение конечным состоянием игры
def is_terminal_state(current_value):
    return current_value == 0

# Функция, которая возвращает список возможных действий для текущего состояния игры
def get_possible_actions(current_value):
    actions = []
    if current_value % 2 == 0:
        actions.append(current_value // 2)
    actions.append(current_value - 2)
    actions.append(current_value + 2)
    return actions

# Функция, которая вычисляет минимальную стоимость для компьютера
def min_value(current_value, alpha, beta, depth):
    if is_terminal_state(current_value):
        return 0
    min_val = math.inf
    for action in get_possible_actions(current_value):
        val = max_value(action, alpha, beta, depth - 1)
        min_val = min(min_val, val)
        beta = min(beta, val)
        if beta <= alpha:
            break
    return min_val

# Функция, которая вычисляет максимальную стоимость для игрока
def max_value(current_value, alpha, beta, depth):
    if is_terminal_state(current_value):
        return 0
    
    max_val = -math.inf
    for action in get_possible_actions(current_value):
        val = min_value(action, alpha, beta, depth - 1)
        max_val = max(max_val, val)
        alpha = max(alpha, val)
        if beta <= alpha:
            break
    return max_val

# Функция, которая выбирает лучшее действие для компьютера с помощью минимакс алгоритма
def computer_turn(current_value):
    print("Ход компьютера!")
    # print("Текущее значение: ", current_value)
    best_action = None
    best_score = -math.inf
    for action in get_possible_actions(current_value):
        score = min_value(action, -math.inf, math.inf, 3) # Глубина поиска = 3
        if score > best_score:
            best_score = score
            best_action = action
    current_value = best_action
    # print("Компьютер выбрал значение: ", current_value)
    return current_value

# Функция, которая запускает игру
def play_game():
    print("Начало игры!")
    current_value = random.randint(20, 30) # Случайное число от 20 до 30
    print("Загаданное число: ", current_value)
    while current_value != 0:
        choice = input("Ваш ход! Выберите операцию: деление на 2 (1), вычитание 2 (2), прибавление 2 (3): ")
        if choice == "1":
            current_value //= 2
        elif choice == "2":
            current_value -= 2
        elif choice == "3":
            current_value += 2
        else:
            print("Неправильный выбор! Попробуйте еще раз.")
            continue
        print("Текущее значение: ", current_value)
        if current_value == 0:
            print("Вы выиграли!")
            break
        current_value = computer_turn(current_value)
        print("Текущее значение: ", current_value)
        if current_value == 0:
            print("Компьютер выиграл!")
            break

play_game()