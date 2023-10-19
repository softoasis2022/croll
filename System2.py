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


cred = credentials.Certificate('softoasis-763c2-firebase-adminsdk-lhap2-28da23a1b3.json')

firebase_admin.initialize_app(cred,{
'databaseURL' : 'https://softoasis-763c2-default-rtdb.firebaseio.com/'
#'databaseURL' : '데이터 베이스 url'
})


def System(kwString):
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
    plusKw(driver.current_url)
    soup = soup.find("div","type_animation lnb_intent")
    for i in soup.find_all("div","lnb_group"):
        html = str(i)
        soup = bs4.BeautifulSoup(html,'html.parser')
        for j in soup.find_all("div","flick_bx"):
            soup = bs4.BeautifulSoup(str(j),'html.parser')
            soup = soup.find("a")
            print(soup.text)
            if (soup['href'][0]== '?'):
                url = "https://search.naver.com/search.naver" + soup['href']
                print("url : " + url)
                if soup.text == '인플루언서':
                    influencer(url)
            else :
                print(soup['href'])

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
                        firebase2('키워드',htmlkw.text)
    except:
        print("d")
                
def influencer(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    for influencer_page in soup.find_all("div","api_subject_bx"):
        soup = bs4.BeautifulSoup(str(influencer_page),'html.parser')
        for li_influencer_page in soup.find_all("li"):
            soup = bs4.BeautifulSoup(str(li_influencer_page),'html.parser')
            for influencer_name in soup.find_all("div","user_info_bx"):
                soup = bs4.BeautifulSoup(str(influencer_name),'html.parser')
                infl = []
                for influencer_info in soup.find_all("span"):
                    soup = bs4.BeautifulSoup(str(influencer_info),'html.parser')
                    infl.append(soup.text)
                firebase2("인플루언서",infl)

def firebase2(state,info):
    firebaseref = db.reference('main') #서버 컨트롤 onoff코드
    if(state == '인플루언서'):
        now = "2023-10-19"
        print(info)
        firebaseref.child("인플루언서").child(info[0]).child("이름").set(info[0])
        firebaseref.child("인플루언서").child(info[0]).child("블로거").set(info[1])
        firebaseref.child("인플루언서").child(info[0]).child("전문").set(info[2])
        fan = now + " 기준 " + info[len(info)-1]
        firebaseref.child("인플루언서").child(info[0]).child("팬").set(fan)
    else:
        print("데이터가 없습니다")


f1= ['인스타카페']
f2 = []


ipaddress=socket.gethostbyname(socket.gethostname())
while((f1 != None) and (socket.gethostbyname(socket.gethostname()) != '')):
    
    for input_kw in f1:
        #roll_naver_surchkw_view_model(input_kw)
        System(input_kw)
    f1=f2
    