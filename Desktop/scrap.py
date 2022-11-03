import requests
from bs4 import BeautifulSoup 
import pandas as pd

url="https://www.al-hamdoulillah.com/invocations/reveil.html"
# url="https://www.al-hamdoulillah.com/invocations/seance-rassemblement.html"
res=requests.get(url)
soup=BeautifulSoup(res.text, "html.parser")
print((soup.select("#contenu h2")[0]))
nbrD = len(soup.select("#contenu h3"))
offset=(len(soup.select("#contenu p"))-2) / nbrD
duas=[]



for i in range(nbrD):
    # useless part
    # splited = (soup.select("#contenu a[download]")[0]).get('href').split('/')
    # end_splitted = splited[len(splited)-1].split('.')
    # mp3number = end_splitted[0]
    # print(end_splitted[0])


    _ = soup.select("#contenu p")[int((i*offset)+1): int((i*offset)+offset+1)]
    duas.append({
        "category": (soup.select("#contenu h2")[0]).text,
        "arabe": _[1].text,
        "french": _[3].text,
        "phonetic": _[5].text,
        "source": _[6].text,
        "audio_url": "https://www.al-hamdoulillah.com/invocations/mp3/"+((soup.select('#contenu h3')[i]).text).split('°')[1]+".mp3",
    })
print(duas)