import os
import json

def process_jsonfile(filepath):
    entity_list = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        json_string = f.read()

    try:
        json_list = json.loads(json_string)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return []

    for item in json_list:
        knowledge_points_list = item.get("knowledge_points", [])
        for knowledge_dict in knowledge_points_list:
            entity_list.append((knowledge_dict.get("title", ""), knowledge_dict.get("en", "")))  # 使用元组

    new_entity_list = list(set(entity_list))  # 去重
    return new_entity_list

input_path = r'/workspaces/paper/output/大学物理1/大学物理'
output_path = r'/workspaces/paper/output/后处理大学物理'

for fileName in os.listdir(input_path):
    input_file_path = os.path.join(input_path, fileName)
    output_file_path = os.path.join(output_path, fileName)   
    text = process_jsonfile(input_file_path)   
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for item in text:
            s = f"({item[0]}, {item[1]})\n"  # 在这里添加括号
            file.write(s)
