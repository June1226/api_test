# -*- coding: utf-8 -*-
# @Time  : 2022/8/7 10:52 PM
# Author : 拒绝内卷的小测试

import requests
import hashlib
import time

def bd_fy(word):
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

    header = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    # 后台提供开发者信息APP ID、密钥
    appid = "20220807001297811"
    key = "ZC9bXvwtBjkCX0ZUBaJw"
    # 接口文档定义随机数，没写几位，按举例的十位来填吧
    salt = str.split(str(time.time()), ".")[0]

    sign = appid + word + salt + key
    # 生成appid+q+salt+密钥的MD5值
    md5 = hashlib.md5()
    md5.update(sign.encode('utf-8'))
    data = {
    "q": word,
    "from": "auto",
    "to": "en",
    "appid": appid,
    "salt": salt,
    "sign": md5.hexdigest()
    }
    response = requests.post(url=url, headers=header, data=data)
    text = response.json()
    fy_word = text["trans_result"][0]["dst"]
    print(fy_word)
    return fy_word

if __name__ == '__main__':
    bd_fy(input('请输入您要翻译的内容：'))