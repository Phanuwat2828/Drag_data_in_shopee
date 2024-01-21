import json
import requests

url = 'https://www.lazada.co.th/shop-Groceries-ChocolateSnacksSweets/?ajax=true&isFirstRequest=true&page=1&spm=a2o4m.home-th.3887232320.5.49a87f6dCTCT6a'
data = requests.get(url);
data_all= data.text;
print(data_all);