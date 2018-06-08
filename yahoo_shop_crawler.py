import os
import requests
import pandas as pd
import numpy as np
import datetime
from bs4 import BeautifulSoup
import re
import time
url = 'https://tw.buy.yahoo.com'
sitemap_url = 'https://tw.buy.yahoo.com/help/helper.asp?p=sitemap&hpp=sitemap'

resp = requests.get(sitemap_url)
resp.encoding = 'big5' # sitemap is using big5 charset, the other pages are using utf8
soup = BeautifulSoup(resp.text, 'html5lib')

sub_dict = {}
result = pd.DataFrame(columns=['catgory_no','category', 'name', 'price','url'])
subs = soup.find_all(href=re.compile("sub"))
for sub in subs:
    tail = list(sub.attrs.values())[0]
    url_sub = url + tail
    sub_no = re.split('=', tail)
    sub_dict[sub_no[1]] = sub.string

index=0
for key, value in sub_dict.items():
    resp_sub1 = requests.get(url+'/?sub='+key)
    soup_sub1 = BeautifulSoup(resp_sub1.text, 'html.parser')
    item_list = soup_sub1.find_all("ul", class_="pdset")
    for item in item_list:
        item_text = item.find("div", class_="text")
        item_price = item.find("span", class_="red-price")
        item_url = item.find("a", href=True)
        item_dict = {'catgory_no':key,'category':value,'name':item_text.string,'price':item_price.string,'url':item_url['href']}
        result.loc[index] = item_dict
        index = index +1
    time.sleep(0.3) # fetch data gently

print(np.where(pd.isnull(result)))
result.to_csv('yahoo_shop_fig.csv', index=True, header=True, encoding='utf-8-sig')
