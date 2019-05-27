import userModule
import pprint

pp = pprint.PrettyPrinter(indent=3)
userModule.welcomeMessage()
category = set(userModule.makeSelection())
#print(category)

choice = int(input("\nWould you like to convert your US dollars? \n1. Yes \n2. Not right now \n\n"))
while(choice >=1 and choice <=2):
  if(choice == 1):
    currentInput = int(input("Tell us how many US dollars you would like to conver to bitcoins \n"))
    bitcoins = userModule.convertCurrency(currentInput)
    print("You have ", bitcoins, " in your budget.")
    break
  elif choice == 2:
    print("\nNo worries, you will be able to do it during the payment process. Just remmember the prices are in bitcoins")
    break
  else:
    print("\nOnly 1(Yes) and 2(No) are valid choices")
    #choice = input("Would you like to convert your US dollars? \n1. Yes \n2. Not right now \n")

print("\nHere is what store has to offer you in the section you chose: \n")
pp.pprint(set(category))


#convert the set into the dictionary with prices
cart = set({})


#def addToCart():
#x = list(map(int, input("Enter a multiple value: ").split()))
#print("List of students: ", x)
inp = input(str("Please enter items you want to add to your cart separated by come and one space \n\n"))
items  = list(map(str, inp.split(", ")))
everything = userModule.getEverything()

print("Items", items)
#loop through items
for item in items:
  if item in category:
    cart.add(item);
  else:
    if item in everything:
      print("This item is in other department but we still can add it to your cart ")
      cart.add(item)
    else:
      print("Incorrect item")
    #substract from the inventory
print("Your cart", cart)

#Showing suggestions of merchendize
#Later add put in a cart suggestion capability
userModule.showSuggestions()

#View your cart
def checkOut():
  print("\n Please kindly review your cart: \n")
  pp.pprint(cart)

checkOut()
import random
#Generates permutations of the usernames
from itertools import permutations
def createUserName():
  print("\nPlease create your user name \n")
  firstName = str(input("Please enter yoru user name: "))
  lastName = str(input("\nPlease enter yoru first name: "))
  superHero = str(input("\nWhat is your favourite superhero? "))
  #later add the number to the permutations of the username
  numPermuts = permutations(range(50))

  userName = {firstName, lastName, superHero}

  userNamesPermuts = list(permutations(userName))
  #print("Length pf permutations", len(list(userNamesPermuts)))
  print("These are possible user names for you: \n")

  count = 0
  for i in userNamesPermuts:
    count += 1
    print(count, i)
  #permutsList = list(userNamesPermuts)
  print("Length of permutations", len(userNamesPermuts))
  choice = int(input("Please choose one: \n"))
  userNameWords = userNamesPermuts[choice]
  print(userNameWords)
  userName = ""
  for word in userNameWords:
    userName += word
    userName += str(random.randint(0, 50))
  print(userName)
  #print("UserNameList", userNamesList)
createUserName()


#Call this after user places something in the cart
#print("Your encoded password ")
#print(userModule.encode("abs"));
