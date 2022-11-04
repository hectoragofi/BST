from bs4 import BeautifulSoup
import requests

'''with open('testhtml.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')'''

'''article = soup.find('div', class_='article')
print(article)

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)'''

'''for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()'''

#article = soup.find('article')

#headline = article.h2.a.text
#print(headline)

name = input("Enter ticker symbol ")
url = f'https://finance.yahoo.com/quote/{name}/'
source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

name = soup.find('h1', class_='D(ib) Fz(18px)').text
marketprice = soup.find('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)').text
change = soup.find('fin-streamer', class_='Fw(500) Pstart(8px) Fz(24px)').text

f = "\n|{:^26}|{:^24}|{:^24}|"
print("|"+"="*76 + "|" + f.format("Name", "Trade Price", "Change"))
print("|"+"="*76 + "|" + f.format(name, marketprice, change))
print("|"+"="*76 + "|")
