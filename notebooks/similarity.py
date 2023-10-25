import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 加载FlagEmbedding模型
flag_embedding = SentenceTransformer('bert-base-uncased')

# 加载txt文件内容
txt_path = '/workspaces/paper/data/大学物理/大学物理分节/§1.2质点运动学的基本问题.txt'
with open(txt_path, 'r') as file:
    txt_content = file.read()

# 加载output文件中的实体
output_path = '/workspaces/paper/output/后处理大学物理/§1.2质点运动学的基本问题.txt'
entities = []
with open(output_path, 'r') as file:
    for line in file:
        entity = line.strip().replace('(', '').replace(')', '').split(',')
        entities.append((entity[0].strip(), entity[1].strip()))

# 计算实体与txt文件的相似度并保存结果到Excel
similarities = []
for entity in entities:
    entity_text = entity[1]
    txt_sentence = [txt_content]
    entity_sentence = [entity_text]
    
    entity_embedding = flag_embedding.encode(entity_sentence)
    txt_embedding = flag_embedding.encode(txt_sentence)
    
    similarity = cosine_similarity(entity_embedding, txt_embedding)[0][0]
    similarity_percentage = int(similarity * 100)
    
    similarities.append((entity[0], txt_path, similarity_percentage))

# 创建DataFrame并保存到Excel
df = pd.DataFrame(similarities, columns=['实体', '文件名', '相似度'])
output_excel_path = '/workspaces/paper/result.xlsx'
df.to_excel(output_excel_path, index=False)