import requests #웹 접근할 수 있음-pip install reqest:설치

from bs4 import BeautifulSoup #html로 파싱

# url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# url="http://www.melon.com/chart/index.htm"
url="http://www.naver.com"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res=requests.get(url,headers=headers)
res.raise_for_status()  #에러시 종료
# print(res.status_code)  #상태 코드

print(res.text)

# with open("stu.txt",'w',encoding='utf-8') as f:
# f=open("stu.txt",'w',encoding='utf-8')
# f.clse()


#텍스트 형태로 저장
with open("naver1.html",'w',encoding='utf-8') as f:
    f.write(res.text)
print("저장")