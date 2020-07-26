#!/usr/bin/env python3

import requests
import time
import threading
from xml.dom import minidom
def send_telegram(text: str):
    token = "token_yout_bot"
    url = "https://api.telegram.org/bot"
    channel_id = "@tg_channel"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })
global link
global oldlink
print("1")
req = requests.get('link_is_yt_channel')
doc = minidom.parseString(req.content)
findlink = doc.getElementsByTagName("link")[2]
oldlink = findlink.getAttribute("href")
print("2")
while(1 == 1):
 req = requests.get('link_is_yt_channel')
 doc = minidom.parseString(req.content)
 findlink = doc.getElementsByTagName("link")[2]
 link = findlink.getAttribute("href")
 time.sleep(60)
 print("3")
 if(oldlink != link):
    print(link)
    oldlink = link
    send_telegram("на канале что-то новенькое, бегом смотреть!:" + link)
 else:
    oldlink = link
