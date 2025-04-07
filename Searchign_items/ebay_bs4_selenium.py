import random 
import time
import sys, os
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
from utils.selenium_utils import get_driver, sleeper

driver = get_driver()


driver.get("https://www.ebay.com/")


sleeper()

search = driver.find_element(By.XPATH,'//input[@name="_nkw"]')

target_item = "laptop"
search.clear()
search.send_keys(target_item)
search.send_keys(Keys.ENTER)


sleeper()



response = driver.page_source


soup = BeautifulSoup(response,'lxml')


result_div = soup.find('div',id="srp-river-results")

list_iems = result_div.find("ul",class_="srp-results srp-list clearfix").find_all("li",class_="s-item s-item__pl-on-bottom")


dic_list=[]

for item in list_iems:
    try:
        name = item.find("span",role="heading").text
    except:
        name = "not found"
    try:
        link = item.find('a')['href']
    except:
        link = "not found"
    try:
        price = item.find('span',class_="s-item__price").find('span',class_="BOLD").text
    except:
        price = 'not found'
    x = {
        'name':name,
        'link':link,
        'price':price,
    }
    dic_list.append(x)
    
