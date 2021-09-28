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
driver.get("https:/www.google.com")
actions =ActionChains(driver)

id = driver.find_element_by_name('q')
actions.send_keys_to_element(id,"jimmy0624062461@gmail.com")
actions.perform()




time.sleep(5)
driver.quit