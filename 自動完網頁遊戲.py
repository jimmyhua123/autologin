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
driver.get("https://tsj.tw/")
actions =ActionChains(driver)

blow =driver.find_element_by_id("click")
blow_count=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
items =[]
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]/i'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]/i'))
prices=[]
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))

actions.click(blow)

for i in range(1000):
    actions.perform()
    count=(int(blow_count.text.replace("您目前擁有","").replace("技術點","")))
    for j in range(3):
        price=int(prices[j].text.replace("技術點",""))
        if price <= count:
            upgrade_action= ActionChains(driver)
            upgrade_action.move_to_element(items[j])
            upgrade_action.click()
            upgrade_action.perform()
            break

time.sleep(5)
driver.quit