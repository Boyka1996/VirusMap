from pyecharts import Map
import numpy as np
value = np.log10(np.array([1052, 104, 98, 83, 75, 69, 60, 51, 44, 40, 39, 33, 31, 19, 19, 18, 18, 15, 15, 13, 11, 10, 9, 7, 7, 5, 5, 4, 4, 3,3,1]))
attr = ["湖北","浙江","广东","河南","重庆","湖南","安徽","北京","四川","上海","山东","广西","江苏","海南","辽宁","江西","福建","陕西","黑龙江","河北","云南","天津","山西","内蒙古","甘肃","香港","贵州","吉林","宁夏","台湾","新疆","青海"]
map = Map("截至 2020-1-26 12:13:19 数据统计", width=1000, height=800)
map.add("",attr,value,is_map_symbol_show=True,maptype="china", is_visualmap=True, visual_text_color='#000',
    is_label_show=True,     visual_range=[np.min(value),np.max(value)])
map.render('r2.html')
map.render(path='r2.png')