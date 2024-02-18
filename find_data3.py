
import json
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
import os

driver = webdriver.Chrome()



def sanitize_path(path):
    illegal_chars = ['.', '#', '$', '[', ']', '/', ':', '\\', '*', '?', '"', '<', '>', '|']
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

def data_pass(data):
    data_save2(data)

def data_save(data):
    with open('D:/data.json', 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=6)  # 읽기 쉽게 포맷팅

def data_save2(data):
    # 폴더 및 파일 이름에서 유효하지 않은 문자 제거
    sanitized_platform = sanitize_path(data['platform'])
    sanitized_store_name = sanitize_path(data['store_name'])
    sanitized_product_name = sanitize_path(data['product_name'])

    # 안전한 경로 구성
    folder_path = os.path.join('D:/coffeemania', sanitized_platform, sanitized_store_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 파일 경로 설정
    file_path = os.path.join(folder_path, sanitized_product_name + '.json')

    # 파일 쓰기
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=6)

def find_rogics():
    for pagenumber in range(1000):
        print(str(pagenumber+1) + "페이지")
        url = "https://search.shopping.naver.com/search/all?"
        search_query = "query="
        kw= "원두"
        search_page = "pagingIndex=" + str(pagenumber+1)
        searchurl = url + search_query +kw+"&"+ search_page
        driver.get(searchurl)
        # 검색 완료한 상테
        scroll() #매 페이지 마다 스크롤을 해준다

        soup = bs4.BeautifulSoup(driver.page_source,'html.parser')
        find_space = soup.find("div","basicList_list_basis__uNBZx")
        find_div1 = bs4.BeautifulSoup(str(find_space),'html.parser')
        find_div2 = bs4.BeautifulSoup(str(find_space),'html.parser')

        for info_space1 in find_div1.find_all("div","adProduct_item__1zC9h"): #광고 스페이스 
            find_info_croll_start1 = bs4.BeautifulSoup(str(info_space1),'html.parser')
            
            company_name = find_info_croll_start1.find("div","adProduct_mall_area__H952t").find("div","adProduct_mall_title__kk0Tr").find("a","adProduct_mall__zeLIC linkAnchor")
            product_name = find_info_croll_start1.find("div","adProduct_title__amInq").find("a","adProduct_link__NYTV9")
            price_name = find_info_croll_start1.find("div","adProduct_price_area__yA7Ad").find("span","price_num__S2p_v").find("em")
            delivery_name = find_info_croll_start1.find("div","adProduct_price_area__yA7Ad").find("span","price_delivery__yw_We")
            link_name = find_info_croll_start1.find("div", "adProduct_info_area__dTSZf").find("a")

            soup_company_name = bs4.BeautifulSoup(str(company_name),'html.parser')
            soup_product_name = bs4.BeautifulSoup(str(product_name),'html.parser')
            soup_price_name = bs4.BeautifulSoup(str(price_name),'html.parser')
            soup_delivery_name = bs4.BeautifulSoup(str(delivery_name),'html.parser')

            price = int(str(soup_price_name.text).replace("원" , "").replace(",", ""))
            
            if(soup_delivery_name.text == "배송비무료"):
                deliveryprice = str(soup_delivery_name.text).replace("배송비","")
            else :
                deliveryprice =int(str(soup_delivery_name.text).replace("배송비","").replace("원","").replace(",",""))
            data = {
                'platform': "네이버",
                'store_name': soup_company_name.text,
                'product_name': soup_product_name.text,
                'price': price,
                'delivery_price': deliveryprice,
                'link': str(link_name['href'])
            }
            data_pass(data)
        for info_space2 in find_div2.find_all("div","product_item__MDtDF"):
            find_info_croll_start2 = bs4.BeautifulSoup(str(info_space2),'html.parser')
            
            company_name = find_info_croll_start2.find("div","product_mall_area___f3wo").find("div","product_mall_title__Xer1m").find("a","product_mall__hPiEH linkAnchor")
            product_name = find_info_croll_start2.find("div","product_title__Mmw2K").find("a","product_link__TrAac linkAnchor")
            price_name = find_info_croll_start2.find("div","product_price_area__eTg7I").find("span","price_num__S2p_v").find("em")
            delivery_name = find_info_croll_start2.find("div","product_price_area__eTg7I").find("span","price_delivery__yw_We")
            link_name = find_info_croll_start2.find("div","product_title__Mmw2K").find("a")

            soup_company_name = bs4.BeautifulSoup(str(company_name),'html.parser')
            soup_product_name = bs4.BeautifulSoup(str(product_name),'html.parser')
            soup_price_name = bs4.BeautifulSoup(str(price_name),'html.parser')
            soup_delivery_name = bs4.BeautifulSoup(str(delivery_name),'html.parser')

            price = int(str(soup_price_name.text).replace("원" , "").replace(",", ""))

            if(soup_delivery_name.text == "배송비무료"):
                deliveryprice = str(soup_delivery_name.text).replace("배송비","")
            else :
                if "포함" in soup_delivery_name.text :
                    price = price - int(str(soup_delivery_name.text).replace("배송비","").replace("포함","").replace("원","").replace(",", ""))
                    deliveryprice = int(str(soup_delivery_name.text).replace("배송비","").replace("포함","").replace("원","").replace(",", ""))
                else : 
                    deliveryprice = int(str(soup_delivery_name.text).replace("배송비","").replace("원","").replace(",",""))
            data = {
                'platform': "네이버",
                'store_name': soup_company_name.text,
                'product_name': soup_product_name.text,
                'price': price,
                'delivery_price': deliveryprice,
                'link': str(link_name['href'])
            }
            data_pass(data)

find_rogics()