# 切换为测试环境
url = "http://hmshop-test.itheima.net"

# 切换为生产环境
# url = ""

import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_PATH, "data")



"""
print(f'当前路径为：{os.getcwd()}')
relative_path = "my_folder/my_file.txt"

a = os.path.abspath(relative_path)
print(a)



# 文件路径
file_path = "/home/user/projects/my_file.txt"

# 获取目录部分
dir_path = os.path.dirname(file_path)
print("目录部分:", dir_path)


# 目录路径
dir_path = "/home/user/projects/my_folder"

# 获取父目录
parent_dir = os.path.dirname(dir_path)
print("父目录:", parent_dir)
"""