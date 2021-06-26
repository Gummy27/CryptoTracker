from flask import Flask, render_template, url_for

# Föll úr öðrum skrám
from variables import *
from htmlConstructors import *

app = Flask(__name__)

getJson()

@app.route("/")
def home():  
    return render_template("wallet.html", 
        overviewData=constructOverview(), 
        cryptoList=[x for x in getWallet(getDate())],
        sum = calculateSum(getDate()),
        sumBaseline = calculateSumBaseline()
    )

@app.route("/<crypto>")
def cryptoView(crypto):
    return render_template("crypto.html",
        crypto=crypto,
        data=constructCrypto(crypto.upper())
    )

@app.route("/json")
def testJson():
    return getJson()