import os
import pandas as pd

# 指定要读取的目录路径
directory_path = '/workspaces/paper/output/词频统计/大学物理分节'

# 创建一个空的DataFrame来保存数据
data = pd.DataFrame(columns=['中文名', '英文名', '数字', '文件名'])

# 遍历目录中的所有文件
for filename in os.listdir(directory_path):
    # 构建文件的完整路径
    file_path = os.path.join(directory_path, filename)

    # 读取文件中的数据
    output_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            key_value = line.strip().split(':')
            if len(key_value) == 2:
                key, value = key_value
                chinese_name, english_name = key.split(', ', 1)
                output_data[chinese_name.strip(), english_name.strip()] = int(value.strip())

    # 将输出数据添加到DataFrame中
    for (chinese_name, english_name), value in output_data.items():
        file_name = os.path.basename(file_path)
        data = data.append({'中文名': chinese_name, '英文名': english_name, '数字': value, '文件名': file_name}, ignore_index=True)

# 将DataFrame保存为Excel文件
data.to_excel('output_fenjie.xlsx', index=False)