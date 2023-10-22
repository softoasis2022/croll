import socket

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from datetime import datetime
import random
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import bs4
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Selenium 웹 드라이버를 초기화
driver = webdriver.Chrome()  # Chrome 드라이버를 사용하려면 Chrome이 설치되어 있어야 합니다.
driver.get("https://map.naver.com/p/search/인스타카페?c=13.00,0,0,0,dh")

time.sleep(1) #네이버 웹플레이스 에서는페이지가 로드되고 정보를 받아오는 형식이기 때문에 대기 시간이 필요 하다 / 디바이스인터넷 속도가 다르므로 디바이스 속도를 판단하여 재 구성 해야 한다

# "searchIframe" iframe을 찾기
iframe = driver.find_element(By.ID,"searchIframe")

# iframe 내부로 전환
driver.switch_to.frame(iframe)

# iframe 내부의 HTML을 가져오기
html = driver.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, "html.parser")
for i in soup.find_all("li"):
    soup = bs4.BeautifulSoup(str(i),'html.parser')
    print(soup)
# "searchIframe" 섹션의 HTML 정보 출력
#print(soup.prettify())

# Selenium 웹 드라이버 종료
driver.quit()