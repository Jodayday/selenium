from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import urllib
import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

driver = webdriver.Chrome()
days = ["mon","tue","wed","thn","fri","sat","sun","dailyPlus","new"]
wait_driver = WebDriverWait(driver, 30)

for day in days:
    url = f"https://comic.naver.com/webtoon?tab={day}"
    createDirectory(f"/img/{day}")

    driver.get(url)

    li_list = wait_driver.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"item")))


    for li in li_list:
        tar_name, tar_author, *_ = li.text.split("\n")
        tar_link = li.find_element(By.TAG_NAME,'a').get_attribute('href')
        tar_src = li.find_element(By.TAG_NAME,'img').get_attribute('src') 
        urllib.urlretrieve(tar_src, f"img/{day}/{tar_name}.jpg")

        with open('webtoon.csv','w') as f:
            f.write(s)

