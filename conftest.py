    # #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2021/10/3 6:07 下午
# @Author :Amaris
# @File   :conftest.py.py

# pytest执行时函数为中文是无法打印
# 解决方案:在同级或者父级文件夹下新建conftest.py文件，然后添加一个hook函数
# 参考链接：https://blog.csdn.net/qq_27371025/article/details/118353968
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.aname = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

