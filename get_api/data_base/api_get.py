
import requests;
import json;


data_process = {
                "product":"itemUrl",
                "price_product_2":"originalPrice",
                "price_product_1":"price",
                "discount":"discount",
                "sold":"itemSoldCntShow",
                "place":"location",
                "count_review":"review"
            }
data_test=[]
data_1=[]
key = data_process.keys();
for j in range(102):
    
    url = 'https://www.lazada.co.th/shop-consumer-electronics/?ajax=true&isFirstRequest=true&page='+str(j+1)+'&spm=a2o4m.home-th.3887232320.70.6fe67f6dFKnzPY';
    data = requests.get(url)
    data_all= data.json();
    for k in range(40):
        Id="product_"+str(k+1);
        data_process_1 = {
                "product":"",
                "price_product_2":"",
                "price_product_1":"",
                "image_product_1":"",
                "discount":"",
                "image_product_2":"",
                "data_product":"",
                "price_before":"",
                "Emoji":"",
                "sold":"",
                "place":"",
                "Recommended_shops":"",
                "count_review":"",
                "maket":"",
                "group":""
            }
        Product = {Id:{}}
        for i in key:
            try:
                data_process_1[i] = data_all['mods']['listItems'][k][data_process[i]];
            except:
                pass
        Product[Id]=data_process_1;
        data_1.append(Product);
    file_name = "data_"+str(j+1)+".json"
    # เขียน JSON object ลงในไฟล์
    with open(file_name, 'w') as json_file:
        json.dump(data_1, json_file, indent=2)




    



# url = 'https://www.lazada.co.th/shop-audio-headphones/?ajax=true&page=50&spm=a2o4m.home-th.3887232320.11.5f217f6dY15yZw';

# data = requests.get(url)
# data_all= data.json();
# # "mods" -> "filter"
# data_test = data_all['mods']["listItems"][0]["name"]
# print(data_test);





