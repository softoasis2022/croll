from modules.croll import start_croll
from modules.Networkcheck import check_network_status
from modules.Systemroadcheck import check_system_status

import json



#문제
#파이캐쉬 생기는 문제 해결
#

#1. 사이트 찾기 site.json 를 찾고 사이트 정보 가지고 오기, json 안에 리스트 형태로 있으니 참고
#2. 사이트 종류를 리스트로 저장
#3. 

def systemcheck():
    #네트워크 체크
    check_network_status()

    #시스템 사양 체크
    check_system_status()

    #시작 시간 체크
    
    return

def startsetup():
    site = read_file(rogic["site"])
    for i in site["site"]:
        site_url = site[i]["url"]
        site_tag = site[i]["tag"]
        search_keyword = read_file(rogic["keyword"])
        start_croll(site_url,json.dumps(site_tag),i,search_keyword[i])
    

def read_file(ref):
    with open(ref, 'r',encoding='utf-8') as file:  # 'r'은 읽기 모드
        site_list = json.load(file)
    return site_list

rogic = read_file("croll_base/rogic.json")
#print(rogic)
site_url = ""


systemcheck()
#startsetup()