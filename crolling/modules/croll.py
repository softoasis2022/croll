import json
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
from openpyxl import load_workbook
import os

## 동경 124도와 132도 사이, 북위 33도와 44 도 사이에 위치



driver = webdriver.Edge()



def start_croll(site_url,site_tag,i,ref_search_keyword):
    print(site_url,site_tag,i,ref_search_keyword) #https://map.naver.com/p/search/ [{'iframe': 'searchIframe'}] naver {'keywordlist': ['nomal', 'special'], 'keyword': {'nomal': ['커피', '카페'], 'special': ['맛집']}}
    keywordvalue = get_keyword(ref_search_keyword)
    page_open(site_url,keywordvalue)
    page_findlayout(site_url,ref_search_keyword,site_tag)
    driver.quit()

def get_keyword(ref_search_keyword):
    keywordlist = ref_search_keyword["keywordlist"]
    for keyword in keywordlist:
        #print(search_keyword["keyword"][keyword])
        for keywordvalue in ref_search_keyword["keyword"][keyword]:
            #print(keywordvalue)
            print(keywordvalue)
            return keywordvalue



def page_open(site_url,keywordvalue):
    #print(keywordvalue)
    driver.get(site_url+keywordvalue)
    
            
            

def page_findlayout(site_url,ref_search_keyword,site_tag):
    print(json.loads(site_tag))
    changedjson = json.loads(site_tag)
    tagsize = list(dict(changedjson).keys())
    for tag_find_action in tagsize:
        #테그가 iframeㅇ릴떄
        if tag_find_action == "iframe":
            
            #테그 아이디 불러오기
            tagid = dict(changedjson)[tag_find_action]
            
            iframe_content = iframe_find(driver, timeout=15)
            if iframe_content:
                print("크롤링 성공! 일부 내용:", iframe_content[:500])
            else:
                print("크롤링 실패")

def iframe_find(driver, timeout=20):
    """
    특정 페이지에서 iframe 로드를 대기하고, id가 'searchIframe'인 iframe 내부 콘텐츠를 크롤링하는 함수.
    
    Args:
        driver (webdriver): Selenium WebDriver 객체
        timeout (int): iframe 로드 대기 시간(초)
    
    Returns:
        str: iframe 내부의 HTML 콘텐츠
    """
    try:
        # 'id'가 'searchIframe'인 iframe을 찾기
        iframe = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, "searchIframe"))
        )
        print("iframe 로드 완료!")

        # 해당 iframe으로 전환
        driver.switch_to.frame(iframe)
        time.sleep(3)  # 잠시 대기하여 동적 콘텐츠가 로드될 시간 제공

        # 동적 콘텐츠가 로드되었는지 확인
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='some-class']"))  # 실제 요소로 대체
        )

        # iframe 내부 HTML 콘텐츠 가져오기
        content = driver.content
        driver.switch_to.default_content()  # 다시 메인 페이지로 전환
        
        return content

    except Exception as e:
        print("iframe 로드 실패 또는 시간 초과:", e)
        return None
