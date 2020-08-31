# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 22:48:24 2019

@author: Lenovo
"""

import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJXP4/ref=sr_1_3?crid=DGCMK62U0F3B&keywords=boat+bluetooth+headphones&qid=1575830467&s=electronics&sprefix=boat+%2Celectronics%2C325&sr=1-3'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def check_price():
    
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(id = "productTitle").get_text()
    
    title = soup.find(id ="productTitle").get_text()
    price = soup.find(id ="priceblock_ourprice").get_text()
    print(price)
    converted_price = float(price[1:3]+ price[4:7])
    print(converted_price)
    if (converted_price > 1450):
        send_mail()
    
    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('1995vaibhavbv@gmail.com', 'tyajyefdzwjumpsz')
    
    subject = "HEY PRICE FELL DOWN"
    body = 'https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJXP4/ref=sr_1_3?crid=DGCMK62U0F3B&keywords=boat+bluetooth+headphones&qid=1575830467&s=electronics&sprefix=boat+%2Celectronics%2C325&sr=1-3'
    
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
            "1995vaibhavbv@gmail.com",
            "vaibhavbv174@gmail.com",
            msg
    )
    print("HEY EMAIL HAS BEEN SENT")
    server.quit()
       
check_price()
# this is awesome
