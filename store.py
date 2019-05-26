# For an online store, this would be a minimum of 6 possible menus that provide functionality such as purchasing and creating reports.



#Purchasing

def welcomeMessage():
  print("Welcome to Iryna's School Supply store!\n");
  print("Let us know what brings you here. Please choose one of the following")

  choice =  int(input("Choolse from one of the following: 1. textbooks, 2.Stationary, 3.Pens and pensils, 4. Laptops, 5. Markers and Highlighters, 6. Computers and printers, 7.paper and printing supplies, 8. Show me everything"))

  return choice

def showTheItems(choice):
  #Dictionaries {item: price}

  textbooks = {}
  stationary = {}
  pensAndPensils = {}
  Laptops = {}
  markersAndHighlighters = {}
  computersAndPrinters = {}
  paperAndPrintingSupps = {}


  switcher = {
    1: "",#show set of textbooks

    2: "", #show set of Stationary

    3: "", #show set of Pends and pensils

    4: "",#show set of Laptops

    5: "",#show set of markers and highlighters

    6: "",#show set of computers and printers

    7: "",#show  set of paper and printing supplies

    8: "",#show a Union of all the sets
  }


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
print("fibonacchi recursive ", fibonacchi)


#login = input("Please enter your user name")
#password = input("Enter you passowd")

#call encrypt password(password)
#fibonacchi = []

def storeInAlphabet():
  print("\nTask 2")
  alphabet = []
  for n in range(97, 123):
    alphabet.append(chr(n))
  print(alphabet)
  return alphabet

def encryptPass():
  #user fibonacchi and Recursion

  #Fill the dictionary with letters and
  #fibonacchi = fibonRecursive(26)
  cipher = {};

    #print(alphabet)
  #Fill in the CYPHER
  alphabet = storeInAlphabet()
  cipher = dict(zip(fibonacchi, alphabet))
  #print (cipher)
  return cipher
print("Cypher ",encryptPass())

#create a list of Fibonacchin numbers


#Creating a list of 26 fibonacchin numbers
#fibonacchi recursive











#-------------CART OPERATIONS--------------
cart = set({})
#Displaying the list of products
#Displaying shopping Cart .
def addToCart(item):
 # myCart = {}
  cart.add(item)
  #return cart

#testing adding to the
myCart = {"cat"}
addToCart("dog")
print(cart)

#retur void just removes
def removeFromCart(item):
  cart.remove(item)
