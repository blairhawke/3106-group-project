import numpy as np
import random

#change the array for testing
practiceArray = np.array([      [0,1,1,1], 
                                [2,2,0,0], 
                                [2,0,0,4], 
                                [2,2,0,0] ])

#creates a 4x4 board with an initial number (2 or 4) at a random location.
#returns a 4x4 numpy array
def startGame():
    startingArray = np.zeros((4,4))
    randomRange = [0,1,2,3]
    randomNumberChoice = [2,4]

    #starting position of first number
    randomY = random.choice(randomRange)
    randomX = random.choice(randomRange)
    #either 2 or 4
    randomInitNum = random.choice(randomNumberChoice)
    #print(randomX, randomY)
    

    for x in range (0, len(startingArray)):
        #print(startingArray[x])
        for i in range (0, len(startingArray)):
            #print (startingArray[x][i])

            if (x == randomX and i == randomY):
                #place initial number in random coordinates
                startingArray[x][i] = randomInitNum
    print(startingArray)
    return startingArray

#print(startGame())


#takes an array and a direction ("up", "down", "left", "right").
#moves the board in said direction recursively.
#adds numbers that are equal.
def movement(array, direction):

    #if modified is set to 1, function will call itself recursively
    #until there are no more modifications.
    modified = 0

    if (direction == "up"):
        #loop array
        for x in range (0, len(array)):
            for i in range (0, len(array)):
                #number to be moved
                if (array[x][i] > 0):
                    #wall
                    if(x == 0):
                        continue
                    
                    #move up if there is a 0 above
                    if (array[x-1][i] == 0):
                        array[x-1][i] = array[x][i]
                        array[x][i] = 0

                        modified = 1

                    #elements are equal.
                    #add together
                    elif (array[x-1][i] == array[x][i]):
                        array[x-1][i] = array[x][i] * 2
                        array[x][i] = 0

                        modified = 1

                    else:
                        #just for testing
                        print("problem up")
        #recursion                
        if (modified):
            movement(array, "up")
            
    if (direction == "left"):

        for x in range (0, len(array)):
            for i in range (0, len(array)):

                if (array[x][i] > 0):
                    if(i == 0):
                        continue

                    if (array[x][i-1] == 0):
                        array[x][i-1] = array[x][i]
                        array[x][i] = 0

                        modified = 1
                        
                    elif(array[x][i-1] == array[x][i]):
                        array[x][i-1] = array[x][i] * 2
                        array[x][i] = 0

                        modified = 1

                    else:

                        print("problem left")
        if (modified):
            movement(array, "left")

    if (direction == "down"):
        #direction "down" and "right" traverse the array backwards,
        #this is in order for the added numbers to land in the correct spot.
        for x in range (len(array) -1, -1, -1):
            for i in range (len(array) -1, -1, -1):

                if (array[x][i] > 0):
                    if(x == 3):
                        continue

                    if (array[x+1][i] == 0):
                        array[x+1][i] = array[x][i]
                        array[x][i] = 0

                        modified = 1

                    elif(array[x+1][i] == array[x][i]):
                        array[x+1][i] = array[x][i] * 2
                        array[x][i] = 0

                        modified = 1

                    else:
                        print("problem down")

        if (modified):
            movement(array, "down")

    if (direction == "right"):

        for x in range (len(array) -1, -1, -1):
            for i in range (len(array) -1, -1, -1):

                if (array[x][i] > 0):
                    if(i == 3):
                        continue

                    if (array[x][i+1] == 0):
                        array[x][i+1] = array[x][i]
                        array[x][i] = 0

                        modified = 1

                    elif(array[x][i+1] == array[x][i]):
                        array[x][i+1] = array[x][i] * 2
                        array[x][i] = 0

                        modified = 1

                    else:
                        print("problem right")

        if (modified):
            movement(array, "right")
    
    return array


#print(movement(practiceArray, "right"))