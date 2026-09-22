import requests
from bs4 import BeautifulSoup

# url="https://n.news.naver.com/article/094/0000013820?cds=news_media_pc&type=editn"
url="https://www.melon.com/chart/index.htm"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res=requests.get(url,headers=headers)
res.raise_for_status()  #에러시 종료


#파일 전체 저장: res.text
#▼ 부분 지정 저장: 파싱 후 원하는 부분 저장 ▼

soup=BeautifulSoup(res.text,'lxml') #html소스로 변셩->css 코드로 사용할 수 있는 문법으로 변경

print("-"*50)
# print("a태그: ",soup.a)
# print("a태그: ",soup.a['href']) # 속성 한개만 지정.
# print("a태그: ",soup.a.attrs) #a태그의 모든 속성잢을 가져온다.
# print("title 제목: ",soup.title)    #슾에서 타이틀 찾아줌
# print("title 제목: ",soup.title.get_text())

# print(soup.prettify()) # 코드가 정렬돼 저장.
# print(res.text)


#태그로 찾는 방법, 속성1개 찾는 방법, 속성 모두 찾는 방법.
# print(soup.title) #태그 가져오기
# print(soup.title.get_text())  #태그 텍스트
# print(soup.div.attrs) #속성값 모두
# print(soup.tbody)

#페이지-> f12 -> ctrl+u :전체페이지로 소스 보기


#ID와 clss 로 찾는 방법
# print(soup.find("div",{'id':"header"}))
# print(soup.find("div",{'id':"util_menu"}))
# print(soup.find("tr",{'clss':"lst50"}))
print(soup.find("tr",{'clss':"input_check d_checkall"['title']}))