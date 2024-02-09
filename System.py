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


import time
import sys 
import os 

import pandas as pd
import numpy as np

from selenium import webdriver 
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import warnings
warnings.filterwarnings('ignore')
#셀레니움 4버전 적용

cred = credentials.Certificate('softoasis-763c2-firebase-adminsdk-lhap2-28da23a1b3.json')

firebase_admin.initialize_app(cred,{
'databaseURL' : 'https://softoasis-763c2-default-rtdb.firebaseio.com/'
#'databaseURL' : '데이터 베이스 url'
})

def croll_naver_surchkw_view_model(kwString): #str / 뷰 모델 크롤링
    driver = webdriver.Chrome()
    driver.get('https://www.naver.com')

    query = driver.find_element(By.ID,'query')

    #검색창 초기화
    query.clear()
    query.send_keys(kwString)
    #검색버튼 클릭
    driver.find_element(By.CLASS_NAME,"btn_search").click()
    html = requests.get(driver.current_url)
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    #검색 완료
    plusKw(driver.current_url)
    url = []
    urltext = []
    for href1 in soup.find_all("div",class_ = 'api_more_wrap'): # 테그 찾기
        soup1 = bs4.BeautifulSoup(str(href1),'html.parser')
        soup1 = soup1.find("a")
        urlstring = str(soup1['href'])
        if(urlstring[0] != "?" and urlstring[0] != "#"):
            url.append(urlstring)
            urltext.append(soup1.text)
    for i in url:
        sp1 = str(i).split('//')
        if sp1[1][0] == 's':
            searchpage_parse(i)
        if sp1[1][0] == 'm':
            mappagepage_parse(driver.current_url)
    
def plusKw(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    try:
        for href2 in soup.find("section","sc_new sp_nkeyword"):  #관련 키워드 섹션 찾기  #함수화 수정 예정
            page_text = str(href2)
            soup1 =bs4.BeautifulSoup(page_text,'html.parser')
            if(type(soup1) != type(None)):
                for kw in soup1.find_all("a"):
                    space_kw = str(kw)
                    soup2 =bs4.BeautifulSoup(space_kw,'html.parser')
                    htmlkw = soup2.find("div","tit")
                    if(type(htmlkw) != type(None)):
                        f2.append(htmlkw.text)
                        firebase('키워드',htmlkw.text)
                    

    except:
        print("d")

def firebase(state,kw):
    firebaseref = db.reference('main') #서버 컨트롤 onoff코드
    if (state == '키워드'):
        firebaseref.child(state).push().set(kw)
    elif(state == 'blogtext'):
        firebaseref.child(state).push().set(kw)
    elif(state == 'market'):
        '''
        for i in firebaseref.child(state).get():
            if firebaseref.child(state).child(i).get() == kw:
                return
        '''
        firebaseref.child(state).push().set(kw)
    else:
        firebaseref.child('new info').child(state).push().set(kw) # 다른 데이터 일경우 새로 저장
def searchpage_parse(url):
    print('검색 페이지 파싱')
    driver = webdriver.Chrome()
    driver.get(url)
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    space = soup.find("div","keyword_challenge_wrap")
    # 타입 에러 확인 
    try:
        for blog in space.find_all('div','title_area'):
            #space.find_all('div','title_area')
            if (type(space.find_all('div','title_area')) != type(None)):
                html = str(blog)
                soup = bs4.BeautifulSoup(html,'html.parser')
                te = soup.find('a')
                if te.text[0] != '[':
                    firebase('blogtext',te.text)
    except:
        search_in(url)
def mappagepage_parse(url):
    print('맵 페이지 파싱')
    driver = webdriver.Chrome()
    driver.get(url)
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    for i in soup.find_all("section","sc_new b8k1d"):
        soup = bs4.BeautifulSoup(str(i),'html.parser')
        for j in soup.find_all("div","N_KDL"):
            soup = bs4.BeautifulSoup(str(j),'html.parser')
            name = soup.find("span")
            print(name.text)
            firebase('market',name.text)
            
    
    
    
    
def search_in(url):  #지식인 파싱
    print('지식인 페이지 파싱')
    firebase('search_in ',url)
    
    
    #지식인 로직에 따른 파싱
    #1. 전달 받은 링크 로딩
    #2. 질문 링크 
                

                
                
                
                    
    '''
    soup=bs4.BeautifulSoup(href,'html.parser')
    for i in soup.find_all("div","flick_bx"):
        print(str(i))
    '''

#새로운 로직
'''
1. 검새 후 검색버튼 리스트별 페이지 접속
2. 추가 업로드가 없을때까지 스크롤 다운
3. 모든정보 가져 오기


'''

f1= ['인스타카페']
f2 = []


ipaddress=socket.gethostbyname(socket.gethostname())
while((f1 != None) and (socket.gethostbyname(socket.gethostname()) != '')):
    
    for input_kw in f1:
        croll_naver_surchkw_view_model(input_kw)
    f1=f2
    




