# coding=UTF-8
#一般
import urllib.request as request

src="https://www.ntu.edu.tw/"
with request.urlopen(src) as res:
    data = res.read().decode('utf-8')
    print(data)

#Json
import urllib.request as request
import json
src="https://www.ntu.edu.tw/"
with request.urlopen(src) as res:
    data = json.load(res)
    print(data)