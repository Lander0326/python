# 只載入一個月的股價資料

import requests as r
import pandas as pd

url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220101&stockNo=00635U"

#print(r.get(url)) # <Response [200]>
res = r.get(url)
#print(res.json())
stock_json = res.json()
#print(type(stock_json)) # <class 'dict'>
#print(stock_json['data'])
df = pd.DataFrame(stock_json['data'],columns=stock_json['fields'])
print(df.head())
