# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2021/10/13 2:50 下午
# @Author :Amaris
# @File   :test_inter.py
import requests
import pytest
from load_data import yaml_load

# 将文件的数据读取存到变量city里面
@pytest.mark.parametrize('city',yaml_load.load('../data/data.yaml'))
def test_post(city):
    url = "https://apis.juhe.cn/simpleWeather/query"
    # data={'city': city, 'key': key}

    res = requests.post(url=url, data=city)
    # logging.info("这是断言前的语句****************")

    print(res.json()['reason'])
    assert res.status_code == result

if __name__ == '__main__':
    pytest.main(['-v','-s'])

