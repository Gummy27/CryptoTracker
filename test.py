import json

with open("data.json", 'r') as file:
    data = json.load(file)

for dates in data["crypto_prices"]:
    for crypto in data["crypto_prices"][dates]:
        try:
            data["crypto_prices"][dates][crypto]["value"] = data["crypto_prices"][dates][crypto]["USD"] / data["crypto_prices"][dates][crypto]["amount"]
        except:
            data["crypto_prices"][dates][crypto]["value"] =  data["crypto_prices"][dates][crypto]["USD"]
        
with open("data.json", 'w') as file:
    file.write(json.dumps(data))