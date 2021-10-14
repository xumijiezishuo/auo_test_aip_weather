# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2021/10/3 5:09 下午
# @Author :Amaris
# @File   :run.py.py

import requests
import pytest
import logging
import allure_pytest



class TestRun:
    # todo：因为方法参数个数不可控，使用不定参数数进行传参



    # 4、测试数据与代码分离，将测试数据存入excel中，然后读取文件中的数据作为方法的参数
    @pytest.mark.parametrize('data,result',
                             [({'city': '深圳', 'key': 'c2c51491d6402280036c8b9f661b42ef'},'查询成功!'),
                              ({'city': '广州', 'key': 'c2c51491d6402280036c8b9f661b42ef'},'查询成功!'),
                              ({'city': '广州', 'key': ''}, '查询成功!')
                              ])
    def test_post(self,data,result):
        url = "https://apis.juhe.cn/simpleWeather/query"
        res = requests.post(url=url, data=data)
        # logging.info("这是断言前的语句****************")

        print(res.json())
        assert res.json()['reason'] == result

    # #取数测试
    # data_list = [{'a':'1','b':'2'},{'name':'lan','sorce':[{'语文':99,'数学':100}]},{'职位':'学习委员'}]
    # data_dict = {'name':'lan','sorce':[{'语文':99,'数学':100}]}
    # print(f"****{data_list[1]['sorce'][0]['数学']}")
    # print(f"****{data_dict['sorce'][0]['语文']}")
    # j = 0
    # list1 = []
    # for i in data_dict:
    #     j += 1
    #     print(f'这是第{j}次取数，key取数值为{i}')
    #     print(f'这是第{j}次取数，value取数值为{data_dict[i]}')
    #     list1.append(data_dict[i])
    #
    # a = [i for i in data_list]
    # b = [i for i in data_dict]
    # # c = [data_dict[i] for i in data_dict]--不可用会报错
    # print(a)
    # print(b)
    # print(list1)






    # # 3、导入pytest包，使用pytest的parametrize进行测试参数化测试数据,其参数列表与方法的参数列表保持一一对应，测试数据是放在列表里面的,一组一组地放，注意中文乱码的解决
    # @pytest.mark.parametrize('data,result',
    #                          [({'city': '深圳', 'key': 'c2c51491d6402280036c8b9f661b42ef'},'查询成功!'),
    #                           ({'city': '广州', 'key': 'c2c51491d6402280036c8b9f661b42ef'},'查询成功!'),
    #                           ({'city': '广州', 'key': ''}, '查询成功!')
    #                           ])
    # def test_post(self,data,result):
    #     url = "https://apis.juhe.cn/simpleWeather/query"
    #     res = requests.post(url=url, data=data)
    #     print(res.json())
    #     assert res.json()['reason'] == result


    # # 2、封装，参数化测试数据，测试数据与代码分离，正向用例和反向用例
    # def test_post(self,url,data,result):
    #     res = requests.post(url=url, data=data)
    #     print(res.json())
    #     assert res.json()['reason'] == result



    # # 1、线性代码，基本使用--接口地址、入参、返回值断言验证
    # url = "https://apis.juhe.cn/simpleWeather/query"
    # data = {'city':'深圳', 'key':'c2c51491d6402280036c8b9f661b42ef'}
    # res = requests.post(url=url, data=data)
    # print(res.json())
    # assert res.json()['reason'] == '查询成功!'


# if __name__ == '__main__':
#     pass
    # 调试代码



    # # 2、封装方法，参数化
    # url = "https://apis.juhe.cn/simpleWeather/query"
    # data = {'city': '深圳', 'key': 'c2c51491d6402280036c8b9f661b42ef'}
    # result = '查询成功!'
    #
    # # 实例化对象
    # testobj = TestRun()
    #
    # # 调用方法
    # testobj.test_post(url,data,result)
