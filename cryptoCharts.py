from matplotlib import pyplot as plt
from datetime import datetime, date
from jsonReader import calculateProfit, getJson
import json

today = str(date.today())+"-"+str(datetime.now().hour)

data = getJson()

def iterateDate(date):
    date = datetime.strptime(date, "%Y-%m-%d-%H")
    return datetime.timestamp(date) + 3600

def calculateDifDate(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d-%H")
    d2 = datetime.strptime(d2, "%Y-%m-%d-%H")

    return ((datetime.timestamp(d1) - datetime.timestamp(d2))/60/60)

def plotCrypto(crypto, beginning=False):
    if(not beginning):
        beginning = data["crypto_beginning"][crypto]

    updatedDays = list(data["crypto_prices"].keys())
    updatedDays = updatedDays[updatedDays.index(beginning):]

    listOfDates = []
    tempDate = beginning
    while(tempDate != iterateDate(today)):
        listOfDates.append(tempDate)
        tempDate = iterateDate(tempDate)

    listOfValues = ['']*len(listOfDates)

    for x in updatedDays:
        listOfValues[listOfDates.index(x)] = data["crypto_prices"][x][crypto]["USD"]

    temp = 0
    for x in range(len(listOfValues)):
        if (listOfValues[x]):
            temp = listOfValues[x]
        else:
            listOfValues[x] = temp

    return(listOfDates, listOfValues)

def plotCryptoPercentage(crypto):
    beginning = data["crypto_beginning"][crypto]

    baseline = data["crypto_prices"][beginning][crypto]["USD"]

    updatedDays = list(data["crypto_prices"].keys())
    updatedDays = updatedDays[updatedDays.index(beginning):]

    print(baseline)

def constructChart(cryptos, date=False):
    fig, ax = plt.subplots()
    for x in cryptos:
        x_axis, y_axis = plotCrypto(x, date)
        ax.plot(x_axis, y_axis)

    ax.set_xticklabels([])

    plt.tick_params(bottom=False)
    plt.show()
        


# constructChart(["DOT", "COMP", "BTC", "ETH"], "2021-06-12-11")
plotCryptoPercentage("DOT")
calculateDifDate("2021-06-13-11", "2021-06-12-22")