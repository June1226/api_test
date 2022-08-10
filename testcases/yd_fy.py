# -*- coding: utf-8 -*-
# @Time  : 2022/8/8 9:50 PM
# Author : 拒绝内卷的小测试

import hashlib
import uuid
import requests
import time

def yd_fy(word):
    url = 'https://openapi.youdao.com/api'

    header = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    time_curtime = int(time.time())
    uu_id = uuid.uuid4()
    app_id = "316472df7dc804a2"
    app_key = "vwfSY14Mic4P9EvOzKYK03s6LBXfKrW5"

    sign = hashlib.sha256((app_id + word + str(uu_id) + str(time_curtime) + app_key).encode('utf-8')).hexdigest()

    data = {
        'q': word,
        "from": "auto",
        "to": "en",
        'appKey': app_id,
        'salt': uu_id,
        'sign': sign,
        'signType': "v3",
        'curtime': time_curtime
    }

    response = requests.post(url=url, headers=header, data=data)
    text = response.json()
    fy_word = text["translation"][0]
    print(fy_word)
    return fy_word

if __name__ == '__main__':
    yd_fy(input('请输入您要翻译的内容：'))