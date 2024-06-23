


test = open('./log/setting.txt',mode='r',encoding='utf-8');
# for i in test.readlines():
#     print(i)
data = test.readlines()
def setting():
    data_setting = []
    for i in range(len(data)):
        data_setting.append(data[i].replace('\n','').split('=')[1]);
    return data_setting;


print(setting())
# print(test.readlines()[0].replace('\n','').split('='))
# print(test.readlines()[1].replace('\n','').split('='))
# print(test.readlines()[1].replace('\n','').split('='))
