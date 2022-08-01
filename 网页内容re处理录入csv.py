# -*- coding: utf-8 -*-
# @File : 网页内容re处理录入csv.py
# @Author : hyb
# @Time : 2022/7/27 22:44
# @Software : PyCharm
import csv
import re

f = open('html.html','r',encoding='utf-8')
data = f.read()
f.close()

obj = re.compile(r'<li>.*?title">(?P<title>.*?)</span>.*?<p class="">.*?<br>\s*(?P<time>.*?)&nbsp;.*?&nbsp;/&nbsp;(?P<type>.*?)\s*</p>.*?property="v:average">(?P<star>.*?)</span>.*?content="10.0"></span>.*?<span>(?P<num>.*?)人评价</span>.*?<span class="inq">(?P<ing>.*?)</span>',re.S)
res_data = obj.finditer(data)

fo = open("html2csv.csv",'w',encoding='utf-8')
csv_writer= csv.writer(fo)

for it in res_data:
    dic = it.groupdict()
    dic['time'] = dic['time'].strip()
    csv_writer.writerow(dic.values())

