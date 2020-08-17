from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
browser = webdriver.Chrome("C:\\Users\\96075\\Desktop\\全部资料\\Python\\爬虫\\chromedriver.exe")
#设置等待时间
wait = WebDriverWait(browser,20)

def crawl_page():
    try:
        url = "http://www.google.com/cse?oe=utf8&ie=utf8&source=uds&q=2020+election&safe=off&start=20&sort=&cx=017476104391584697148:yfiniwqwjp4"
        browser.get(url)
        time.sleep(5)
        for i in range(10):
            sumbit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.gsc-cursor-page")))
            sumbit_button.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "gsc-webResult gsc-result")))
        get_html()
    except:
        crawl_page()

def get_html():
    html = browser.page_source
    soup = BeautifulSoup(html.text,"lxml")
    href = soup.select("div.gs-title a.gs-title")
    for h in href[1::2]:
        print(h)

if __name__ == '__main__':
    crawl_page()


