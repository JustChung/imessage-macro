from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
print(driver.title)
time.sleep(3)
en_lang_elem = driver.find_element(By.ID, "langSelect-EN")
en_lang_elem.click()
time.sleep(3)
cookie_elm = driver.find_element(By.ID, "bigCookie")
cookie_elm.click()
time.sleep(15)
driver.close()
