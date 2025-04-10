from ebay_scrapper.search_items.search import search_items

def test_search_returns_dataframe():
    df = search_items("laptop", "","csv")
    assert not df.empty
    assert "name" in df.columns

