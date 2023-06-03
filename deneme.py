import random
def dusmanOluşturucu (level,oyuncu):
    dusman = {}
    for i in range(level+7):
        if oyuncu == 1:
            dusman[i] = [[random.randint(0,19)*30, random.randint(0,19)*-30],3]
        else:
            dusman[i] = [[random.randint(20, 39) * 30, random.randint(0, 19) * -30], 3]
    return dusman

def yetenekolusturucu(level,oyuncu)