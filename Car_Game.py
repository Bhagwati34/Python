cmd = ""
start = False
stop = False
while True:
    cmd = input("> ").upper()
    if cmd.upper() == "HELP":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif cmd == "START":
        if start:
            print("car is already started!")
        else:
            start = True
            print("car started ..... Ready to go!")
    elif cmd == "STOP":
        if stop:
            print("car already stopped!")
        else:
            stop = True
            print("car stopped.")
    elif cmd == "QUIT":
        break
    else:
        print("I don't understand that ........")
