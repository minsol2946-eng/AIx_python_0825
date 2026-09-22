import requests
from bs4 import BeautifulSoup

url="https://www.melon.com/chart/index.htm"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res=requests.get(url,headers=headers)
res.raise_for_status()  #에러시 종료

soup=BeautifulSoup(res.text,'lxml')
print("-"*50)

s_tbody=soup.tbody
trs=s_tbody.find_all("tr",{"class":"lst50"})

for i in range(50):
    tds = trs[i].find_all("td") #50위 까지 td찾기
    inputs = tds[0].find("input")['title']  #50위까지 제목 찾기
    s_a = tds[6].find("a").get_text()   #50위까지 앨범명
    rank= tds[1].find('span',{'class':'rank'}).get_text()   #순위찾기   #클래스 안에 것 찾을 때 {} 사용
    cover= tds[3].find('img')['src']    #사진찾기
    print(f"{i+1} :{rank}, {inputs}, {s_a},{cover}") # 1위 정보  ####속성값,글씨 전부 들고 오기:.attrs