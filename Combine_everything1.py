""" 1번째 파일 """

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

""" cmd에서 cd C:\Program Files (x86)\Google\Chrome\Application\ 입력 후
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/Chrome_debug_temp" 
입력하면 포트가 9222 인 크롬창 나타남 """

# 포트 9222의 크롬을 크롬드라이버에 적용
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Users/손병우/Desktop/coding/02_selenium/chromedriver"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
action = ActionChains(driver)

##############################
action.key_down(Keys.TAB).key_down(Keys.ENTER).perform()
###############################

# iframe 이 있는 경우와 없는 경우로 진행
iframes = driver.find_elements_by_tag_name('iframe')
if len(iframes) == 0:
    page = 2
    next_btn1 = driver.find_element_by_xpath('//*[@name="redNextBtn"]')
    next_btn1.click()
    time.sleep(1)
else:
    driver.switch_to.frame("ifr")
    next_btn1 = driver.find_element_by_xpath('//*[@name="redNextBtn"]')
    next_btn1.click()
    time.sleep(1)
    page=3

# 5페이지 까지 알아서 돌림

while page < 5: 
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