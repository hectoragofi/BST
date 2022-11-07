from bs4 import BeautifulSoup
import requests
import keyboard,time,os
from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()

name = input("Enter ticker symbols to track ")
global ii
ii = 1
defaultticks = ["NDAQ","AAPL","AMZN","MSFT","TSLA","GOOG","IBM","ORCL","V","F","KO"]
if(name == ''):
    name = defaultticks
else:
    name = name.split(" ")
    for i in range(1,len(name)):
        if(name[i] == ""):
            name = defaultticks
        else:
            break
        i = i + 1
if(os.name == 'posix'):
    os.system('clear')
else:
   os.system('cls')

def getInfo(namenum):
    url = f'https://finance.yahoo.com/quote/{name[namenum]}/'
    source = requests.get(url).text

    global cname, marketprice,change,changepercent,dayopen,dayhigh,daylow

    soup = BeautifulSoup(source, 'lxml')

    cname = soup.find('h1', class_='D(ib) Fz(18px)').text
    marketprice = soup.find('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    change = soup.find('fin-streamer', class_='Fw(500) Pstart(8px) Fz(24px)').text
    changepercent = soup.find('div',class_='D(ib) Mend(20px)').find_next('span').find_next('span').text.strip("()%")
    dayopen = soup.find('tr', class_='Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)').find_next('td').find_next('td').find_next('td').find_next('td').text
    dayrange = soup.find('tr', class_='Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text
    dayrange = dayrange.split("-")
    dayhigh = dayrange[1]
    daylow = dayrange[0]

def gtable():
    table = Table()
    table.add_column("Last")
    table.add_column("Trade Price")
    table.add_column("Change")
    table.add_column("Change %")
    table.add_column("Open")    
    table.add_column("Low")
    table.add_column("High")

    for i in range(len(name)):
        getInfo(i)
        if float(change) >= 0:
            changeColor = "[green]"
        else:
            changeColor = "[red]"
        table.add_row(f"{changeColor}{cname}", f"{changeColor}{marketprice}", f"{changeColor}{change}", f"{changeColor}{changepercent}%",f"{changeColor}{dayopen}",f"{changeColor}{daylow}",f"{changeColor}{dayhigh}")
        i = i + 1
    
    return table

with Live(gtable(), refresh_per_second=1) as live:
    if keyboard.is_pressed("a"):
        exit()
    while(True):
        ii = ii + 1
        time.sleep(0.4)
        live.update(gtable())
