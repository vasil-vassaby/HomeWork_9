total = 150
new_game = False


def get_total():  # для получения общего количества конфет
    global total
    return total


def take_candies(take: int):  # для определения количества конфет после хода игрока
    global total
    total -= take


def game():
    global new_game
    return new_game


def restart():
    global new_game
    global total
    if new_game:
        new_game = False
    else:
        total = 150
        new_game = True
