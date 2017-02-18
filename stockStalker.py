'''
stockStalker.py
This module is the entry point of stock stalker app. It reads all the 
necessary files provided in  command line arguments. Creates all data
structures. Invokes stalker module which does all the number crunching
and data retrieval and trigger evaluation work.

This module also has the ability to invoke the stalker module periodically.
It also periodically reads to files again to see if they have changed.
'''

import sys
from collections import defaultdict
import utility_functions as UF

ARGS_COUNT      = 7
d_portfolioFile   = ''
d_watchlistFile   = ''
d_contactFile     = ''

#storing stock values/actions
#Its a dictionary of dictionaries.. 
#Contains a dictionary tracking all the buy/sell actions
#and a value element tracking its total cost basis value
d_stockValueAction = {}

def usage():
    '''
    Prints Usage
    '''
    print('Usage: stockStalker.py -p <portfolio> -w <watchlist> -c <contact info>')

def parseInput():
    '''
    Goes through all the command line arguments. Validates them and
    collects all the filenames from them.
    '''
    print(sys.argv)

    global d_portfolioFile
    global d_watchlistFile
    global d_contactFile
    
    portfolioFound  = False
    watchlistFound  = False
    contactFound    = False

    if len(sys.argv) != ARGS_COUNT:
        return False

    count = 0
    for arg in sys.argv:
        if arg == '-p':
            d_portfolioFile = sys.argv[count + 1]
            portfolioFound = True
        elif arg == '-w':
            d_watchlistFile = sys.argv[count + 1]
            watchlistFound = True
        elif arg == '-c':
            d_contactFile = sys.argv[count + 1]
            contactFound = True
        count += 1

    ''' TODO: Check if files actully exist here '''

    if portfolioFound == False or watchlistFound == False or contactFound == False:
        return False

    return True


def preparePortfolio():
    '''
    Reads portfolio file line by line and saves all the info
    '''
    global d_portfolioFile
    fileContents = None
    with open(d_portfolioFile) as f:
        fileContents = f.readlines()
    
    fileContents = [x.strip() for x in fileContents]
    
    currentStock = None
	for line in fileContents:
        (isStockLine, value) = UF.isNewStockLine()
        (isActionLine, action, stockCount, stockPrice) = UF.isStockActionLine(line)
        (isTriggerLine, condition, value) = UF.isStockTriggerLine(line)
        if True == isStockLine:
            currentStock = value
            d_stockValueAction[currentStock] = {'totalCost': 0, 'actions': []}
        elif True == isActionLine:
            if currentStock == None:
                #TODO: put a try except around it and log errors.
                raise
            
            d_stockValueAction[currentStock]['actions'].append({'action': action, 'shares': stockCount, 'price': stockPrice})
            if(action == "BUY"):
                d_stockValueAction[currentStock]['totalCost'] += stockCount*stockPrice
            elif action == "SELL":
                d_stockValueAction[currentStock]['totalCost'] -= stockCount*stockPrice
            else:
                #TODO: try-except and log errors
                raise
        elif True == isTriggerLine:
            #TODO: Handle triggers

    

def prepareWatchList():
    '''
    Reads warchlist file and saves all the info
    '''


def saveContactInfo():
    '''
    Reads contact info from the contact file
    '''


def parseInputFiles():
    '''
    Makes three function calls to parse and collect 
    information from all three files. It also builds all
    the data structures to be used by the stalker module
    '''
    preparePortfolio()
    prepareWatchList()
    saveContactInfo()
    

def setupDataStructures():
   if False == parseInput():
       usage()
       return

   print('Moving forward with file parsing')
   parseInputFiles()


if __name__ == '__main__':
    setupDataStructures()
