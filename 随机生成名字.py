# -*- coding: utf-8 -*-
# @File : 随机生成名字.py
# @Author : hyb
# @Time : 2022/7/29 21:07
# @Software : PyCharm
import faker as faker

alex = faker.Faker(locale="zh_CN")
name = []
for i in range(10000):
    name.append(alex.name())
# print(name)
for i in name:
    if "丁" in i:
        print(i)
    elif "洪" in i:
        print(i)