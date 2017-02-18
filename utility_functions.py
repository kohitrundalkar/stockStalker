'''
Some functions used by stockStalker 
modules
'''

import string

#Parse text to see if this is the stock name
#line in the portfolio file
def isNewStockLine(portfolioLine):
    if portfolioLine and portfolioLine != '':
        tokens = portfolioLine.split()
        if(tokens[0].find("STOCK") != -1):
            return (True, tokens[1].strip())
        else:
            return (False, 'Not a stock line.')
    
    return (False, 'Empty/Null line.')


#Parse the portfolio action line to extract the
#buy/sell action and the stock value
def isStockActionLine(actionLine):
    if actionLine and actionLine != '':
        tokens = actionLine.split()
        if(tokens[0].find("BUY") != -1):
            return (True, "BUY", float(tokens[1]), float(tokens[3]))
        elif (tokens[0].find("SELL") != -1):
            return (True, "SELL", float(tokens[1]), float(tokens[3]))
        else:
            return (False, "", 0.0, 0.0)
    
    return (False, "", 0.0, 0.0)


#Parse the porfolio trigger lines
def isStockTriggerLine(triggerLine):
    if triggerLine and triggerLine != '':
        tokens = triggerLine.split()
        if(tokens[0].find("TRIGGER") != -1):
            return (True, tokens[1], float(tokens[2]))
    
    return (False, '', 0.0)
           
        



