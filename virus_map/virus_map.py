import time
import json
import requests
import numpy as np
from datetime import datetime
from pyecharts.charts import Map
from pyecharts import options as opts

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(time.time() * 1000)
data = json.loads(requests.get(url=url).json()['data'])
china_data = data['areaTree'][0]
virus_data = china_data['children']
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
# value=np.log2(np.array(confirm_array))
# value=np.maximum(value, 0)
# print(value)
value=np.array(confirm_array)
key=province_array
today = datetime.today()
format = "%Y.%m.%d %H:%M:%S"
s = today.strftime(format)

province_info = [[province_array[i], confirm_array[i]] for i in range(len(province_array))  ]
china_map = Map()
china_map.set_global_opts(title_opts=opts.TitleOpts(title=s+" 确诊人数"),visualmap_opts=opts.VisualMapOpts(max_=500))
china_map.add("确诊人数>500", province_info, maptype="china")
china_map.render('map1.html')
china_map.render(path='virus_statistics1.png')
#
# map = Map("截至 "+s+" 确诊人员数据统计", width=1000, height=800)
# map.set_global_ops=op
# map.add("",key,value,is_map_symbol_show=True,maptype="china", is_visualmap=True, visual_text_color='#000',
#     is_label_show=True)
# # map.add("",key,value,is_map_symbol_show=True,maptype="china", is_visualmap=True, visual_text_color='#000',
# #     is_label_show=True,     visual_range=[np.min(value),np.max(value)])
# map.render('virus_statistics.html')
# map.render(path='virus_statistics.png')