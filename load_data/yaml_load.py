import yaml

# yaml格式内容数据的读取
def load(path):
    file = open(path,'r',encoding='utf-8')
    data = yaml.load(file,Loader=yaml.FullLoader)
    print(data)
    return data


