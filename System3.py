

import time
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

from selenium import webdriver 
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import warnings


'''
메누 받아오기
스토어 받아오기
이미지 저장 하기
상가 발품 받아오기

'''

driver = webdriver.Chrome()
driver.get('https://www.naver.com')
time.sleep(2)
html = requests.get(driver.current_url)
soup = bs4.BeautifulSoup(html.text,'html.parser')

search_in = soup.find_all("div","search_input_box")
soup = bs4.BeautifulSoup(str(search_in),'html.parser')

query = driver.find_element(By.ID,'query')

query.clear()
query.send_keys("카페")
driver.find_element(By.CLASS_NAME,"btn_search").click()

html = requests.get(driver.current_url)
soup = bs4.BeautifulSoup(html.text,'html.parser')
section_score = 0 
for i in soup.find_all("div","title_wrap"):
    if i != None:
        section_score = section_score + 1
        print(i.text)
        
print("현재 페이지 섹션 갯수는 "+str(section_score)+"개 입니다")

'''
섹션으로 안치는 그룹 : 파워링크, 플레이스, 
섹션에 포함 된 그룹 : 플레이스, 


참고 사항 : 타이틀 문자열은 title_wrap 로 통일이 되어있음 섹션이 아닌 
'''