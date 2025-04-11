import argparse

from ebay_scraper.searchItems.search import search_items

def main():
    parser = argparse.ArgumentParser(description="Search items on eBay and scrape product data.")
    parser.add_argument("--search", "-s", type=str, required=True, help="Search keyword (e.g. macbook)")
    parser.add_argument("--limit", "-l", type=int, default=10, help="Number of products to scrape")
    parser.add_argument("--output", "-o", type=str, default="results.csv", help="Output filename")

    args = parser.parse_args()

    print("Starting scraper...")

    search_items(
        keyword=args.search,
        save_path="sample_data/",
        filename=args.output,
        file_format="csv",
    )



if __name__ == "__main__":
    main()