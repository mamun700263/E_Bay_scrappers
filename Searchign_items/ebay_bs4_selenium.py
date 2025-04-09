import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.selenium_utils import get_driver, sleeper

driver = get_driver()

target_website = "https://www.ebay.com/"
driver.get(target_website)
sleeper()

search = driver.find_element(By.XPATH, '//input[@name="_nkw"]')
target_item = "laptop"
search.clear()
search.send_keys(target_item)
search.send_keys(Keys.ENTER)
sleeper()

response = driver.page_source
soup = BeautifulSoup(response, "lxml")


result_div = soup.find("div", id="srp-river-results")

list_iems = result_div.find("ul", 
                            class_="srp-results srp-list clearfix").find_all(
    "li", class_="s-item s-item__pl-on-bottom"
)


dic_list = []

for item in list_iems:
    try:
        name = item.find("span", role="heading").text
    except:
        name = "not found"
    try:
        link = item.find("a")["href"]
    except:
        link = "not found"
    try:
        price = (
            item.find("span", class_="s-item__price").find("span", class_="BOLD").text
        )
    except:
        price = "not found"
    x = {
        "name": name,
        "link": link,
        "price": price,
    }
    dic_list.append(x)

driver.quit()
df = pd.DataFrame(dic_list)
df.to_csv("Searchign_items/ebay_laptops.csv", index=False)



