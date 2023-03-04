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


def waiting_game():
    target_time = random.randint(1, 4)
    print("Your target time is:", target_time, "s")
    try:
        inp = input("press enter to begin")
        start_time = time.time_ns()
        if inp:
            raise Exception("Please only press enter. Try again")
        else:
            inp = input("Press enter again ")
            end_time = time.time_ns()
        if inp:
            raise Exception("Please only press enter. Try again")
        else:
            total_time = round((end_time - start_time) / nano, 3)
            time_diff = round(total_time - target_time, 3)
            print("your time is", total_time, "s")
            if abs(time_diff) < tolerance:
                print("Congrats, you win! Your time is within", tolerance,
                      "s of the target time, with a difference of", time_diff,
                      "s")
            else:
                print("Sorry, you lose. Your time isn't within", tolerance,
                      "s of the target time, with a difference of:", time_diff,
                      "s")

    except:
        print("Error, try again, only press 'enter'.")
        waiting_game()

    finally:
        pass


waiting_game()
