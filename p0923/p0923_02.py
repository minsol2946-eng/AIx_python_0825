from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}

# # browser = webdriver.Chrome()
# # url = "https://comic.naver.com/bestChallenge?sortType=starscore"

# # browser.get(url)
# # time.sleep(4)

# # soup = BeautifulSoup(browser.page_source,'lxml')
# # with open('weptoon.html','w',encoding='utf-8') as f:
# #     f.write(soup.prettify())


# with open('weptoon.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')



# UL=soup.find('ul',{'class':'BestChallengeView__challenge_list--sUqhh'})
# LIS=UL.find_all('li')

# # print(IMG)

# # # 이미지
# # IMG = LIS[i].find('img')['src']
# # print(IMG)
# # # 이미지 저장
# # IMG_res = requests.get(IMG,headers=headers)
# # os.makedirs('./p0923/webtoon',exist_ok=True) # 폴더생성
# # with open(f'p0923/webtoon/w_{i}.jpg','wb') as f:
# #     f.write(IMG_res.content)
# # print("-"*50)



# for i in range(3):
#     IMG_res = requests.get(IMG,headers=headers)
#     os.makedirs('./p0923/webtoon',exist_ok=True) # 폴더생성
#     with open(f'p0923/webtoon/w_{i}.jpg','wb') as f:
#         f.write(IMG_res.content)
#     print("-"*50)


#     IMG=LIS[0].find('img')['src']
#     TITLE=LIS[0].find('span',{'class':'ContentTitle__title--e3qXt'}).get_text(strip=True)
#     WRITER=LIS[0].find('a',{'class':'ContentAuthor__author--CTAAP'}).get_text(strip=True)
#     STAR=LIS[0].find('span',{'class':'Rating__star_area--dFzsb'}).get_text(strip=True)
#     VIEW=LIS[0].find('span',{'class':'Rating__view_area--GQb_S'}).get_text(strip=True)
#     print()






# # print(TITLE)
# # print(WRITER)
# # print(STAR)
# # print(VIEW)

# # img_res=requests.get()

#----------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import os

# 이미지 요청할 때 사용할 헤더
headers = {'User-Agent': 'Mozilla/5.0'}

# HTML 파일 열기
with open('weptoon.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')


# 웹툰 목록 가져오기
UL = soup.find('ul', {'class': 'BestChallengeView__challenge_list--sUqhh'})
LIS = UL.find_all('li')

# 이미지 저장 폴더 생성
os.makedirs('./p0923/webtoon', exist_ok=True)



V_Total=0
V_Avg=0

# 3개 가져오기
for i in range(3):
    IMG = LIS[i].find('img')['src']
    TITLE = LIS[i].find('span',{'class': 'ContentTitle__title--e3qXt'}).get_text(strip=True)
    WRITER = LIS[i].find('a',{'class': 'ContentAuthor__author--CTAAP'}).get_text(strip=True)
    STAR = LIS[i].find('span',{'class': 'Rating__star_area--dFzsb'}).get_text(strip=True)
    VIEW = LIS[i].find('span',{'class': 'Rating__view_area--GQb_S'}).get_text(strip=True)
    IMG_res = requests.get(IMG, headers=headers)
    with open(f'./p0923/webtoon/w_{i}.jpg', 'wb') as f:
        f.write(IMG_res.content)


    # 결과 출력
    print("번호 :", i + 1)
    print("제목 :", TITLE)
    print("작가 :", WRITER)
    print("별점 :", STAR)
    print("조회수 :", VIEW)
    print("이미지 :", IMG)
    print("-" * 50)

    V_Total+=VIEW

V_Avg=V_Total/3
print(V_Total)
print(V_Avg)
