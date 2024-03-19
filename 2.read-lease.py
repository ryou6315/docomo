import requests
from bs4 import BeautifulSoup
import pandas as pd

# 发送 GET 请求获取网页内容
url = 'https://help.okta.com/en-us/content/topics/releasenotes/production.htm'  # 替换为你要爬取的网页地址
response = requests.get(url)

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 示例：从网页中获取数据
data = []
items = soup.find_all('div', class_='relnotes_entry')
# print("找到的元素数量：", len(items))
# for item in items:
#     print(item)


for item in soup.find_all('div', class_='relnotes_entry'):
    title = item.find('h4').text.strip()
    description = item.find('p').text.strip()
    data.append([title, description])

# 查找包含修复内容的 <div> 标签
fixes_div = soup.find('div', class_='relnotes_bugs')

# 如果存在修复内容的 <div> 标签，则查找其中的所有 <li> 标签并打印其内容
data.append(["Fix","Fix-----"])
if fixes_div:
    
    ul_tag = fixes_div.find('ul')  # 在 fixes_div 下找到第一个 <ul> 标签
    # 如果找到 <ul> 标签，则获取其中的所有 <li> 标签并打印其内容
    if ul_tag:
        li_tags = ul_tag.find_all('li')  # 在 ul_tag 对象中找到所有 <li> 标签
        # 打印每个 <li> 标签的内容
        i = 0
        for li_tag in li_tags:
            i = i+1
            print(li_tag.get_text(strip=True))
            data.append([i,li_tag.get_text(strip=True)])
    else:
        print("未找到 <ul> 标签")
else:
    print("未找到修复内容的 <div> 标签")







# 将数据存入 DataFrame
df = pd.DataFrame(data, columns=['Title', 'Description'])

# 将数据保存为 Excel 文件
output_file = 'output.xlsx'  # 输出文件名
df.to_excel(output_file, index=False)

print("数据已保存到 Excel 文件:", output_file)
