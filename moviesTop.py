from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as opening
url = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&view=advanced"
openedUrl = opening(url)
html = openedUrl.read()
openedUrl.close()
pageSoup = soup(html, "html.parser")
items = pageSoup.findAll("div", {"class": "lister-item mode-advanced"})
# print(soup.prettify(items[0]))
# print(first[0].text.strip())
fileName = "moviesList.csv"
f = open(fileName, 'w')
headers = "Serial Number, Title,Year\n"
f.write(headers)
for item in items:
    first = item.findAll("h3", {"class": "lister-item-header"})
    title = first[0].text.strip()
    title = title.split('.')
    numbers = title[0]  # serial number
    newTitle = title[1]
    newTitle = newTitle.split('(')
    finalTitle = newTitle[0].strip()  # movie title
    year = newTitle[1][:-1]  # movie year
    f.write(numbers + ',' + finalTitle.replace(',','') + ',' + year + '\n')


