""" 2번째 파일"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Users/손병우/Desktop/coding/02_selenium/chromedriver"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
action = ActionChains(driver)

# page=5 설정
page=5

# 총 page 분석 후 몇번 돌릴지 변수에 저장
page_txt=driver.find_element_by_xpath('//*[@id="controller"]/div[4]/ul/li[2]/p').text
split = page_txt.split()       # 공백 기준으로 나눔
cycle_time=int(split[2])-1   # (마지막 페이지-1)

# 사전문제에서 next 버튼 눌러주기
next_btn1 = driver.find_element_by_xpath('//*[@name="redNextBtn"]')
next_btn1.click()
time.sleep(1)

while page < cycle_time:
    # 음소거 만들기
    audio = driver.find_element_by_xpath('//*[@id="soundOnOffImage"]')
    audio.click()

    # sliderbar의 max time 추출 (maxtime = sleeptime)
    max = driver.find_element_by_id('sliderbar')
    sleeptime = int(max.get_attribute("max"))
    time.sleep(sleeptime+1)

    # 클릭지점 클릭 후 sleep 1초
    next_btn1 = driver.find_element_by_xpath('//*[@name="redNextBtn"]')
    next_btn1.click()
    time.sleep(1)
    
    # page 플러스
    page+=1

""" 유튜브로 음악 재생 """
# 새창에서 유튜브
driver.execute_script('window.open("https://www.youtube.com/");')
driver.switch_to.window(driver.window_handles[-1])
time.sleep(1)

# 검색 후 클릭
search = driver.find_element_by_xpath('//*[@name="search_query"]')
search.send_keys('네가없는밤')
time.sleep(1)

search.submit()
time.sleep(1)

music = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
music.click()
