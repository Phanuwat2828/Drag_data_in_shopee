
import requests;


url = 'https://www.lazada.co.th/shop-moto-lighting/?ajax=true&isFirstRequest=true&page=1&spm=a2o4m.home-th.3887232320.1.11257f6dlhhSgD';

data = requests.get(url)
print(data.text)






