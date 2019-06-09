textbooks = {
        "Introduction to Programming": 55.95, 
        "MySQL": 67.00, 
        "Web Development": 98.99 ,
        "Programming in C/C++": 120.00, 
        "Web Design": 88.00, 
        "Project Management":45.00, 
        "Writing programs in Java": 130.00, 
        "JavaScript and jQuery": 19.00, 
        "Discrete Mathematics": 75.00, 
        "Brain Friendly Android Developement": 48.55, 
        "Cloud Computing": 145.00, 
        "English 101": 34.00, 
        "Agile processes": 87.00, 
        "Database Systems" : 45.00
        }

stationary = {"Envelopes": 9.00, 
              "Staples": 25.00, 
              "Scissors": 7.00, 
              "Staple Removers": 2.00, 
              "Hole punchers": 25.00,
              "Supply container": 3.00,
              "Pencil cup": 5.00
              }

pensAndPensils = {"Ball pen blue": 3.00, 
                  "Gell pen blue": 7.00, 
                  "Ball pen black": 3.00,
                  "Ball pen black": 3.00, 
                  "Red ball pen": 3.00, 
                  "Red gell pen": 7.00
                  }

laptops = {"Dell-123": 549.00, 
           "Compaq-234": 199.00, 
           "Dell-124": 349.00, 
           "Dell-125": 375.00, 
           "HP-888": 700.00, 
           "HP - 777": 600.00, 
           "Acer-123": 450.00, 
           "Mac 8GB": 1200.00, 
           "Mac 16GB": 2999.00
           }

markersAndHighlighters = {"Expo Dry Erase markers": 3.99, 
                          "Low Odor Markers" :4.99, 
                          "BIC 6pk highlighters": 2.99, 
                          "Sharpie 3pk Highlighers": 2.49
                          }

devicesAndPrinters = {"Brother Wireless Printer-9": 99.00, 
                      "HP OfficeJet": 70.00, 
                      "Brother Wireless Printer-11": 130.00, 
                      "HP OfficeJet Wireless": 100.00}

paperAndPrintingSupps = {"Copy Paper": 3.99, 
                         "Laser Printer Paper": 5.99 , 
                         "InkJet Paper": 4.99, 
                         "Color Paper": 9.99
                         }


inventoryLottery = {
  "Introduction to Programming": 20,
  "MySQL": 13,
  "Web Development" : 21,
  "Programming in C/C++": 23,
  "Web Design": 3,
  "Project Management": 33,
  "Writing programs in Java": 6

}



electronics = laptops.keys() | devicesAndPrinters.keys()
allStationary = stationary.keys() | pensAndPensils.keys()|markersAndHighlighters.keys()

#find our intersection of Laptops and All electronics
# Set difference: take a and remove elements in b
#diff = a - b
#print(diff)


#Set intersection 
otherElectronics = electronics - laptops.keys()

print("\nOther electronics besides laptops are ",otherElectronics)


##union of dicionaries
allStationary2 = {**stationary,**pensAndPensils, **markersAndHighlighters} 
#print("Merged dicionaries", allStationary2)
#set of all items in the store
#The method keys() returns a list of all the available keys in the dictionary.
#everything = set.union(set(textbooks.keys()), set(stationary.keys()), set(pensAndPensils.keys()), set(laptops.keys()), set(markersAndHighlighters.keys()), set(devicesAndPrinters.keys()),set( paperAndPrintingSupps.keys()))

everything = {**textbooks, **stationary, **pensAndPensils, **laptops, **markersAndHighlighters, **devicesAndPrinters, **paperAndPrintingSupps}
#-------------BINARY TREE OF MERCHANDISE-------------------

#Creating binary tree
#The tree with sort by price. If two products have the same price, the node will be
#replaced. Key - item name, value, get(item) - price.
class Node():
    #Constructor
    #Keyprice - price of the item in the store
	def __init__(self, keyPrice, itemName):
		# object attribute key assigned parameter key
		self.keyPrice = keyPrice
		# serves as pointers to the children nodes
		self.left = None
		self.right = None
		self.itemName = itemName
        
def insert(root, node):
	# root is placeholder we use to recurse through nodes
	# node is the key of the node we are inserting
	
	# If the tree is empty, set root to passed in node
	if root is None:
		root = node 
	
	else:
		if root.keyPrice < node.keyPrice:
			if root.right is None:
				root.right = node 
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)
                
# inorder tree traversal
def inorder(root):
	if root:
		inorder(root.left)
		print(root.keyPrice, "  ", root.itemName)
		inorder(root.right) 
        
#post order 
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)   
        print(root.keyPrice, "  ", root.itemName)
        

def getEverything():
  return everything
# Lets create our BST to the right
array = getEverything()
#print(array.get("Web Development"))

root1 = Node(array.get("Web Development"), "Web Development")  # root


for i in array:
    insert(root1, Node(array.get(i),  i ))
    #print(array.get(i), i )
    
#These traversal printings work    
#inorder(root1)   
#postorder(root1)

'''
def printBinaryTree():
    inorder(root1)
'''
def getBinaryTree():
    return root1
#print("Binary tree is ", getBinaryTree())
tree = getBinaryTree()
#prints None currently

#print("InOrder Traversal of Get Binary Tree ")
#postorder(tree)

#printBinaryTree()



def getTextbooks():
  #return textbooks.keys()
  #return list(textbooks)
  return textbooks;

#print("Textbook dictionary ", getTextbooks())

def getStationary():
  return stationary
#print("All stationary ", getStationary())

def getPensAndPensils():
  return pensAndPensils

def getLaptops():
  return laptops

def getMarkersAndHighlighters():
  return markersAndHighlighters

def getDevicesAndPrinters():
  return devicesAndPrinters

def getPaperAndPrintingSupps():
  return paperAndPrintingSupps


#------------
def getElectronics():
  return electronics

def getAllStationary():
  return allStationary



def getInventoryLottery():
  return inventoryLottery
#Return Set intersection 
def getOtherElectronics():
    return otherElectronics
#------------------------
  
