from playsound import playsound
import time
counter = 0
while True:
    counter += 1
    print(counter)
    playsound('assets/sounds/service-bell_daniel_simon.mp3')
    time.sleep(2)