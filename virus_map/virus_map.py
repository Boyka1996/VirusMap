import time
import json
import requests
import numpy as np
from datetime import datetime
from pyecharts.charts import Map
from pyecharts import options as opts

'''从腾讯新闻请求获取感染数据'''
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(time.time() * 1000)
data = json.loads(requests.get(url=url).json()['data'])

'''获取各个省份感染数据'''
china_data = data['areaTree'][0]
virus_data = china_data['children']

'''五个数组：确诊感染人数、疑似感染人数、死亡人数、治愈人数、省份'''
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
print(province_array)
print(confirm_array)
print(dead_array)
print(heal_array)

value = np.array(confirm_array)
key = province_array
today = datetime.today()
date_format = "%Y.%m.%d %H:%M:%S"
s = today.strftime(date_format)

'''用pyecharts作图'''
province_info = [[province_array[i], confirm_array[i]] for i in range(len(province_array))]
china_map = Map()
china_map.set_global_opts(title_opts=opts.TitleOpts(title=s + " 确诊人数"), visualmap_opts=opts.VisualMapOpts(max_=500))
china_map.add("确诊人数>500", province_info, maptype="china")
china_map.render('map1.html')
