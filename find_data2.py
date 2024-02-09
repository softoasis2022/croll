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

driver = webdriver.Chrome()
'''
def scroll():
    #1 페이지 라면 스크롤 끝까지 내림

    # 스크롤하기 전의 높이
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 페이지 끝까지 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 페이지 로딩을 기다림
        time.sleep(5)

        # 스크롤 후의 높이를 계산하여 이전 높이와 비교
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("스크롤 완료")
'''


#data = {} #크롤 데이터 초기화

data = {}

 #상단 추가 광고 링크 유형
'''
제품 이름 div테그 class=adProduct_title__amInq
금액 div 테그 class=adProduct_price_area__yA7Ad
카데 고리 div 테그 class=adProduct_depth__s_IUT
제품 상테 및 미리보기 정보 div 테그 class=adProduct_desc__uKoBP adProduct_max__nqViL
리뷰 수, 구매 건수, 등록일, 찜하기 수 div 테그 class=adProduct_etc_box__UJJ90
'''

#상단 추가 광고 링크 없는 유형
'''
제품 이름 div테그 class=product_title__Mmw2K
금액 div 테그 class=product_price_area__eTg7I
카데 고리 div 테그 class=product_depth__I4SqY
제품 상테 및 미리보기 정보 div 테그 class=product_desc__m2mVJ product_max__a2TYt
리뷰 수, 구매 건수, 등록일, 찜하기 수 div 테그 class=product_etc_box__ElfVA
'''

'''
for pagenumber in range(5):
    url = "https://search.shopping.naver.com/search/all?"
    search_kw = "query=" + "원두"
    search_page = "pagingIndex=" + str(pagenumber+1)
    searchurl = url + search_kw +"&"+ search_page
    
    driver.get(searchurl)
    # 검색 완료한 상테
    scroll() #매 페이지 마다 스크롤을 해준다
    time.sleep(3)
    html = requests.get(driver.current_url)
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    find_space = soup.find("div","basicList_list_basis__uNBZx")
    find_div = bs4.BeautifulSoup(str(find_space),'html.parser')

   

    for info_space1 in find_div.find_all("div","adProduct_item__1zC9h"):
        find_info_croll_start1 = bs4.BeautifulSoup(str(info_space1),'html.parser')
        company_mane = find_info_croll_start1.find("div","adProduct_mall_area__H952t").find("div","adProduct_mall_title__kk0Tr").find("a","adProduct_mall__zeLIC linkAnchor").text
        product_name = find_info_croll_start1.find("div","adProduct_title__amInq").find("a","adProduct_link__NYTV9").text
        print(company_mane + " + " + product_name)
    
    
    for info_space2 in find_div.find_all("div","product_item__MDtDF"):
        find_info_croll_start2 = bs4.BeautifulSoup(str(info_space2),'html.parser')
        company_mane = find_info_croll_start2.find("div","product_mall_area___f3wo").find("div","product_mall_title__Xer1m").find("a","product_mall__hPiEH linkAnchor").text
        product_name = find_info_croll_start2.find("div","product_title__Mmw2K").find("a","product_link__TrAac linkAnchor").text
        print(company_mane + " + " + product_name)
'''


# 데이터 프레임 생성
df = pd.DataFrame(data)
# 엑셀 파일로 저장
filename = "coffeemania/min/제품목록.xlsx"
df.to_excel(filename, index=False, engine='openpyxl')
print(f"{filename}에 데이터가 저장되었습니다.")