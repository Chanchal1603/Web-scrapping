# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H4FQhRiTliURBQu48WAKDXGdXBAeVHjd
"""

import bs4

import requests as rq

r = rq.get("https://www.flipkart.com/search?q=laptops900")

r.status_code

r.text

soup = bs4.BeautifulSoup(r.text, "html.parser")

soup.title

soup.title.get_text()

myDivs = soup.findAll('div', attrs={'class':'_1vC4OE'})

for item in myDivs:
  
  print(item.get_text(), end ="\n\n")

