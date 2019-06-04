command = ""
while command != "quit":
    command = input(">>").lower()
    if command == "start":
        print("Start the car.")
    elif command == "stop":
        print("Stop the car.")
    elif command == "help":
        print("""
                Start-to start the car
                stop-to stop the car
                quit-to quit the game""")
    else:
        print("Sorry i don't understand that")