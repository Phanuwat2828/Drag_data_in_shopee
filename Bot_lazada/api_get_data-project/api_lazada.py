import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



def process():
    for i in range(0,40):
        data_item = data["mods"]["listItems"][i];
        name = data_item['name']
        image = data_item['image']
        price = float(data_item['priceShow'].replace("฿","").replace(",",""));
        location = data_item['location']
        if "discount" in data_item:
            discount = data_item['discount'].replace("% ","").replace("Off","");
        else :
            discount = 0;

        if "review" in data_item:
            review = data_item['review'];
            if review == '':
                review = 0;
        else :
            review = 0;

        if "itemUrl" in data_item:
            itemurl = data_item['itemUrl'];
        else :
            itemurl = data_item[ "thumbs"][0]['itemUrl'];

        if "itemSoldCntShow" in data_item:
            sold = float(data_item["itemSoldCntShow"].replace(" sold","").replace(" ชิ้น","").replace("K",""));
        else :
            sold = 0.0;
        print("==============",(i+1),"=================");
        print(name);
        print(image);
        print(price);
        print(location);
        print(review);
        print(discount);
        print(itemurl);
        print(sold);


# Define retry strategy
retry_strategy = Retry(
    total=3,
    backoff_factor=2,
    status_forcelist=[500, 502, 503, 504],
)

# Create a session with retry strategy and timeout
session = requests.Session()
session.mount('http://', HTTPAdapter(max_retries=retry_strategy))
session.mount('https://', HTTPAdapter(max_retries=retry_strategy))

# Define URL
url = 'https://www.lazada.co.th/shop-mobiles/?ajax=true&isFirstRequest=true&page='

try:
    # Make the request with timeout
    for _ in range (1,103):
        print("===============================================================")
        print("\t\t\tround",_);
        print("===============================================================")
        response = session.get(url+str(_), timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json();
        process();

except requests.RequestException as e:
    print("Error:", e)