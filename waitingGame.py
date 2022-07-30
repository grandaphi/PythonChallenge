#  a game where the user is given a target time and  prompted to press enter to
#  start. The user is then to be prompted to press enter again when they believe 
#  the target time has elapsed. The program assesses the accuracy of the user's 
#  timing; too fast, too slow,(both with the time difference) or right on 
#  target. We will assume 3 decimal places will be accurate enough
import random
import time 

milli = 1E3
nano = 1E9
tolerance = 0.1



def waitingGame():
    targetTime = round(random.random()*3)+1
    print("Your target time is:", targetTime, "s")
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
            totalTime =round((endTime - startTime)/nano)
            timeDiff = round(totalTime - targetTime,3)
            print("your time is", totalTime,"s")
            if abs(timeDiff)< tolerance:
                print("Congrats, you win! Your time is within",tolerance, "s of the target time, with a difference of",timeDiff, "s")
            else:
                print("Sorry, you lose. Your time isn't within", tolerance, "s of the target time, with a difference of:",timeDiff, "s")
            
    except:
        print("Error, try again, only press 'enter'.")
        waitingGame()

    finally:
        pass

waitingGame()

