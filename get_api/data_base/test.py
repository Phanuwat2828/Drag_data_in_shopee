import json
import requests

url = 'https://shopee.co.th/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11044959&limit=60&offset=180'
data = requests.get(url);
data_all= data.text;
print(data_all);