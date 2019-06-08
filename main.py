import userModule
import pprint
import Data

#print(Data.getTextbooks());

cart = set({})

pp = pprint.PrettyPrinter(indent=3)





#print(userModule.getInventory())

#=======EXECUTION-===========
userModule.welcomeMessage()
userModule.convertCurr()
userModule.printSelection()
userModule.store()


