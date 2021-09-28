import selenium,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "G:/chromedriver/chromedriver.exe"
driver =webdriver.Chrome(PATH)
#ctrl+/ 快樹註解
driver.get("https://www.dcard.tw/f")#去哪個網站
print(driver.title)
search  =   driver.find_element_by_name("query")
search.clear()#清文字
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)#enter鍵
WebDriverWait(driver, 20).until(#網頁跳轉需要時間 等20秒或 (By.CLASS_NAME, "sc-3yr054-1")出現
    EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1"))
)

titles=driver.find_elements_by_class_name("tgn9uw-3")
link=driver.find_element_by_link_text("區塊鏈相關 Podcast 大推薦，分享給願意增進加密貨幣、NFT、Defi 等相關知識的各位")
link.click()
driver.back()#上一頁
driver.back()#
driver.forward()#下一頁



for title in titles:
    print(title.text)#印標題




time.sleep(5)
driver.quit