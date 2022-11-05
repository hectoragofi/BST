from bs4 import BeautifulSoup
import requests
import time
from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()

name = input("Enter ticker symbols to track ")
name = name.split(" ")

def getInfo(namenum):
    url = f'https://finance.yahoo.com/quote/{name[namenum]}/'
    source = requests.get(url).text

    global cname, marketprice,change

    soup = BeautifulSoup(source, 'lxml')
    cname = soup.find('h1', class_='D(ib) Fz(18px)').text
    marketprice = soup.find('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    change = soup.find('fin-streamer', class_='Fw(500) Pstart(8px) Fz(24px)').text

    return cname, marketprice, change

def gtable():

    table = Table()
    table.add_column("Name")
    table.add_column("Trade Price")
    table.add_column("Change")

    for i in range(len(name)):
        getInfo(i)
        if float(change) >= 0:
            changeColor = "[green]"
        else:
            changeColor = "[red]"

        table.add_row(f"{cname}", f"{marketprice}", f"{changeColor}{change}")
        i = i + 1
    
    return table

with Live(gtable(), refresh_per_second=1) as live:
    while(True):
        time.sleep(0.4)
        live.update(gtable())
