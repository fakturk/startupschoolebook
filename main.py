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
    # print(content.prettify())
    pieces = []
    for c in content:
        pieceLink = c['href']
        pieceTitle = c.find(class_='piece-title').text
        pieceAuthor = c.find(class_='piece-author').text
        articleUrl = pieceLink
        article = requests.get(articleUrl)
        articleSoup = BeautifulSoup(article.text, 'html.parser')
        # kill all script and style elements
        for script in articleSoup(["script", "style"]):
            script.decompose()    # rip it out
        print(pieceTitle,pieceAuthor,pieceLink)
        pieceContent = articleSoup.text
        
        piece = [pieceTitle,pieceAuthor,pieceLink,pieceContent]
        pieces.append(piece)
        print(pieceTitle,pieceAuthor,pieceLink,pieceContent)
        # print(c.prettify())
        # piece = soup.find_all(class_='piece')
        # # print(c)
        # for p in piece:
        #     print(p.text)
        
    # print(content)
    articles[span]=pieces
    
print(articles)
# onearticleurl = 'http://paulgraham.com/bronze.html'
# one = requests.get(onearticleurl)
# oneSoup = BeautifulSoup(one.text, 'html.parser')
# # kill all script and style elements
# for script in oneSoup(["script", "style"]):
#     script.decompose()    # rip it out
# print(oneSoup.text)
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