# -*- coding: utf-8 -*-
# @File : 网页文件re处理录入excel.py
# @Author : hyb
# @Time : 2022/7/27 22:02
# @Software : PyCharm
import re

from openpyxl import Workbook

f = open('html.html','r',encoding='utf-8')
data = f.read()

obj = re.compile(r'<li>.*?title">(?P<title>.*?)</span>.*?<p class="">.*?<br>\s*(?P<time>.*?)&nbsp;.*?&nbsp;/&nbsp;(?P<type>.*?)\s*</p>.*?property="v:average">(?P<star>.*?)</span>.*?content="10.0"></span>.*?<span>(?P<num>.*?)人评价</span>.*?<span class="inq">(?P<ing>.*?)</span>',re.S)
res_data = obj.finditer(data)

wb = Workbook()
sheet = wb.active
sheet.append(['电影名称','时间','电影类型','打分','评分人数','简介'])
for it in res_data:
    sheet.append([it.group('title'),it.group('time'),it.group('type'),it.group('star'),it.group('num'),it.group('ing')])
wb.save('网页文件re处理录入excel.xlsx')
wb.close()
