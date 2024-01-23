import json
import requests

url = 'https://www.lazada.co.th/?spm=a2o4m.home-th.header.dhome.5cbf7f6duhFe9C'
data = requests.get(url);
data_all= data.text;
print(data_all);