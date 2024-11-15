roomList=["Hall", "Study", "Bedroom","Kitchen","Washroom"]
location="Hall"
clock=9
inventory=["Watch"]
kitchenItems=["Knife","Coffee"]
solved=False

#FUNCTION FOR EACH ROOM

def goToHall():
  global location
  global clock
  global inventory
  location = ""
  while location not in roomList:
    location=input("You are in the Hall. It is " + str(clock) + ":00. Where would you like to go? ")

def goToStudy():
  global location
  global clock
  global inventory
  print("You are in the Study. You hear a loud noise from the washroom. You run there")
  location="Washroom"
  #Here i ddin't increment the time, you can choose when to/not to increment the time

def goToBedroom():
  global location
  global clock
  global inventory
  global solved
  print("You are in the Bedroom.")
  if clock <12:
    print("Agatha is here. But she's sound asleep. You try to wake her but she won't wake up.")
    print("YOu decide to go back to the hall.")
    location="Hall"
    clock+=1
  else:
    print("Agatha is here. She is sitting up in bed. She says 'Oh hello, if you get me a coffee, I will tell you who the murderer is'")
    if "Coffee" in inventory:
      inventory.remove("Coffee")
      print("Thanks, she says, as she takes the coffee. She screams 'I DID IT. HE WAS MAKING SO MUCH NOISE AND I WAS TRYING TO SLEEP'")
      solved=True
    else:
      print("Unfortunately you don't have any coffee.")


def goToKitchen():
  global location
  global clock
  global kitchenItems
  print("You are in the Kitchen.")
  if "Coffee" in kitchenItems:
    print("There's a coffee on the counter. You pick it up")
    kitchenItems.remove("Coffee")
    inventory.append("Coffee")
    while True:
      answer=input("Would you like to drink it? (y/n): ")
      if answer=="y":
        print("Glug Glug Glug")
        break
        inventory.remove("Coffee")
      elif answer=="n":
        print("Ok. You decide to save it for later.")
        break
  print("There's nothing else to do here, so you go back to the Hall.")
  location="Hall"
  clock+1

def goToWashroom():
  global location
  global clock
  print("You are in the Washroom. You do a number 2. Lets go back to the hall")
  clock+=1
  location="Hall"





#MAIN LOOP
while clock<17 and solved==False:
  if location == "Hall":
    goToHall()
  elif location == "Study":
    goToStudy()
  elif location == "Bedroom":
    goToBedroom()
  elif location == "Kitchen":
    goToKitchen()
  elif location == "Washroom":
    goToWashroom()

if solved == True:
  print("It is " + str(clock) + ":00. You did it")
else:
  print("It is " + str(clock) + ":00. You failed to solve the murder.")
