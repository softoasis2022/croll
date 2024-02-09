'''

네이버쇼핑에서 리스트로 보기 1번 데이터 파이보다 더 많은 정보 확보 가능
116페이지 까지 크롤 완료
'''

import time
import requests

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

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
from openpyxl import load_workbook

driver = webdriver.Chrome()
filename = "D:/min/제품목록.xlsx"

cred = credentials.Certificate('softoasis.json')

firebase_admin.initialize_app(cred,{
'databaseURL' : 'https://softoasis-763c2-default-rtdb.firebaseio.com/'
#'databaseURL' : '데이터 베이스 url'
})

def sanitize_path(path):
    illegal_chars = ['.', '#', '$', '[', ']', '/']
    for char in illegal_chars:
        path = path.replace(char, "_")
    return path

def scroll():
    #1 페이지 라면 스크롤 끝까지 내림

    # 스크롤하기 전의 높이
    
    while True:
        # 페이지 끝까지 스크롤
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 페이지 로딩을 기다림
        time.sleep(1)

        # 스크롤 후의 높이를 계산하여 이전 높이와 비교
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("스크롤 완료")
'''
def scroll():
    while True:
        driver.find_elements(By.TAG_NAME,'body')
'''

#data = {} #크롤 데이터 초기화

data = {
    "판매회사": None,
    "제품이름": None,
    "가격": None,
    "배송비": None,
    "링크": None
}

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
page = 1000
none_name = 0
for pagenumber in range(page):
    url = "https://search.shopping.naver.com/search/all?"
    search_query = "query="
    kw= "원두"
    search_page = "pagingIndex=" + str(pagenumber+1)
    searchurl = url + search_query +kw+"&"+ search_page
    driver.get(searchurl)
    # 검색 완료한 상테
    scroll() #매 페이지 마다 스크롤을 해준다

    li_company_mane = []
    li_product_name = []
    li_price_name = []
    li_delivery_name = []
    li_link_name = []
    
    soup = bs4.BeautifulSoup(driver.page_source,'html.parser')
    find_space = soup.find("div","basicList_list_basis__uNBZx")
    find_div1 = bs4.BeautifulSoup(str(find_space),'html.parser')
    find_div2 = bs4.BeautifulSoup(str(find_space),'html.parser')
    for info_space1 in find_div1.find_all("div","adProduct_item__1zC9h"):
        find_info_croll_start1 = bs4.BeautifulSoup(str(info_space1),'html.parser')
        
        company_name = find_info_croll_start1.find("div","adProduct_mall_area__H952t").find("div","adProduct_mall_title__kk0Tr").find("a","adProduct_mall__zeLIC linkAnchor")
        product_name = find_info_croll_start1.find("div","adProduct_title__amInq").find("a","adProduct_link__NYTV9")
        price_name = find_info_croll_start1.find("div","adProduct_price_area__yA7Ad").find("span","price_num__S2p_v").find("em")
        delivery_name = find_info_croll_start1.find("div","adProduct_price_area__yA7Ad").find("span","price_delivery__yw_We")

        soup_company_name = bs4.BeautifulSoup(str(company_name),'html.parser')
        soup_product_name = bs4.BeautifulSoup(str(product_name),'html.parser')
        soup_price_name = bs4.BeautifulSoup(str(price_name),'html.parser')
        soup_delivery_name = bs4.BeautifulSoup(str(delivery_name),'html.parser')

        if soup_company_name.text != None:
            firebaseref = db.reference('coffeemania').child(kw) #서버 컨트롤 onoff코드

            companyname = sanitize_path(soup_company_name.text)
            productname = sanitize_path(soup_product_name.text)

            if companyname != "":
                if companyname != "None":
                    firebaseref.child("브랜드").child(companyname).child(productname).child("가격").set(soup_price_name.text)
                    firebaseref.child("브랜드").child(companyname).child(productname).child("배송비").set(soup_delivery_name.text)
                else :
                    print(productname)
                    none_name= none_name+1
                    firebaseref.child("판매자 알수 없음").push().child(productname).child("가격").set(soup_price_name.text)
                    firebaseref.child("판매자 알수 없음").push().child(productname).child("배송비").set(soup_delivery_name.text)
            else :
                none_name= none_name+1
                productname = sanitize_path(soup_product_name.text)
                print("판매자 알 수 없음 : "+ productname)
                firebaseref.child("판매자 알수 없음").push().child(productname).child("가격").set(soup_price_name.text)
                firebaseref.child("판매자 알수 없음").push().child(productname).child("배송비").set(soup_delivery_name.text)

    for info_space2 in find_div2.find_all("div","product_item__MDtDF"):
        find_info_croll_start2 = bs4.BeautifulSoup(str(info_space2),'html.parser')
        
        company_name = find_info_croll_start2.find("div","product_mall_area___f3wo").find("div","product_mall_title__Xer1m").find("a","product_mall__hPiEH linkAnchor")
        product_name = find_info_croll_start2.find("div","product_title__Mmw2K").find("a","product_link__TrAac linkAnchor")
        price_name = find_info_croll_start2.find("div","product_price_area__eTg7I").find("span","price_num__S2p_v").find("em")
        delivery_name = find_info_croll_start2.find("div","product_price_area__eTg7I").find("spam","price_delivery__yw_We")

        soup_company_name = bs4.BeautifulSoup(str(company_name),'html.parser')
        soup_product_name = bs4.BeautifulSoup(str(product_name),'html.parser')
        soup_price_name = bs4.BeautifulSoup(str(price_name),'html.parser')
        soup_delivery_name = bs4.BeautifulSoup(str(delivery_name),'html.parser')

        if soup_company_name.text != None:
            firebaseref = db.reference('coffeemania').child(kw) #서버 컨트롤 onoff코드

            companyname = sanitize_path(soup_company_name.text)
            productname = sanitize_path(soup_product_name.text)

            if companyname != "":
                if companyname != "None":
                    firebaseref.child("브랜드").child(companyname).child(productname).child("가격").set(soup_price_name.text)
                    firebaseref.child("브랜드").child(companyname).child(productname).child("배송비").set(soup_delivery_name.text)
                else :
                    print(productname)
                    none_name= none_name+1
                    firebaseref.child("판매자 알수 없음").push().child(productname).child("가격").set(soup_price_name.text)
                    firebaseref.child("판매자 알수 없음").push().child(productname).child("배송비").set(soup_delivery_name.text)
            else :
                none_name= none_name+1
                productname = sanitize_path(soup_product_name.text)
                print("판매자 알 수 없음 : "+ productname)
                firebaseref.child("판매자 알수 없음").push().child(productname).child("가격").set(soup_price_name.text)
                firebaseref.child("판매자 알수 없음").push().child(productname).child("배송비").set(soup_delivery_name.text)
            
    print(none_name)
    # 데이터 프레임 생성
    '''
    df = pd.DataFrame(data)
    # 엑셀 파일로 저장
    df.to_excel(filename, index=False, engine='openpyxl')
    print(f"{filename}에 데이터가 저장되었습니다.")
    '''



'''
wb = load_workbook(filename)
    ws = wb.active


'''