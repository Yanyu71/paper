import pandas as pd
import openai

# 设置OpenAI API密钥
#openai.api_key = 'YOUR_API_KEY'
#openai.api_key = "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"
#openai.api_key = "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"
print(openai.api_base)
#openai.api_base = 'https://api.openai.com/v1'
#openai.api_base = 'https://api.xiamoai.top/v1'
#openai.api_key = 'sk-ScP6iCRfsRQKfGce47D6898b2aA44c369e58D8972aA86029'
#openai.api_key = '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'
# 读取Excel文件
excel_path = '/workspaces/paper/data/zhushi - example.xlsx'
df = pd.read_excel(excel_path)

# 获取第一列数据
column_data = df.iloc[:, 0]

# 调用ChatGPT生成描述并打印结果
for data in column_data:
    response = openai.Completion.create(
        engine='text-davinci-003',
        #model="gpt-3.5-turbo",
        prompt=data,
        max_tokens=30,
        n=1,
        stop=None,
        temperature=0.7
    )
    concept_description = response.choices[0].text.strip()
    print(concept_description)
    