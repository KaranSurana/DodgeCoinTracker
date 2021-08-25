from bs4 import BeautifulSoup
import requests
import winsound
from datetime import datetime
import time

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 200  # Set Duration To 1000 ms == 1 second
prev=0
 
while True:
    html_text=requests.get('https://in.finance.yahoo.com/cryptocurrencies/').text
    soup=BeautifulSoup(html_text,'lxml')
    job=soup.find('span',class_="Trsdu(0.3s)",attrs={"data-reactid": "284"}).text
    winsound.Beep(frequency, duration)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Dodge Coin Price Is",job,"at", current_time)
    time.sleep(15)
