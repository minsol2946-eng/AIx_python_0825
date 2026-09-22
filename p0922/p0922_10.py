##selenium:자동화 프로그램->pip install selenium / python -m pip install selenium
#윈도우 크롬 브라우저 기본 설정
#크롬-도움말-설정-https://googlechromelabs.github.io/chrome-for-testing/-크롬드라이버윈도우64

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup
import time
import os


#브라우저열기
browser=webdriver.Chrome()
url="http://www.naver.com"

#1. naver열림
browser.get(url)

#브라우저의 위치값을 찾아서 클릭하기
elem = browser.find_element(By.ID,'query')
elem.click()
#뉴스페이지 이동
elem.send_keys("뉴스")
elem.send_keys(Keys.ENTER)
time.sleep(3)
#네이버 뉴스페이지 이동
elem2=browser.find_element(By.CLASS_NAME,'sds-coms-text')
elem2.click()

input()