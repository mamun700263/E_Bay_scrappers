from ebay_scrapper.search_items.ebay_bs4_selenium import search_items

def test_search_returns_dataframe():
    df = search_items("laptop", "","csv")
    assert not df.empty
    assert "name" in df.columns

