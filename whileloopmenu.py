kitchenCount=0
bedroomCount=0
livingroomCount=0
washroomCount=0

print("you enter the house.")

while kitchenCount==0 or bedroomCount==0 or livingroomCount==0 or washroomCount==0:
  choice=input("What room would you like to go to? ")
  if choice=="kitchen":
    kitchenCount+=1
    print("you enter the kitchen")
    if kitchenCount==1:
      print("you see a knife on the table")
    else:
      print("you already saw everything here")
  elif choice=="bedroom":
    bedroomCount+=1
    print("you enter the bedroom")
  elif choice=="livingroom":
    livingroomCount+=1
    print("you enter the livingroom")
  elif choice=="washroom":
    washroomCount+=1
    print("you enter the washroom")
  else:
    print("Bad selection")

print("you've been in each room")
