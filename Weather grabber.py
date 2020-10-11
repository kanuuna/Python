# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:33:56 2020

@author: Antti

This program grabs weather data from UK Meteorological Office
"""

import requests
import bs4


post_code = input('Enter first 3 digits of UK postcode: ')

result = requests.get(f'https://www.metoffice.gov.uk/weather/forecast/gcw21fpb4#?nearestTo={post_code}20(United%20Kingdom)&date=2020-10-10')

soup = bs4.BeautifulSoup(result.text , 'lxml')

soup

soup_search = soup.select('.step-temp')

soup_summary = soup.select('.summary-text')

soup_precip = soup.select('.sig')

print("\nToday's chance of rain is: "+soup_precip[0].getText())

print(soup_summary[0].getText())

print(f'Temperatures for {post_code} for the next 10 hours')

print(soup_search[0].getText())

day_high = soup.select('.tab-temp-high')
day_low = soup.select('.tab-temp-low')



print("Today's max temp is: " + day_high[0].getText())
print("Today's min temp is: " + day_low[0].getText())

print('Temperatures for the following 3 days are: \n'+day_high[1].getText() + '\n' +day_high[2].getText() + '\n' + day_high[3].getText() )

input('Press any key + enter to close')