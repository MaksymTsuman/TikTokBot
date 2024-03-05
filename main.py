from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from bs4 import BeautifulSoup
import requests

from fake_useragent import UserAgent

class TiktokBot():
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--incognito')
        self.options.add_argument("--start-maximized")
        self.service = Service(executable_path='C:\\Users\\HOME\\Desktop\\Tik tok bot\\chromedriver-win64\\chromedriver.exe')
        self.driver = webdriver.Chrome(options=self.options, service=self.service)

    
    def compleate(self):
        self.driver.close()
        self.driver.quit()


    def login(self):
        driver = self.driver
        try:
            driver.get("https://www.tiktok.com/uk-UA/")
            time.sleep(4)

            go_to_google = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[3]/div/div/div/div[1]/div/div/div[1]/div[3]/div[2]")
            go_to_google.click()
            time.sleep(4)
        
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(4)

            email_input = driver.find_element(by=By.NAME, value="identifier")
            email_input.clear()
            email_input.send_keys("")# email
            time.sleep(4)
            email_input.send_keys(Keys.ENTER)
            time.sleep(4)

            password = driver.find_element(by=By.NAME, value="Passwd")
            password.send_keys("")# pasword
            time.sleep(4)
            password.send_keys(Keys.ENTER)
            time.sleep(4)

            cont = driver.find_element(by=By.XPATH, value="//span[contains(text(),'Продолжить')]")
            cont.click()
            time.sleep(10)

            driver.switch_to.window(driver.window_handles[0])
            time.sleep(4)

        except Exception as ex:
            print(ex)


    def spam(self, urls):
        driver = self.driver
        c = 0
        for i in urls: 

            driver.get(i)
            time.sleep(4)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(7)

            comment = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/div")
            comment.send_keys(f"Hello")
            comment.send_keys(Keys.ENTER)
            time.sleep(6)
    

    def get_all_posts_urls(self):
        driver = self.driver
        global urls
        url = "https://www.tiktok.com/search?q=%D1%81%D0%B1%D1%83&t=1709475551669"
        driver.get(url)
        time.sleep(11)
        urls = set()
        

        for i in range(0,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)   
            hrefs = driver.find_elements(by=By.TAG_NAME, value="a")
                     
            for item in hrefs:
                href = item.get_attribute('href')
                if url and "/video/" in href:
                    urls.add(href)

        for j in urls:
            print(j)
                    
    
    def subscibe(self):

        driver = self.driver
        global users
        users = set()

        driver.get("https://www.tiktok.com/@majlo_bpemehu")
        time.sleep(4)

        sub = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[2]/span")
        sub.click()
        time.sleep(14)

        for i in range(0, 6):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)  

            hrefs = driver.find_elements(by=By.TAG_NAME, value="p")
            hrefs = hrefs[7:]

            for item in hrefs:
                users.add(item.text)

        print(users)

bot = TiktokBot()
