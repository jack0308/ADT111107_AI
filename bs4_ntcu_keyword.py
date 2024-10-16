import requests
from bs4 import BeautifulSoup

url = 'https://2023ntcu.ntcu.edu.tw/'
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, 'html.parser')
# 設定關鍵詞
keyword = "國立臺中教育大學"  # 您可以根據需要更改關鍵詞


# 使用 stripped_strings 获取所有文本内容
text_content = ' '.join(soup.stripped_strings)

# 统计关键词出现次数
keyword_count = text_content.count(keyword)

print(f"关键词 '{keyword}' 出现{keyword_count}次")
