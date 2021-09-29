import selenium,time,os,wget
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
driver.get("https://www.instagram.com/")
username=WebDriverWait(driver, 20).until(#網頁跳轉需要時間 等20秒或 (By.CLASS_NAME, "sc-3yr054-1")出現
    EC.presence_of_element_located((By.NAME, "username"))
)
password=WebDriverWait(driver, 20).until(#網頁跳轉需要時間 等20秒或 (By.CLASS_NAME, "sc-3yr054-1")出現
    EC.presence_of_element_located((By.NAME, "password"))
)
username.clear()
password.clear()
print("Enter your account : ")
Your_account=input()
print("Your account : ",Your_account)
print("Enter your passward : ")
Your_password=input()
print("Your passwwrd : ",Your_password[:-3],"xxx")
username.send_keys(str(Your_account))
password.send_keys(str(Your_password))
print("Enter your keyword to download pictures : ")
userkeyword=input()
print("Your keyword : ",userkeyword)
print("Start download  ")

login =driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login.click()
WebDriverWait(driver, 20).until(#網頁跳轉需要時間 等20秒或 (By.CLASS_NAME, "sc-3yr054-1")出現
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)
search=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
keyword=str(userkeyword)
#keyword="inkyung97"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
WebDriverWait(driver, 20).until(#網頁跳轉需要時間 等20秒或 (By.CLASS_NAME, "sc-3yr054-1")出現
    EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD'))
)
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
imgs = driver.find_elements_by_class_name("FFVAD")

path = os.path.join(keyword)

if not os.path.exists(path):
    os.mkdir(path)
else:
    pass
count = 0
for img in imgs:
    save_as = os.path.join(path, keyword + str(count) + '.jpg')
    # print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"), save_as)
    count += 1
print(" Download finished  ")
print(" You can find your pictures in files  ")

