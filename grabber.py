# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:51:59 2020


"""

import requests
import bs4

def img_grabber(link):
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text , 'lxml')
    count = 1
    for full_link in soup.select('.thumbimage'):
        img_link = full_link['src']
        img = requests.get('https:' + img_link)
        f = open(f'img_{count}.jpg' , 'wb')
        f.write(img.content)
        f.close()
        count = count + 1
        
    print('Images succesfully downloaded!')
        
img_grabber(input('Enter Wikipedia link: '))
