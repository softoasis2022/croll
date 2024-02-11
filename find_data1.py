'''

네이버 일반검색 창에서 데이터 크롤링

'''


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
import pandas as pd

url = "https://www.naver.com/"

driver = webdriver.Chrome()
driver.get(url)

query = driver.find_element(By.ID,'query')

#검색데이터 초기화 : 제품이름, 가격, 배송비, 
data = {}

#검색창 초기화
query.clear()
query.send_keys("원두")
#검색버튼 클릭
driver.find_element(By.CLASS_NAME,"btn_search").click()
html = requests.get(driver.current_url)
soup = bs4.BeautifulSoup(html.text,'html.parser')
for find_section in soup.find_all("section"):
    soup = bs4.BeautifulSoup(str(find_section),'html.parser')
    check_section = soup.find("h2","title")
    check_section = bs4.BeautifulSoup(str(check_section),'html.parser')
    if check_section.text == "네이버쇼핑":
        find_ul = soup.find_all("ul","list_divide")
        find_ul = bs4.BeautifulSoup(str(find_ul),'html.parser')
        find_li = find_ul.find_all("li")
        print(find_li)

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