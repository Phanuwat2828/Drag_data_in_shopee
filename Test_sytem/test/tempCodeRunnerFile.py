import os
import json


path_here = os.getcwd();
print(path_here)
path ="./Data_link/data_link_all.json"
with open(path, 'r', encoding='utf-8-sig') as file:
    data = json.load(file)