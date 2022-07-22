#  a game where the user is given a target time and  prompted to press enter to
#  start. The user is then to be prompted to press enter again when they believe 
#  the target time has elapsed. The program assesses the accuracy of the user's 
#  timing; too fast, too slow,(both with the time difference) or right on 
#  target. We will assume 3 decimal places will be accurate enough
import time 

nano = 1E9

def waitingGame():
    try:
        inp = input("press enter to begin")
        startTime = time.time_ns()
        if inp:
            raise Exception("Please only press enter. Try again")
        else:
            inp  = input("Press enter again ")
            endTime = time.time_ns()
        if inp:
            raise Exception("Please only press enter. Try again")
        else:
            timeDiff = (endTime - startTime)/nano
            print("your time is", timeDiff)
    except:
        waitingGame()

    finally:
        pass

waitingGame()

