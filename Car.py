import time
import random

car_command = ""
started = False

while True:
    car_command = input("> ").lower()

    if car_command == "start":

        if started:
            print("Car is already running...")
        else:
            started = True

            print("You turn the key and nothing happens...")
            time.sleep(random.randint(1,3))
            print("The car makes a loud rumble and starts...")

    elif car_command == "stop":

        if not started:
            print("Car is already stopped...")
        else:
            started = False
            print("The car screeches to a stop...")


    elif car_command == "help":
        print("""
Start - to start the car
Stop - to stop the car
Quit - to exit the vehicle
    """)
    elif car_command.upper() == "QUIT":
        break

    else:
        print("Sorry, I do not understand")