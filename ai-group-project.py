import numpy as np
import random

class protectTurn():
    protect = []

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
    print("Starting array: ")
    print(startingArray)
    return startingArray

#print(startGame())



#takes an array and a direction ("up", "down", "left", "right").
#moves the board in said direction recursively.
#adds together numbers that are equal.
#
#finally, adds a random number (2,4) to an empty space in the board after moving.
turnProtect = protectTurn()
def movement(array, direction):

    #if modified is set to 1, function will call itself recursively
    #until there are no more modifications.
    modified = 0
    protectEle = 0

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
                        #if elements have been added together this turn.
                        #Protect that element from changing until next turn.
                        for j in range (0,len(turnProtect.protect)):
                            if (((x-1),i) or (x,i) == turnProtect.protect[j] ):
                                protectEle = 1
                                #print(new.protect[j])

                        #free to combine, no protection
                        if protectEle == 0:
                            array[x-1][i] = array[x][i] * 2
                            array[x][i] = 0
                            #add position to the protected array.
                            turnProtect.protect.append(((x-1),i))

                        #print("appending: ")
                        #print(x-1,i)
                            modified = 1

        #recursion                
        if (modified):
            movement(array, "up")
        else:
            #Empty protect array for next pass
            turnProtect.protect = []

            #add a number(2,4) into one of the remaining 0's.
            #returns array
            print("Printing results after \"up\"")
            addRandomNum(array)
            print(array)
            
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
                        for j in range (0,len(turnProtect.protect)):
                            if ((x,(i-1)) or (x,i) == turnProtect.protect[j]):
                                protectEle = 1

                        if protectEle == 0:
                            array[x][i-1] = array[x][i] * 2
                            array[x][i] = 0

                            turnProtect.protect.append((x, (i-1)))

                            modified = 1

        if (modified):
            movement(array, "left")
        else:
            turnProtect.protect = []

            #for clarity, show direction and resulting board
            print("Printing results after \"left\"")
            addRandomNum(array)
            print(array)

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
                        for j in range (0,len(turnProtect.protect)):
                            if (((x+1),i) or (x,i) == turnProtect.protect[j]):
                                protectEle = 1

                        if protectEle == 0:
                            array[x+1][i] = array[x][i] * 2
                            array[x][i] = 0

                            turnProtect.protect.append(((x+1),i))

                            modified = 1


        if (modified):
            movement(array, "down")
        else:
            turnProtect.protect = []
            print("Printing results after \"down\"")
            addRandomNum(array)
            print(array)
            

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
                        for j in range (0,len(turnProtect.protect)):
                            if ((x,(i+1)) or (x,i) == turnProtect.protect[j]):
                                protectEle = 1

                        if protectEle == 0:
                            array[x][i+1] = array[x][i] * 2
                            array[x][i] = 0

                            turnProtect.protect.append((x,(i+1)))

                            modified = 1

        if (modified):
            movement(array, "right")
        else:
            turnProtect.protect = []
            print("Printing results after \"right\"")
            addRandomNum(array)
            print(array)

    #returns array after given direction
    return array

#Helper function for movement().
#fills an array 'availableSpots' with coordinates of 0's in the array.
#Randomly chooses from coordinates in the array and changes that coordinate to either a 2 or 4
def addRandomNum(array):
    availableSpots = []
    randomNumberChoice = [2,4]
    randomNum = random.choice(randomNumberChoice)

    for x in range (0, len(array)):
        for i in range (0, len(array)):
            if(array[x][i] == 0):
                availableSpots.append((x,i))

    newNumPos = random.choice(availableSpots)
    array[newNumPos[0]][newNumPos[1]] = randomNum

    return array


practice = np.array ([  [4, 0, 2, 2],
                        [0, 0, 0, 2],
                        [0, 0, 4, 0],
                        [0, 0, 0, 2]    ])

#startingArray = startGame()
#secondPassDirection = movement(startingArray, "down")
#thirdPassDirection = movement(secondPassDirection, "left")
#fourthPassDirection = movement(thirdPassDirection, "right")
#fifthPassDirection = movement(fourthPassDirection, "up")
fifthPassDirection = movement(practice, "right")


