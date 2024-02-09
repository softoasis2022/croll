'''

네이버쇼핑에서 리스트로 보기 1번 데이터 파이보다 더 많은 정보 확보 가능

'''


import time
import requests


import chromedriver_autoinstaller
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

from selenium import webdriver 
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import warnings
import pandas as pd

def scroll():
    #1 페이지 라면 스크롤 끝까지 내림

    # 스크롤하기 전의 높이
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 페이지 끝까지 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 페이지 로딩을 기다림
        time.sleep(3)

        # 스크롤 후의 높이를 계산하여 이전 높이와 비교
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("스크롤 완료")






for pagenumber in range(1000):
    url = "https://search.shopping.naver.com/search/all?"
    search_kw = "query=" + "원두"
    search_page = "pagingIndex=" + str(pagenumber+1)
    searchurl = url + search_kw +"&"+ search_page
    driver = webdriver.Chrome()
    driver.get(searchurl)
    # 검색 완료한 상테
    scroll() #매 페이지 마다 스크롤을 해준다
    time.sleep(3)


'''


#검색데이터 초기화 : 제품이름, 가격, 배송비, 
data = {}

#검색창 초기화

#검색버튼 클릭

html = requests.get(driver.current_url)
soup = bs4.BeautifulSoup(html.text,'html.parser')
'''





'''
# 예제 데이터
data = {
    "판매회사": ["회사1", "회사2", "회사3"],
    "제품이름": ["제품A", "제품B", "제품C"],
    "용량": ["100ml", "200ml", "300ml"],
    "가격": [10000, 20000, 30000],
    "배송비": [2500, 3000, 0],
    "링크": ["http://link1.com", "http://link2.com", "http://link3.com"]
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
filename = "/mnt/data/제품목록.xlsx"
df.to_excel(filename, index=False, engine='openpyxl')

print(f"{filename}에 데이터가 저장되었습니다.")
'''