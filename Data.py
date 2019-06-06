textbooks = {"Introduction to Programming", "MySQL", "Web Development","Programming in C/C++", "Web Design", "Project Management", "Writing programs in Java", "JavaScript and jQuery", "Discrete Mathematics", "Brain Friendly Android Developement", "Cloud Computing", "English 101", "Agile processes", "Database Systems" }

stationary = {"Envelopes", "Staples", "Scissors", "Staple Removers", "Hole punchers", "Supply container", "Pencil cup"}

pensAndPensils = {"Ball pen blue", "Gell pen blue", "Ball pen black", "Ball pen black", "Red ball pen", "Red gell pen"}

laptops = {"Dell-123", "Compaq-234", "Dell-124", "Dell-125", "HP-888", "HP - 777", "Acer-123", "Mac 8GB", "Mac 16GB"}

markersAndHighlighters = {"Expo Dry Erase markers", "Low Odor Markers", "BIC 6pk highlighters", "Sharpie 3pk Highlighers"}

devicesAndPrinters = {"Brother Wireless Printer-9", "HP OfficeJet", "Brother Wireless Printer-11", "HP OfficeJet Wireless"}

paperAndPrintingSupps = {"Copy Paper", "Laser Printer Paper", "InkJet Paper", "Color Paper"}


inventory = {
  "Introduction to Programming": 20,
  "MySQL": 13,
  "Web Development" : 21,
  "Programming in C/C++": 23,
  "Web Design": 3,
  "Project Management": 33,
  "Writing programs in Java": 6

}

electronics = laptops | devicesAndPrinters
allStationary = stationary | pensAndPensils|markersAndHighlighters
#set of all items in the store
everything = set.union(textbooks, stationary, pensAndPensils, laptops, markersAndHighlighters, devicesAndPrinters, paperAndPrintingSupps)


def getTextbooks():
  return textbooks

def getStationary():
  return stationary

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

def getEverything():
  return everything


def getInventory():
  return inventory
#------------------------
