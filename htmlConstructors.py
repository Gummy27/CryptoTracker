from jsonReader import *
from variables import *

getJson()

def constructOverview():
    wallet = getWallet(getDate())
    overviewData = {}

    # Fjöldi
    overviewData["wallet"] = {}
    for x in wallet:
        overviewData["wallet"][x] = wallet[x]["amount"]

    # Auður
    overviewData["wealth"] = getPrices()  
    for x in overviewData["wealth"]:
        overviewData["wealth"][x] = "$" + str(round(overviewData["wealth"][x], 2))
    
    # Verð
    overviewData["price"] = {}
    for x in wallet:
        overviewData["price"][x] = "$"+str(round(wallet[x]["value"], 2))

    # Hagnaður
    overviewData["profits"] = calculateProfit()
    for x in overviewData["profits"]:
        overviewData["profits"][x] = "$" + str(round(overviewData["profits"][x], 2))

    return overviewData

def constructCrypto(crypto):
    data = getJson()
    baseline = data["crypto_beginning"][crypto]

    compiledData = data["crypto_prices"][getDate()][crypto]

    compiledData["profit"] = compiledData["USD"] - data["crypto_prices"][baseline][crypto]["USD"]
    	
    compiledData["complete"] = data["crypto_prices"]
    return compiledData