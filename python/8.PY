light = input("Enter traffic light color: ").lower()

if light == "red":
    print("STOP!")
elif light == "yellow":
    print("Prepare to stop")
elif light == "green":
    print("You can go")
else:
    print("Wrong input!")
