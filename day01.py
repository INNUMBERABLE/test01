# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:53:55 2018

@author: lenovo
"""
print("好久发货时间都会感慨");
usermoney = 12,20,30
a = usermoney[1]
print(a)
a = 3
b = 2
c = [1,2,3]
print(c[0])
weeks = ['星期一',
     '星期二',
     '星期三',
     '星期四',
     '星期五',
     '星期六',
     '星期日']
print(weeks[0])
print(weeks[1])
print(weeks[2])
print(weeks[3])
print(weeks[4])
print("今天是" + weeks[5])#星期六
print(weeks[6])
msg = {"地址":"北京市海定区xxxxx",
 "手机号码":"123456789101",
 "寄信人":"chance"
 }

print(msg["地址"])
print(msg["手机号码"])
print(msg["寄信人"])
information = {"姓名":"花花",
               "身高":"185",
               "性别":"男",
               "年龄":"25"}
print(information["姓名"])
print(information["身高"])
print(information["性别"])
print(information["年龄"])
xzq = {'name':'薛子谦',
       'songs':['a','b','c','d'],
       '认识过的人':['af','df','cd']}
songs = xzq['songs']
print(len(songs))
print(max(xzq['认识过的人']))
tq = {'温度':['22','23','25','26','25'],
      '状况':['小雨','小雨','多云','晴','晴转多云'],
      '空气状况':['良','良','优','良','优']}
temperature = tq['温度']
print(len(temperature))
print(len(tq['温度']))
print(max(temperature))
print(temperature)

city_pinyin = input('请输入城市:')
print(city_pinyin)
address = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
print(address.format(city_pinyin))
print("欢迎使用全球天气app")
print("1、查看当前城市天气 2、查看其他城市天气3、保存当前城市天气")
menno = input("请输入菜单:")
if menno== '1':
    print("1、查看当前城市天气")
if menno == '2':
    print("2、查看其他城市天气")
if menno == 3:
    print("3、保存当前城市")
    
#引用其他工具包
import urllib.request as r
city_pinyin = input('请输入城市:')
address = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info = r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
import json
data = json.loads(info)
print("最高温度:" + str(data['main']['temp_max']) + "\n"
                   + "最低温度:" + str(data['main']['temp_min']) + "\n" 
                   + "天气:" + str(data['weather'][0]['description']) + "\n" 
                   + "气压:" + str(data['main']['pressure']) + "\n" + "风速:" + str(data['wind']['speed'])
                   )



 
 

