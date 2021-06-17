import json
from datetime import date, datetime
from matplotlib import pyplot as plt

# Föll úr öðrum skrám
from cryptoCharts import showCryptoChart
from jsonReader import getJson
today = str(date.today())+"-"+str(datetime.now().hour)

with open("data.json") as file:
    data = json.load(file)

def printOutJsonFile():
    prevTotal = 469.42
    for day in data["crypto_prices"]:
        print(day)
        total = 0.0
        for crypto in data["crypto_prices"][day]:
            print("     ", crypto, data["crypto_prices"][day][crypto])
            total += float(data["crypto_prices"][day][crypto]["USD"])
        print("     ", "Total:", total, "USD")
        print("     ", "Change:", total-prevTotal, "USD")

        prevTotal = total

def printOutProfit():
    for x in data["crypto_beginning"]:
        beginning = data["crypto_beginning"][x]
        print(x, round(data["crypto_prices"][today][x]["USD"] - data["crypto_prices"][beginning][x]["USD"], 2), "USD")

getJson()

with open("data.json") as file:
    data = json.load(file)

while(True):
    print("""Profit - Sýnir hagnað/tapi á öllum rafmyntunum. 
Json - Prentar út upplýsingarnar í json skránni á lesanlegan hátt.
Chart x - Sýnir flowchart með verði einstaka rafmynta í gegnum tíðina. 
Exit - Lokar forritinu.
Update - Uppfærir gagnagrunninn
""")

    userInput = input("Hvað viltu gera? : ").split(" ")
    userInput[0] = userInput[0].lower()
    print()
    if(userInput[0] == "json"):
        printOutJsonFile()
    elif(userInput[0] == "chart"):
        showCryptoChart(userInput[1])
    elif(userInput[0] == "profit"):
        printOutProfit()
    elif(userInput[0] == "update"):
        getJson()
    elif(userInput[0] == "exit"):
        break

    print("-------------------------------------")