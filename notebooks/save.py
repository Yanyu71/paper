import os
import pandas as pd

# 指定目录路径
directory = '/workspaces/paper/output/词频统计/大学物理'

# 获取目录中的所有文件名
files = os.listdir(directory)

# 初始化空的DataFrame
df = pd.DataFrame(columns=['键值对', '数量'])

# 逐个读取文件并提取数据
for file in files:
    file_path = os.path.join(directory, file)
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 提取键值对数据
    output_data = []
    for line in lines:
        line = line.strip()
        key_value, count = line.rsplit(':', 1)
        key = key_value.strip('()').split(',')
        key = [item.strip() for item in key]
        try:
            count = int(count.strip())
        except ValueError:
            continue  # 跳过无效的数量
        output_data.append((tuple(key), count))
    
    # 将数据添加到DataFrame
    df = df.append(pd.DataFrame(output_data, columns=['键值对', '数量']), ignore_index=True)

# 将数据导出为Excel文件
df.to_excel('output_fenjie.xlsx', index=False)