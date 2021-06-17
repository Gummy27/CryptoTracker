from matplotlib import pyplot as plt
from datetime import datetime, date
import json

today = str(date.today())+"-"+str(datetime.now().hour)

with open("data.json") as file:
    data = json.load(file)

def showCryptoChart(crypto):
    beginning = data["crypto_beginning"][crypto]

    updatedDays = []
    isPastBeginning = False
    for x in data["crypto_prices"]:
        if(x == beginning):
            isPastBeginning = True
        if(isPastBeginning):
            updatedDays.append(x)

    print()
    listOfDates = []
    listOfValue = []
    tempDate = beginning
    while(tempDate != iterateDate(today)):
        if(tempDate == updatedDays[0]):
            updatedDays.pop(0)
            tempValue = data["crypto_prices"][tempDate][crypto][0]
        tempDate = iterateDate(tempDate)
        listOfDates.append(tempDate)
        listOfValue.append(tempValue)

    plt.plot(listOfDates, listOfValue)
    plt.show()

def iterateDate(date):
    year, month, day, hour = map(int, date.split("-"))

    leapYear = lambda x : (x % 4 == 0) and (x % 100 != 0 and x % 100 != 0)

    daysInMonth = [31, 28 + leapYear(year), 31, 30, 31, 31, 31, 31, 30, 31, 30, 31]

    if(hour == 24):
        hour = 1
        if(day == daysInMonth[month]):
            day = 1
            if(month == 12):
                month = 1
                year += 1
            else:
                month += 1
        else:
            day += 1
    else:
        hour += 1

    month = ("0" * (2-len(str(month)))) + str(month)
    return(f"{year}-{month}-{day}-{hour}")