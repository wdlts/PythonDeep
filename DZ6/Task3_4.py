import random

def check_queens(pos):
    for i in range(8):
        for j in range(i+1, 8):
            if pos[i] == pos[j] or pos[i] - i == pos[j] - j or pos[i] + i == pos[j] + j:
                return False
    return True


def get_pos():
    pos = list(range(1, 9))
    for i in range(4):
        random.shuffle(pos)
        while not check_queens(pos):
            random.shuffle(pos)
        print(pos)

get_pos()
