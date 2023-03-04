#  challenge: write a function to set an alarm
#  inputs: alarm time, alarm sound file to play, and alarm message to diplay
#  uses audio on replit.com for audio output. Linux and windows need other implementations

from replit import audio
import time, sched 

def playAlarm(file,msg):
    print(msg)
    string = ('./alarm_sounds/'+file)
    sound = audio.play_file(string)


def setAlarm(delay, file, message):
    sch =  sched.scheduler(time.time, time.sleep)
    sch.enter(10,1,playAlarm,argument=(file,message))
    sch.run()

delay,file,message = input("enter timedelay, file and message").split()
setAlarm(delay,file,message)