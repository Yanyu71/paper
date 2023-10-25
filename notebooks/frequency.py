import re
import os

def extract_chinese_and_english(text):  #提取文本中的中英文内容
    pattern = r'\((.*?),\s*(.*?)\)'
    matches = re.findall(pattern, text)
    return matches

def count_phrases_in_text(phrases, text):
    phrase_count = {f"({chinese}, {english})": 0 for chinese, english in phrases}

    for chinese, english in phrases:
        count = text.count(chinese)
        phrase_count[f"({chinese}, {english})"] = count

    return phrase_count

def frequency_batch(phrases_filename,text_filename,output_filename):
    with open(phrases_filename, "r", encoding="utf-8") as phrases_file:
        phrases_content = phrases_file.read()

    extracted_phrases = extract_chinese_and_english(phrases_content)

    with open(text_filename, "r", encoding="utf-8") as text_file:
        input_text = text_file.read()

    result = count_phrases_in_text(extracted_phrases, input_text)

    with open(output_filename, "w", encoding="utf-8") as output_file:
        for phrase, count in result.items():
            output_file.write(f"{phrase}: {count}\n")
    print(f"结果已保存至 {output_filename}")


def main():
    phrases_path = r"/workspaces/paper/output/后处理大学物理"
    text_path = r"/workspaces/paper/data/大学物理/大学物理分节"
    output_path = r"/workspaces/paper/output/词频统计/大学物理分节"
    for fileName in os.listdir(phrases_path):
        frequency_batch(phrases_path+'/'+fileName, text_path+'/'+fileName, output_path+'/'+fileName)
        #+'/'+fileName
    print("词频统计完成")

if __name__ == "__main__":
    main()
