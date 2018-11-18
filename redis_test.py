#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: nieshkc
import redis
import json
r = redis.Redis(host="172.20.52.152",port=6379,db=0)
data={'name':'TOM','age':23,'sex':'female'}
new_data=json.dumps(data)
r.set('data',new_data)
res=r.get('data')
new_res=json.load(res)
print(new_res)
print(type(new_res))
print(res)
print(type(res))


