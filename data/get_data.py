import time
import json
import requests

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(time.time() * 1000)
data = json.loads(requests.get(url=url).json()['data'])
china_data = data['areaTree'][0]
virus_data = china_data['children']
print(len(data))
print(type(data))
print(china_data.keys())

print(china_data['total'])
# print(type(data))
# print(data['areaTree'])
# print(len(data['areaTree']))
print(china_data.keys())
print(china_data['children'])
print(len(virus_data))
print(virus_data[0]['total'])
# for i in range(len(data['areaTree'])):
#     print(data['areaTree'][i]['name'])
# print(data.keys())
confirm_array = []
suspect_array = []
dead_array = []
heal_array = []
province_array = []
for province_data in virus_data:
    confirm_array.append(province_data['total']['confirm'])
    suspect_array.append(province_data['total']['suspect'])
    dead_array.append(province_data['total']['dead'])
    heal_array.append(province_data['total']['heal'])
    province_array.append(province_data['name'])

print(confirm_array)
print(province_array)
print()
print()