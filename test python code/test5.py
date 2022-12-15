import threading as th
import time

secondes = 0
heures = 0

input = "stop"

def test(input) :
    while input == "start" :
        global secondes, minutes, heures
        print("il est : "+str(heures)+":"+str(minutes)+":"+str(secondes))
        secondes+=1
        time.sleep(0.001)

        if secondes >= 60 :
            secondes = 0
            minutes+= 1
        if minutes >= 60 :
            minutes = 0
            heures+= 1


test("start")
t = th.Thread(target=test)
t.start()

time.sleep(10)

test("stop")