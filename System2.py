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
            print(soup["href"])

            #보안 완전체가 아닌 링크는 전환 해서 사용 예시) 인플루언서,뉴스,쇼핑 / 사용하지 않는 링크는 아래에 주석 처리
            if (soup.text == '지도'):
                mapsearch(soup["href"])
            '''
            elif (soup.text == '인플루언서'):
                url = "https://search.naver.com/search.naver"+ soup["href"]
                print(url)
                influencer(url)
            elif(soup.text == 'VIEW'):
                print("https://search.naver.com/search.naver" + soup["href"] )
            else :
                print("전환 하지 않은 링크"+soup["href"])
            elif (soup.text == '뉴스'):
                url = "https://search.naver.com/search.naver" + soup["href"]
                print(url)
            elif (soup.text == '어학사전'):
                print(soup["href"])
            elif (soup.text == '도서'):
                print(soup["href"])
            elif (soup.text == '쇼핑'):
                print("https://search.shopping.naver.com/search/all" +soup["href"])
            '''
            

def plusKw(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text,'html.parser')
    for i in soup.find_all("section","sc_new sp_related"):
        soup = bs4.BeautifulSoup(str(i),'html.parser')
        for j in soup.find_all("div","tit"):
            soup = bs4.BeautifulSoup(str(j),'html.parser')
            f2.append(soup.text)
    print(f2)
def mapsearch(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(url)
    store = []
    time.sleep(7) #네이버 웹플레이스 에서는페이지가 로드되고 정보를 받아오는 형식이기 때문에 대기 시간이 필요 하다 / 디바이스인터넷 속도가 다르므로 디바이스 속도를 판단하여 재 구성 해야 한다
    # "searchIframe" iframe을 찾기
    iframe = driver.find_element(By.ID,"searchIframe")
    # iframe 내부로 전환
    driver.switch_to.frame(iframe)
    # iframe 내부의 HTML을 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    for store_space in soup.find_all("div","Ryr1F"):
        soup = BeautifulSoup(str(store_space), "html.parser")
        for store_info_space in soup.find_all("li","VLTHu OW9LQ"):
            soup = BeautifulSoup(str(store_info_space), "html.parser")
            for store_info_sellect in soup.find_all("div","place_bluelink C6RjW"):
                soup = BeautifulSoup(str(store_info_sellect), "html.parser")
                store.append(soup.find("span","YwYLL").text)
    store_search(store)
    '''
    1. 메뉴 이름 , 참고 사진 (네이버 사진 다운, n개 이상에 합쳐진 메뉴이름에서 마지막 이름을 메뉴 메인 이름으로 선정)
    2. 1번을 제외한 앞 단어들은 서브 이름으로 선정
    3. 
    '''
            
    #https://pcmap.place.naver.com/place/1614953667/bookingDeliveryItem?from=map&fromPanelNum=1&x=127.0398016&y=37.5267821&timestamp=202311081917
    #place_section no_margin
def store_search(store):
    driver = webdriver.Chrome()
    for search_store in store:
        print("스토어 이름 : "+search_store)
        menu = []
        driver.get('https://www.naver.com')
        query = driver.find_element(By.ID,'query')
        #검색창 초기화
        query.clear()
        query.send_keys(search_store)
        #검색버튼 클릭
        driver.find_element(By.CLASS_NAME,"btn_search").click()
        time.sleep(3)
        html = requests.get(driver.current_url)
        soup = bs4.BeautifulSoup(html.text,'html.parser')
        for sc1 in soup.find_all("section","sc_new"):
            soup_sc1 = bs4.BeautifulSoup(str(sc1),'html.parser')
            for find_address in soup_sc1.find_all("span","LDgIH"):
                soup_find_address= bs4.BeautifulSoup(str(find_address),'html.parser')
                address = soup_find_address.find("span").text
            for find_menu in soup_sc1.find_all("div","Cycl8"):
                soup_find_menu= bs4.BeautifulSoup(str(find_menu),'html.parser')
                print(soup_find_menu)
            '''
            if soup.find("span").text == search_store:
                for store_info in soup_storeinfo.find_all("div","place_section no_margin"):
                    soup = bs4.BeautifulSoup(str(store_info),'html.parser')
                    for find_info in soup.find_all("span","LDgIH"):
                        soup = bs4.BeautifulSoup(str(find_info),'html.parser')
                        print("주소 : "+soup.find("span").text)
                        store_address.append(soup.find("span").text)
                        address = soup.find("span").text
            '''
            '''
            for menu in soup_storeinfo:
                menusc1 = bs4.BeautifulSoup(str(menu),'html.parser')
                for menulistspace in menusc1.find_all("div","place_section no_margin yX5qs"):
                    soup = bs4.BeautifulSoup(str(menulistspace),'html.parser')
                    for menuurl in soup.find_all("ul","Pi3tE"):
                        soup = bs4.BeautifulSoup(str(menuurl),'html.parser')
                        for menulist in soup.find_all("li"):
                            soup = bs4.BeautifulSoup(str(menulist),'html.parser')
                            for menuname in soup.find_all("span","VQvNX"):
                                soup = bs4.BeautifulSoup(str(menuname),'html.parser')
                                menu.append(soup.text)
                                print(soup.text)
            '''
        FB_storeinfo("스토어",search_store,address,menu)
                        

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
                FB_crollsearch("인플루언서",infl)

def FB_crollsearch(state,info):
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

def FB_storeinfo(datastate,storename,address,data):
    firebaseref = db.reference('main') #서버 컨트롤 onoff코드
    if datastate == "스토어":
        firebaseref.child(datastate).child(storename).child("주소").set(address)
        for menu in data:
            firebaseref.child(datastate).child(storename).child("메뉴").set(menu)


f1= ['인스타카페']
f2 = []


ipaddress=socket.gethostbyname(socket.gethostname())
while((f1 != None) and (socket.gethostbyname(socket.gethostname()) != '')):
    
    for input_kw in f1:
        #roll_naver_surchkw_view_model(input_kw)
        System(input_kw)
    f1.clear()
    f1=f2

    