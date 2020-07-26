import yaml
def get_yaml_data(yaml_file):
    # 打开yaml文件
# 直接打开读出来
    f = open(yaml_file,'r',encoding='utf-8')
    result = f.read()
    # 转换成字典读出来
    a = yaml.load(result,Loader=yaml.FullLoader)
    return a
