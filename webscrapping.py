# -*- coding: utf-8 -*-
"""
Created on Mon May 25 04:00:58 2020

@author: Vishwas
"""
import requests 
from bs4 import BeautifulSoup 
import csv

   
URL = "https://coreyms.com/"
source = requests.get(URL).text
csv_file=open('websrap.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','Video_Link'])
   
soup = BeautifulSoup(source, 'lxml') 
   
for article in soup.find_all('article'):
    headline=article.a.text
    print(headline)
    summary=article.find('div',class_=('entry-content')).p
    print(summary)
    try:
        vid_src=article.find('iframe',class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id=vid_id.split('?')[0]
        yt_link=f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link=None
    print(yt_link)
    print()
    
    csv_writer.writerow([headline,summary,yt_link])
csv_file.close()    


