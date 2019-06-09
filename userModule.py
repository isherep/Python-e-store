# For an online store, this would be a minimum of 6 possible menus that provide functionality such as purchasing and creating reports.

import pprint
import Data
choice =0
pp = pprint.PrettyPrinter(indent=3)

laptops = Data.getLaptops()


#print(type(textbooks))

def welcomeMessage():
  #for i in range(20):
  print("\n\n", 20 * "<*>-")
  print( 20*"~~~~")

  print(10*" ", "Welcome to Iryna's School Supply store!");
  print( 20*"~~~~")
  print(20 * "<*>-")
  print("\nWe created this cool Binary Search Tree of a merchandize by price and would like\
        to show you its inorder traversal will sort items by price\n")
  print(20 * "<*>-")
  showBinaryTree()
  print("\n", 20 * "<*>-")
  #print("\nLet us know what brings you here. Please choose one of the following\n")


def convertCurr():
  choice = int(input("\nWould you like to convert your US dollars? \n1. Yes \n2. Not right now \n\n"))
  while(choice >=1 and choice <=2 ):
    if(choice == 1):
      currentInput = int(input("Tell us how many US dollars you would like to conver to bitcoins \n"))
      bitcoins = convertCurrency(currentInput)
      print("\nYou have ", bitcoins, " in your budget.")
      print("\n-------------------------------------\n")
      return bitcoins
      break
    elif choice == 2:
      print("\nNo worries, you will be able to do it during the payment process. Just remmember the prices are in bitcoins")
      break
    else:
      print("\nOnly 1(Yes) and 2(No) are valid choices")
      #choice = input("Would you like to convert your US dollars? \n1. Yes \n2. Not right now \n")



def printSelection():
  print("\nLet us know what brings you here. Please choose one of the following\n")
  print("Choolse from one of the following: \n1. Textbooks \n2. Stationary \n3. Pens and pensils \n4. Laptops \n5. Markers and Highlighters \n6. Devices and printers \n7. Paper and printing supplies \n8. All electronics \n9. All stationary & writing supplies \n10. All departments \n0.Exit \n\n")


#Returns selected catogory's set of merchandise
def makeSelection():
  #choice = printSelection()
  #choice = 0
  choice = int(input("Please select one: "))
  while choice !=0:
  #while True:
    #choice = int(input("Please select one: "))
    switcher = {
      1: Data.getTextbooks(),#show set of textbooks
      2: Data.getStationary(), #show set of Stationary
      3: Data.getPensAndPensils(), #show set of Pends and pensils
      4: Data.getLaptops(),#show set of Laptops
      5: Data.getMarkersAndHighlighters(),#show set of markers and highlighters
      6: Data.getDevicesAndPrinters(),#show set of computers and printers
      7: Data.getPaperAndPrintingSupps(),#show  set of paper and printing supplies
      8: Data.getElectronics(),#show a Union of computers and laptops
      9: Data.getAllStationary(),#union of Stationary and pens and pencils
      10: Data.getEverything(),
      0: set({})
    }
    #
    return switcher.get(choice)



#import sys
#sys.setrecursionlimit(1500)
def convertCurrency(decimal):
  # Function to print binary number for the input decimal using recursion
  if decimal==0:
    return ''
  else:
    return convertCurrency(decimal//2) + str(decimal%2)


#--------LOGGING IN, ENCRYPTION AND CYPHER---
#What I am doing is that initially I am assigning -1 to all the indexes in the list telling that this particular state has never been visited. Once, I visit a particular state, I store its solution in the arr at that index. And if the solution state has been visited and is encountered again, I straight away return the solution possible at that index without recursing further on it.

n=26
fibonacchi = []

def fibonRecursive(n):

  if fibonacchi[n] != -1:
    return fibonacchi[n]
  if n == 0:
    fibonacchi[0] = 0
    return 0 #base case 1
  elif n == 1:
    fibonacchi[1] = 1;
    return 1  #base case 2
  else:
    fibonacchi[n] = fibonRecursive(n-1) + fibonRecursive(n-2);
    return fibonacchi[n];



for i in range(n+1):
  fibonacchi.append(-1);
fibonRecursive(n)
#print("fibonacchi recursive ", fibonacchi)

#login = input("Please enter your user name: ")#password = input("Enter you passowd: ")


#call encrypt password(password)
#fibonacchi = []


def checkOutCart():
  print("\n Please kindly review your cart: \n\n")

  pp.pprint(cart)
  print("\n==========================================\n")

def storeInAlphabet():

  alphabet = []
  for n in range(97, 123):
    alphabet.append(chr(n))
  #print(alphabet)
  return alphabet

def createCipher():

  cipher = {};

  alphabet = storeInAlphabet()
  #print("Alphabet ", alphabet)
  cipher = dict(zip(alphabet, fibonacchi))
  #print (cipher)
  return cipher
#print("Cypher ",encryptPass())

import pandas as pd
cipher = createCipher()

df = pd.DataFrame.from_dict(cipher, orient='index', columns=['Letter'])

#print(df)

#encodes the password
import numpy as np
def encode(password):

  encodedWord = ""
  cipher = createCipher()
  digitArray = []
  for i in password:
    if i in cipher.keys():
      digitArray.append(cipher.get(i))
  print("The encoded numbers are: ")
  #testing the coded characters
  print(digitArray)
  codeArr= np.array(digitArray)
  product = np.sum(codeArr)
  return product
  #return digitArray


#-------------CART OPERATIONS--------------
cart = set({})
#Displaying the list of products
#Displaying shopping Cart .
def addToCart(item):
 # myCart = {}
  cart.add(item)
  #return cart


#create combinations of similar items from other department
from itertools import combinations
import random
#Returns a list of suggested products
def showSuggestions():
  #create combinations of everythig set
  result = combinations(Data.getEverything(), 5)
  #randomly print one combination to the user
  print("\n====================================\n")
  print("\n ~~~~~~~People also bought: ~~~~~~~~\n ")
  #print("Number of combinations", len(list(result)))
  #change hardcoded ma to the length of combinations
  randomSuggestion = random.randint(1,1533939-1)
  #print(list(result)[randomSuggestion])
  #for l in list(result):
	 # print(l)

  return list(result)[randomSuggestion]

def processCard():
    #calculate total of items in the cart
    #find the prices for the keys in themap
    total = 0
    for i in cart:
        #find a value from a key in that dicitonary using Everything dictionary 
        price = Data.getEverything().get(i)
        total +=price
        #print(price, total)
       
    print("\n\n",50 * "=")
    print("\nYour total is: ", total, " bitcoins")
    
    print("\n\n",50 * "=")
    cartInfo = str(input("\nPlease provide card number, expiration date, and zipcode separated by comas, NO SPACES\n"))
    cartInfoNums = cartInfo.split(',')
    
    cartNum = cartInfoNums[0]
    expDate = cartInfoNums[1]
    zipCode = cartInfoNums[2]
    
    if len(cartNum) == 16 and len(expDate) == 5 and len(zipCode) == 5:
        print("\nYour order has been processes. \n")
        print(15 * "<*>-")
        print("\nThank you for your purchase! \n")
        print(15 * "<*>-")
        print(70*"=")
    else:
        print("Please enter card information again")
        
    
    

def offerLottery():
  print("\n==========================================\n")
  print("**********Congratulations! *************\nToday you get a chance to win one free item from our online store.\
        \n\nWould you like to see what the each item probability of winning is before your play the lottery? \
        \nPlease enter 1 or 2\n")
  choice = int(input("\n1. Yes\n2. No \n\n"))
  
  #while(choice == None):
  if choice == 1:
  #show calculated probabilities
    #print("The probability of winning each item is: \n")
    calcProbabils()
    
    #choose the item randomly
    inventoryLottery = list(Data.getInventoryLottery())
    totalQuantity = len(inventoryLottery)
    ranItem = random.randint(1,totalQuantity)
    itemWon = inventoryLottery[ranItem]
    print("\n", 40 * "=", "\n")
    print("*** You have won the item: ", itemWon, "***")
    #processCard()
  if choice == 2:
    print("It's OK, You did not miss much =)")
    checkOutCart()
    #processCard()
           
  else:
    print("\nValid selections are 1  and 2. Please enter one of them")
  #userModule.checkOutCart()

import random
#Generates permutations of the usernames
from itertools import permutations


def createUserName():
  print("\n\n~~~~~ We will create a user name for you ~~~~~\n")
  firstName = str(input("Please enter yoru user name: "))
  lastName = str(input("\nPlease enter yoru first name: "))
  superHero = str(input("\nWhat is your favourite superhero? "))
  #later add the number to the permutations of the username
  numPermuts = permutations(range(50))

  userName = {firstName, lastName, superHero}

  userNamesPermuts = list(permutations(userName))
  #print("Length pf permutations", len(list(userNamesPermuts)))
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("These are possible user names permutations  for you: \n")
  print("Please choose one: \n")
  
  #need a loop here to ony accept integers
  count = 0
  for i in userNamesPermuts:
    count += 1
    print(count, i)
  #permutsList = list(userNamesPermuts)
  #print("Length of permutations", len(userNamesPermuts))
  choice = -1#invalid choice case, initializing

  while choice < 1 or choice >6:
      choice = input("\nYour choice: \n")
      #precondition in case user entered string not number
      try:
      #while type(choice) !=int:
          choice = int(choice)
          userNameWords = userNamesPermuts[choice - 1]
          userName = ""
          for word in userNameWords:
              userName += word
              userName += str(random.randint(0, 50))
          
          print("\nYour user name will be :  ")
          print(40 * "*")
          print("*", 7*" ", userName, 7*" ", "*")
          print(40 * "*")
      #if non-int in range entered - keep looping until correct number is entered    
      except ValueError:
          choice = -1
          print("\nPlease enter numbers only\n")
          continue
  

def calcProbabils():
#calculate each probabilty in current inventory
  inventoryLottery = Data.getInventoryLottery()
  totalQuantity = sum(inventoryLottery.values())
  #print(totalQuantity) - test
  print("\n******* Probabilities to win each item on sale are *********\n")
  print(70 * "-")
  for i in inventoryLottery:
    prob = str(round(inventoryLottery.get(i)/totalQuantity, 2)* 100) + "%"

    print(i, " -- ", prob)
    #pp.pprint(i)
    #pp.pprint(prob)

#retur void just removes
def removeFromCart(item):
  cart.remove(item)


#shows a list of items in a chose category and adds the selected item to the cart
def addToCart(category):
  inp = input(str("Please enter items you want to add to your cart separated by come and one space \n\n"))
  ##category = set(makeSelection())
  #print("Category is ", category)
  
  
  #Set intersection 
  if category == set(Data.getLaptops()):
      print("\nThese are the other electronic items that are \
            not in the Laptops category\n")
      pp.pprint(Data.getOtherElectronics())
      
  items  = list(map(str, inp.split(", ")))
  everything = Data.getEverything()

  #print("Items", items)
  #loop through items
  total = 0
  for item in items:
    if item in category:
      cart.add(item);
      total += everything.get(item)
    else:
      if item in everything:
        print("This item is in other department but we still can add it to your cart ")
        cart.add(item)
        total += everything.get(item)
      else:
        print("Incorrect item")
      #substract from the inventory
  print("\n~~~~~~~~~~ Your cart: ~~~~~~~~~~~~\n\n", cart)
  print("\nYour total is: ", total, " bitcoins")
  print(40*"~")

#category = set(makeSelection())




def showBinaryTree():
    tree = Data.getBinaryTree()
    Data.inorder(tree)
#checkOutCart()
def createPassword():
  password = str(input("Please enter your password and we will encode it: "))
  #encode(password)
  print("\nYour encoded password is: ", encode(password))

def checkOut():
  isReady = int(input("Are you ready to to proceed further? Please enter 1 or 2:   \n1. Yes \n2. No\n\n"))

  if isReady == 1:
    createUserName()
    createPassword()
  else:
    #welcomeMessage()
    #show the merchendise again
    print("\nYou are welcome to shot some more. Here is all the categories: \n")
    printSelection()
    
    category = makeSelection()
    #shw merchandize in selection
    showItemsInCateg(category)
    addToCart(category)
    
    createUserName()
    createPassword()

#-------------------------
def showItemsInCateg(category):
  #category = set(userModule.makeSelection())
  #category = makeSelection()
  print("\nHere is what store has to offer you in the section you chose: \n")
  pp.pprint(category)
#-------------------------

    

def store():
  category = makeSelection()
  if makeSelection() is not None:
    showItemsInCateg(category)
    addToCart(category)
    #checkOutCart()
    pp.pprint(showSuggestions())
    #ask if the customer likes any of suggestion and wold like to add them
    # to a cart or withlist
    #print("Would you like to any of these to the cart?\n 1.Yes \n2.No\n")
    everything = Data.getEverything()
    result = int(input("Would you like to add any of these to the cart?\n1.Yes \n2.No\n\n"))
    if(result == 1):
        selected= str(input("Please print which item you would like to add to the cart: \n\n"))
        items  = list(map(str, selected.split(", ")))
        for item in items:
            if item in everything:
                cart.add(item);
            print("\n\nItems have beed added to your cart\n", 30 * "===========", "\n" )
            print("*******YOUR CART: ********\n")
            pp.pprint(cart)
            
    if(result == 2):
        print(40*"=")
        print("\nItems have beed added to your cart\n", 30 * "=" )
        print("Thank you, lets move to the next step\n") 
        print("***Your cart: ***\n")
        pp.pprint(cart)
            
    
    checkOut()
    offerLottery()
    print("\n==========================================\n")
    processCard()

  else:
    print(20 * "<*>-")  
    print("~~~~~~~~~~~~ Goodbye! ~~~~~~~~~~~~~~~\n")
    print("~~~ If you want to come back, please press Run button ~~~\n")
    print(80 * "=")
