#This example uses Python 2.7 and the python-request library.
import requests
import json
from datetime import date, datetime

today = str(date.today())+"-"+str(datetime.now().hour)

def getDataFromAPI():
    API_KEY = "9cea12e5-6cd3-4443-8bf8-64755ab98eff"
    URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    headers = {
        "X-CMC_PRO_API_KEY" : API_KEY,
        'Accepts' : "application/json"
    }

    params = {
        'start' : '1',
        'limit' : '100',
        'convert' : "USD"
    }
    return json.loads(requests.get(url=URL, params=params, headers=headers).text)["data"]

def updateJsonFile():
    data = getDataFromAPI()

    with open("data.json", 'r') as file:
        wallet = json.load(file)

    wallet["crypto_prices"][today] = {}
    for x in wallet["crypto_wallet"]:
        for i in data:
            if(i["symbol"] == x):
                wallet["crypto_prices"][today][x] = {
                    "USD":float(wallet["crypto_wallet"][x]) * float(i["quote"]["USD"]["price"]), 
                    "amount":float(wallet["crypto_wallet"][x]),
                    "value": float(i["quote"]["USD"]["price"])
                }
                break
    
    wallet["last_update"] = today

    with open("data.json", 'w') as file:
        file.write(json.dumps(wallet))

def getJson():
    with open("data.json") as file:
        data = json.load(file)

    if data["last_update"] != today:
        updateJsonFile()
        print("The file was updated successfully!")
    else:
        print("The file is already up to date!")

    return data

def getWallet():
    with open("data.json", 'r') as file:
        data = json.load(file)

    return dict(data["crypto_wallet"])

def getPrices():
    with open("data.json", 'r') as file:
        data = json.load(file)

    temp = {}
    for x in data["crypto_prices"][data["last_update"]]:
        temp[x] = data["crypto_prices"][data["last_update"]][x]["USD"]

    return temp

def calculateProfit():
    with open("data.json", 'r') as file:
        data = dict(json.load(file))

    temp = {}
    for x in data["crypto_wallet"]:
        temp[x] = data["crypto_prices"][data["last_update"]][x]["USD"] - data["crypto_prices"][data["crypto_beginning"][x]][x]["USD"]

    return temp

