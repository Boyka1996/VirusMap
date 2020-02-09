# coding=utf-8
import requests
from xlwt import *

'''别问为啥不用井号注释，键盘上半边坏了'''
'''操作太频繁可能会并发量超过约定并发配额，限制访问，可以多申请几个ak轮着来'''
'''这一块是创建表格，最后要往里面天'''
file = Workbook(encoding='utf-8')
table = file.add_sheet('data')
try:
    count = 0
    for page_num in range(1000):
        print(count)
        url = 'http://api.map.baidu.com/place/v2/search?query=小区&page_size=20&page_num=' + str(
            page_num) + '&region=青岛&output=json&ak=9SSSntq2LARQWCQIdCekthuvehV33snF'
        '''
        服务文档：http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
        query，page_size等参数看上面，page_num是查询到的第几页
        ak所有ip都能用，下个月就关了，可以自己申请一个
        
        '''
        response = requests.get(url)
        print(response.json())
        data = response.json()['results']
        print(data)
        if len(data) == 0:
            '''查完了就结束'''
            break
        for community in data:
            '''获取小区名字、地区和地址
            有的地址是包含山东省请青岛市和所在区的'''
            print(count)
            name = community['name']
            area = community['area']
            address = community['address']
            address = address.replace('山东省', '')
            address = address.replace('青岛市', '')
            address = address.replace(area, '')

            '''下面是往表格里写'''
            table.write(count, 0, name)
            table.write(count, 1, area)
            table.write(count, 2, address)
            count += 1


except Exception as e:
    '''中间歇逼了保存一下'''
    file.save('data.xlsx')
    print(e)

'''保存到本地'''
file.save('小区信息.xlsx')
