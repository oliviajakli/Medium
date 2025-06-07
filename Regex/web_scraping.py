# Author: Olivia Jákli
# Example #4
# Extract product titles from a webpage using regex.

import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://www.givenchy.com/us/en-US/women/bags')
soup = BeautifulSoup(page.content, 'html.parser')
products = soup.find_all('div', class_='product-infos')
content = str(page.content)

title_pattern = r'class="product-name">(.*?)<\/h4>'
titles = re.findall(title_pattern, content)

with open('product_titles.txt', 'w') as file:
    for title in titles:
        product_title = re.sub(r'<.*?>', '', title)  # Remove HTML tags
        product_title = product_title.strip()  # Remove leading/trailing whitespace
        file.write(product_title + '\n')

print(f"Extracted {len(titles)} product titles and saved to 'product_titles.txt'.")