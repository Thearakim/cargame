command = ""
started = False
while True:
    command = input(">>").lower()
    if command == "start":
        if started:
            print("The car have already started!!")
        else:
            started = True
            print("Start the car.")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!!")
        else:
            started = False
            print("Stop the car.")
    elif command == "help":
        print("""
                Start-to start the car
                stop-to stop the car
                quit-to quit the game""")
    elif command =="quit":
        break
    else:
        print("Sorry i don't understand that")
