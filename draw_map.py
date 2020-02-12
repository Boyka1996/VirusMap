import numpy as np
from pyecharts.charts import Map, Geo

'''数据来源：国家及各省市地区卫健委'''
value = np.array(
    [4586, 428, 311, 278, 277, 200, 165, 162, 145, 142, 129, 114, 101, 101, 78, 70, 65, 63, 46, 43, 41, 35, 29, 26, 18,
     17, 14, 14, 12, 10, 8, 7, 6, 1])
attr = ["湖北", "浙江", "广东", "河南", "湖南", "安徽", "重庆", "江西", "山东", "四川", "江苏", "北京", "上海", "福建", "广西", "云南", "河北",
        "陕西", "海南", "黑龙江", "辽宁", "山西", "天津", "甘肃", "内蒙古", "宁夏", "吉林", "新疆", "贵州", "香港", "台湾", "澳门", "青海", "西藏"]

'''在map_virus.add()设置地图显示参数。'''
map_virus = Map("截至 2020-1-30 14：42 数据统计", width=1000, height=800)
map_virus.add("China", attr, value, is_map_symbol_show=True, maptype='china', is_visualmap=True, is_piecewise=True,
              visual_text_color='#000',
              is_label_show=True, pieces=[
        {"max": 10000, "min": 1001, "label": ">1000"},
        {"max": 1000, "min": 500, "label": "500-1000"},
        {"max": 499, "min": 200, "label": "200-499"},
        {"max": 199, "min": 100, "label": "100-199"},
        {"max": 99, "min": 10, "label": "10-99"},
        {"max": 9, "min": 1, "label": "1-9"}])
map_virus.render(path='1月30日疫情地图.png')
# map_virus.render('1月30日疫情地图.html')
