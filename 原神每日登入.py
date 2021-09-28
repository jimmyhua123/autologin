import selenium,time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "G:/chromedriver/chromedriver.exe"
driver =webdriver.Chrome(PATH)
#ctrl+/ 快樹註解
driver.get("https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=zh-tw")
actions =ActionChains(driver)
#先隨便點圖片 等登入跳出來
c1=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div/img')
actions.click(c1)
time.sleep(5)
actions.perform()
#再輸入帳密 
accunt=driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div[1]/div/input')
password=driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div[2]/div/input')
accunt.clear()
actions.send_keys_to_element(accunt,"jimmy0624062461@gmail.com")
actions.send_keys_to_element(password,"madhead345")
button=driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div[3]/button')
actions.click(button)
actions.perform()
#有智慧驗證笑死
time.sleep(5)
driver.quit