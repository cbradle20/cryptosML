import urllib.request
import requests
import pandas as pd
import json

"""
extracting all the data points in the dictionary for 1 day timeframe
"""
url1d = "https://api.nomics.com/v1/currencies/ticker?key=f7a0286fa28cadcf41c2dece7ec73010&ids=AAVE,ALGOO,BAND,BTC,COMP,CRV,ETH,LINK,MKR,OMG,REN,SNX,UMA,UNI,YFI&interval=1d"
data = requests.get(url1d)
data = data.json()
data = json.dumps(data)
data = json.loads(data)

"""
Not even going to explain this loop lol 
"""
for i in data: 
    oned = i.pop("1d")
    i.update(oned)
df = pd.DataFrame(data)
df["price_change_pct"] = pd.to_numeric(df["price_change_pct"])
df["price_change_pct"] =  df["price_change_pct"].multiply(100)

df2 = df[["id", "price_change_pct"]]
df2 = df2.sort_values("id", ascending = True)
print(df2)

df.to_csv("cryptos.csv")

"""
Machine Learning starts here
"""

#df["Price Change precentage"] = df["Price Change percentage"].astype(float)
#df["Volume Change Percent"] = df["Volume Change Percent"].astype(float)
#print(df)
#print(data.json())