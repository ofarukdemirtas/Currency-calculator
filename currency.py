import requests
url="https://finans.truncgil.com/today.json"
resp=requests.get(url)
read=resp.json()
date=read["Update_Date"]
dolarSatis=read["USD"]["Satış"]
message="Hello, Current dollar as of {} \nDollar:{} TL\nHave a good day".format(date, dolarSatis)
print(message)

