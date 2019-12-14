import random
deck='1d 2d 3d 4d 5d 6d 7d 8d 9d 10d jackd queend kingd 1h 2h 3h 4h 5h 6h 7h 8h 9h 10h jackh queenh kingh 1c 2c 3c 4c 5c 6c 7c 8c 9c 10c jackc queenc kingc 1l 2l 3l 4l 5l 6l 7l 8l 9l 10l jackl queenl kingl'.split()
deckExpanded=[]
for each in deck:
    
    if (each[-1]=="l"):
        deckExpanded.append(each[:-1]+' of leaves')

    if (each[-1]=="d"):
        deckExpanded.append(each[:-1]+' of diamonds')

    if (each[-1]=="c"):
        deckExpanded.append(each[:-1]+' of cloves')

    if (each[-1]=="h"):
        deckExpanded.append(each[:-1]+' of hearts')



random.shuffle(deckExpanded)
hou.ui.displayMessage("Your hand has "+deckExpanded[0]+', '+deckExpanded[1]+' and '+deckExpanded[2]+'\nYour opponent has '+deckExpanded[3]+', '+deckExpanded[4]+' and '+deckExpanded[5])
