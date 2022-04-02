import numpy as np
import random


#creates a 4x4 board with an initial number (2 or 4) at a random location.
#returns a 4x4 numpy array
def startGame():
    startingArray = np.zeros((4,4))
    randomRange = [0,1,2,3]
    randomNumberChoice = [2,4]

    #starting position of first number
    randomX = random.choice(randomRange)
    randomY = random.choice(randomRange)
    #either 2 or 4
    randomInitNum = random.choice(randomNumberChoice)
    #print(randomX, randomY)
    

    for x in range (0, len(startingArray)):
        #print(startingArray[x])
        for i in range (0, len(startingArray)):
            #print (startingArray[x][i])

            if (x == randomY and i == randomX):
                #place initial number in random coordinates
                startingArray[x][i] = randomInitNum
        
    return startingArray

#print(startGame())
    