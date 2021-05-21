from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

trs=soup.select('#old_content > table > tbody > tr')

for tr in trs:
    t_tag=tr.select_one('td.title > div > a')
    n_tag=tr.select_one('td:nth-child(1) > img')
    s_tag=tr.select_one('td.point')
    if t_tag is not None :
        num=n_tag['alt']
        title=t_tag.text
        star=s_tag.text
        doc={
            'num':num,
            'title':title,
            'star':star
            }
        db.movies.insert_one(doc)