from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

my_url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=6339e051-a000-4e1d-ac86-da630f28aeac&as-searchtext=iphone&sort=price_desc"
uClient = urlopen(my_url)
pageHtml = uClient.read()
uClient.close()
pageSoup = soup(pageHtml, "html.parser")
containers = pageSoup.findAll("div", {"class": "_3O0U0u"})
# print(len(containers)) total number of products
# print(soup.prettify(containers[0])) all information of one product
product1 = containers[0]
# finding title
title = product1.div.img['alt']
# print(title)
# finding price
price = product1.findAll("div", {"class": "col col-5-12 _2o7WAb"})
# print(price[0].text)
# finding ratings
rating = product1.findAll("div", {"class": "niH0FQ"})
# print(rating[0].text)
# Creating a file
fileName = "appleProducts.csv"
f = open(fileName, "w")
columnNames = "Product Name,Pricing,Rating\n"
f.write(columnNames)
for container in containers:
    productName = container.div.img['alt']
    price_c = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_c[0].text.strip()
    rating_c = container.findAll("div", {"class": "niH0FQ"})
    rating = rating_c[0].text
    price = price.split("₹")
    newPrice = price[1]
    newPrice = newPrice.replace(",", "")
    newPrice = newPrice.split("N")
    rating = rating.split(',')
    newRate = rating[0]
    newRate = newRate.split('.')
    afterDecimal = newRate[1]
    finalPrice = "Rs." + newPrice[0]
    finalRating = newRate[0]+"."+afterDecimal[0]
    print(productName.replace(",","|" ), finalPrice, finalRating)
    f.write(productName.replace(",","|" ) + "," + finalPrice + "," + finalRating + '\n')