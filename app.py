from flask import Flask, render_template, url_for

# Föll úr öðrum skrám
from cryptoCharts import showCryptoChart
from jsonReader import getJson, getPrices, getWallet, calculateProfit

app = Flask(__name__)

data = getJson()

@app.route("/")
def home():  
    print("This is the test", getWallet())  
    return render_template("wallet.html", wallet=getWallet(), prices=getPrices(), profits=calculateProfit())

@app.route("/json")
def testJson():
    return data