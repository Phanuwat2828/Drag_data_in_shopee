import os
import json


path_here = os.getcwd();
path_here = os.path.abspath(os.path.join(path_here, os.pardir))
print(path_here)
path =path_here+"/Data_link/data_link_all.json"
with open(path, 'r', encoding='utf-8-sig') as file:
    data = json.load(file)
print(data);
# Get the current working direc

# Print the parent directory

