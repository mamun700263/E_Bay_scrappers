import os

import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ebay_scraper.utils.selenium_utils import get_driver, sleeper


def mamun_vai():
    print("Hello, Mamun Vai! This is a test function.")


def search_items(
    keyword="laptop",
    save_path="sample_data/",
    filename=None,
    file_format="csv"
    )-> pd.DataFrame:
    """
    Search for items on eBay and scrape name, price, and link.

    Args:
        keyword (str): Search term for eBay.
        save_path (str): Directory to save the scraped file.
        filename (str): Optional custom filename (without extension).
        file_format (str): 'csv', 'json', or 'xlsx'.

    Returns:
        pd.DataFrame: DataFrame with item name, price, and link.
    """
    driver = get_driver()
    driver.get("https://www.ebay.com/")
    sleeper()

    search_box = driver.find_element(By.XPATH, '//input[@name="_nkw"]')
    search_box.clear()
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)
    sleeper()

    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()

    # Parse search results
    try:
        results_div = soup.find("div", id="srp-river-results")
        items_list = results_div.find("ul", class_="srp-results srp-list clearfix")
        item_blocks = items_list.find_all("li", class_="s-item s-item__pl-on-bottom")
    except AttributeError:
        print("[❌] Could not parse results properly.")
        return pd.DataFrame()

    scraped_data = []

    for item in item_blocks:
        name = item.find("span", role="heading")
        price = item.find("span", class_="s-item__price")
        link = item.find("a")

        scraped_data.append({
            "name": name.text if name else "not found",
            "price": price.text if price else "not found",
            "link": link["href"] if link else "not found"
        })

    df = pd.DataFrame(scraped_data)

    # Handle saving
    if not filename:
        filename = f"ebay_{keyword.replace(' ', '_')}"
    full_path = os.path.join(save_path, f"{filename}.{file_format}")

    os.makedirs(save_path, exist_ok=True)

    if file_format == "csv":
        df.to_csv(full_path, index=False)
    elif file_format == "json":
        df.to_json(full_path, orient="records", lines=True)
    elif file_format == "xlsx":
        df.to_excel(full_path, index=False)
    else:
        print(f"[⚠️] Unsupported file format: {file_format}. Skipping save.")

    print(f"[✅] Scraped data saved to {full_path}")
    return df
