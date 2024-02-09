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
driver.get('https://www.instagram.com/explore/search/keyword/?q=%EC%B9%B4%ED%8E%98')
time.sleep(30)
html = requests.get(driver.current_url)
soup = bs4.BeautifulSoup(html.text,'html.parser')
print(soup)
