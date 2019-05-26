# For an online store, this would be a minimum of 6 possible menus that provide functionality such as purchasing and creating reports.

textbooks = {"Introduction to Programming", "MySQL", "Web Development"}
stationary = {"Envelopes", "Staples", "Scissors", "Staple Removers"}
pensAndPensils = {"Ball pen blue", "Gell pen blue", "Ball pen black", "Ball pen black"}

Laptops = {"Dell-123", "Compaq-234", "Dell-124", "Dell-125", "HP-888", "HP - 777"}

markersAndHighlighters = {"Expo Dry Erase markers", "Low Odor Markers", "BIC 6pk highlighters", "Sharpie 3pk Highlighers"}
devicesAndPrinters = {"Brother Wireless Printer", "HP OfficeJet", }
paperAndPrintingSupps = {"Copy Paper", "Laser Printer Paper", "InkJet Paper"}

electronics = Laptops | devicesAndPrinters
allStationary = stationary | pensAndPensils|markersAndHighlighters
#set of all items in the store
everything = set.union(textbooks, stationary, pensAndPensils, Laptops, markersAndHighlighters, devicesAndPrinters, paperAndPrintingSupps)

import pprint
def welcomeMessage():
  print("\nWelcome to Iryna's School Supply store!\n");
  print("Let us know what brings you here. Please choose one of the following\n")

  choice =  int(input("Choolse from one of the following: \n1. Textbooks \n2. Stationary \n3. Pens and pensils \n4. Laptops \n5. Markers and Highlighters \n6. Devices and printers \n7. Paper and printing supplies \n8. Show all electronics \n9. Show all stationary & writing supplies \n10. Show me everything\n\n"))
  from itertools import chain

  switcher = {
    1: textbooks,#show set of textbooks

    2: stationary, #show set of Stationary

    3: pensAndPensils, #show set of Pends and pensils

    4: Laptops,#show set of Laptops

    5: markersAndHighlighters,#show set of markers and highlighters

    6: devicesAndPrinters,#show set of computers and printers

    7: paperAndPrintingSupps,#show  set of paper and printing supplies

    8: electronics,#show a Union of computers and laptops

    9: allStationary,#union of Stationary and pens and pencils
    10: everything
  }
  pp = pprint.PrettyPrinter(indent=2)
  print("Your choose",pp.pprint(switcher.get(choice)))

#import sys
#sys.setrecursionlimit(1500)
def convertCurrency(decimal):
  # Function to print binary number for the input decimal using recursion
  if decimal==0:
    return ''
  else:
    return convertCurrency(decimal//2) + str(decimal%2)
  #if decimal > 1:
   #   convertCurrency(decimal//2)
  #return(decimal % 2)


# decimal number
#dec = 34
#convertCurrency(dec)
#print("The decimal number is ", decim)

currentInput = int(input("Tell us how many US dollars you would like to conver to bitcoins \n"))
bitcoins = convertCurrency(currentInput)
#This programs assumes you can divide binary bitcoins just like a regular money
print("You have ", bitcoins, " bitcoins to spent")



  #return choice


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
  product = np.prod(digitArray)
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

#testing adding to the
myCart = {"cat"}
addToCart("dog")
#print(cart)

#retur void just removes
def removeFromCart(item):
  cart.remove(item)
