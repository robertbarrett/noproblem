roomList=["Hall", "Study", "Bedroom","Kitchen","Washroom"]
location="Hall"
clock=9
while clock<17:
  if location == "Hall":
    location = ""
    while location not in roomList:
      location=input("You are in the Hall. It is " + str(clock) + ":00. Where would you like to go? ")
  elif location == "Study":
    print("You are in the Study. Lets go back to the hall")
    clock+=1
    location="Hall"
  elif location == "Bedroom":
    print("You are in the Bedroom. Lets go back to the hall")
    clock+=1
    location="Hall"
  elif location == "Kitchen":
    print("You are in the Kitchen. Lets go back to the hall")
    clock+=1
    location="Hall"
  elif location == "Washroom":
    print("You are in the Washroom. You do a number 2. Lets go back to the hall")
    clock+=1
    location="Hall"

print("It is " + str(clock) + ":00. You failed to solve the murder.")
