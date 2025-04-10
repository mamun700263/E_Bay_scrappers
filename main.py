from ebay_scrapper.search_items.search import search_items

if __name__ == "__main__":
    df = search_items("laptop")
    print(df.head())
