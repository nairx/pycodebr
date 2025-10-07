flag = input("Enter signal")
match flag:
    case "green":
        print("Go")
    case "red":
        print("Stop")
    case "yellow":
        print("Slow down")
    case _:
        print("Error")