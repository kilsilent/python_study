#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: nieshkc

# hight=dGint(inpuA
# weight=int(input('enter your weight:'))
# BMI=weight/hight
# if BMI<18.5:
#     print('so light')
# elif 18.5<BMI<25:
#     print('正常')
# elif 25<BMI<28:
#     print('过重')
# elif 28<BMI<32:
#     print('肥胖')
# elif BMI>32:
#o     print('太胖')

#学习字典代码

# name_dict={'张三':'北京','李四':'上海','王五':'重庆','赵六':'济南'}
#
# while 1:
#     Name=input('输入你的名字：')
#     print(name_dict)
#     if Name in name_dict:
#         print('呀！都是%s的老乡' % name_dict.get('Name'))
#     else:
#         print('抱歉，没有您的信息，咱俩认识一下')
#         Name=input('输入你的名字：')
#         Addr=input('输入你的家乡：')
#         name_dict[Name]=Addr


#链接redis数据库示例
import redis
import json
redis_ip='172.20.52.152'
passwd='Ufsoft123'


r = redis.Redis(host=redis_ip,port=6379,password=passwd,db=10,decode_responses=True)

if not r.exists('name_addr'):
    name_addr={'张三':'北京','李四':'上海','王五':'重庆','赵六':'济南'}
    r.hmset('name_addr',name_addr)
name_addr=r.hgetall('name_addr') #从数据库中读取name_addr字典的所有值
print(name_addr)

if not r.exists('addr_name'):
    addr_name={} #创建一个空的地址为键，名字为值的字典
    for k in name_addr: #名字取出来
        v=name_addr[k] #地址取出来
        print(k,v)
        try:
            if addr_name[v]: #如果地址为键，名字为值的字典存在的话
                addr_name[v].append(k) #就把地址追加入名字列表中
                print('addr_name')
        except:
            addr_name[v]=[k] #否则，建立一个字典中的名字列表
            print(v,addr_name[v])
            print(addr_name)
            json_dump=json.dumps(addr_name) #将数据压缩成字符串进行存储
            r.set('addr_name',json_dump)
json_loads=r.get('addr_name') #将字符串从redis中读出来
addr_name=json.loads(json_loads) #然后还原回字典格式
print(name_addr) #从数据库中读取addr_name字典的所有值
Name='example'
while  Name:
    Name=input('输入你的名字：')
    if not Name:
        exit(1)
    state=r.hexists('name_addr',Name) #判断用户名字是否存在
    if state:
        addr_val=r.hget('name_addr',Name)
        names=addr_name[addr_val]#获取同一个地方的所有名字
        print('呀！%s都是%s的老乡' % (names,addr_val))
        # r.delete('name_addr',Name) #临时删除某人就打开，删完就关闭
    else:
        print('请问你是哪里人啊，我记录下')
        Addr_new=input('输入你的家乡：')
        r.hset('name_addr',Name,Addr_new)
        if Addr_new not in addr_name:
                addr_name[Addr_new] = [Name]
        else:
            addr_name[Addr_new].append(Name)
        dump_data_new=json.dumps(addr_name)
        r.set('addr_name',dump_data_new)



