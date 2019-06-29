import ebooklib
from ebooklib import epub

import requests
# from lxml import html
from bs4 import BeautifulSoup


url = 'https://www.startupschool.org/library'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
# soup.find_all(class_='piece-title')
titles = soup.find_all(class_='title')
articles={}
# print(titles)
for t in titles:
    # print(t)
    span = t.span.text
    print(span)
    content=t.find_next_sibling(class_="content") 
    for c in content:
        pieceLink = c['href']
        pieceTitle = c.find(class_='piece-title').text
        pieceAuthor = c.find(class_='piece-author').text
        # print(pieceTitle,pieceAuthor,pieceLink)
        piece = [pieceTitle,pieceAuthor,pieceLink]
        # print(c.prettify())
        # piece = soup.find_all(class_='piece')
        # # print(c)
        # for p in piece:
        #     print(p.text)
        
    # print(content)
    articles[span]=piece
print(articles)
# tree = html.fromstring(r.content)
# print(tree)
#This will create a list of titles:
# titles = tree.xpath('//div[@class="title"]/text()')
# articles = r.json()
# print(articles)
# print(titles)

book = epub.read_epub('12factor.epub')
index = book.get_item_with_href('index.xhtml')
# print(index)