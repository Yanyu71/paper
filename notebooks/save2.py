import os
import pandas as pd

# 指定要读取的文件路径
file_path = '/workspaces/paper/output/词频统计/大学物理/§1.2质点运动学的基本问题.txt'

# 读取文件中的数据
output_data = {}
with open(file_path, 'r') as file:
    for line in file:
        key, value = line.strip().split(':')
        output_data[key.strip()] = int(value.strip())

# 创建一个空的DataFrame来保存数据
data = pd.DataFrame(columns=['中文名', '英文名', '数字', '文件名'])

# 将输出数据添加到DataFrame中
for key, value in output_data.items():
    chinese_name, english_name = key.split(', ')
    file_name = os.path.basename(file_path)
    data = data.append({'中文名': chinese_name, '英文名': english_name, '数字': value, '文件名': file_name}, ignore_index=True)

# 将DataFrame保存为Excel文件
data.to_excel('output_example.xlsx', index=False)