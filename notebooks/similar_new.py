import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 加载FlagEmbedding模型
flag_embedding = SentenceTransformer('bert-base-uncased')

# 指定txt文件目录和output目录
txt_dir = '/workspaces/paper/data/大学物理/大学物理分节'  # 替换为实际的txt文件目录路径
output_dir = '/workspaces/paper/output/后处理大学物理'  # 替换为实际的output目录路径
output_excel_path = '/workspaces/paper/result.xlsx'  # 替换为实际的输出Excel文件路径

# 存储所有实体及其对应的文件名和相似度
all_entities = []

# 遍历txt文件目录下的所有txt文件进行处理
for txt_file in os.listdir(txt_dir):
    # 构建txt文件路径和对应的output文件路径
    txt_path = os.path.join(txt_dir, txt_file)
    output_file = os.path.splitext(txt_file)[0] + '.txt'
    output_path = os.path.join(output_dir, output_file)

    # 加载txt文件内容
    with open(txt_path, 'r') as file:
        txt_content = file.read()

    # 加载output文件中的实体
    entities = []
    with open(output_path, 'r') as file:
        for line in file:
            entity = line.strip().replace('(', '').replace(')', '').split(',')
            entities.append((entity[0].strip(), entity[1].strip()))

    # 计算实体与txt文件的相似度并保存结果
    for entity in entities:
        entity_text = entity[1]
        txt_sentence = [txt_content]
        entity_sentence = [entity_text]

        entity_embedding = flag_embedding.encode(entity_sentence)
        txt_embedding = flag_embedding.encode(txt_sentence)

        similarity = cosine_similarity(entity_embedding, txt_embedding)[0][0]
        similarity_percentage = int(similarity * 100)

        all_entities.append((entity[0], txt_file, similarity_percentage))

    print(f"{txt_file}已完成")

# 创建DataFrame并保存到Excel
df = pd.DataFrame(all_entities, columns=['实体', '文件名', '相似度'])
df.to_excel(output_excel_path, index=False)