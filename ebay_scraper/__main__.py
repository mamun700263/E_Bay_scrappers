import argparse

def main():
    parser = argparse.ArgumentParser(description="Search items on eBay and scrape product data.")
    parser.add_argument("--search", "-s", type=str, required=True, help="Search keyword (e.g. macbook)")
    parser.add_argument("--limit", "-l", type=int, default=10, help="Number of products to scrape")
    parser.add_argument("--output", "-o", type=str, default="results.csv", help="Output filename")

    args = parser.parse_args()

    # For now, just print the inputs (we'll plug into your actual scraper soon)
    print(f"Keyword: {args.search}")
    print(f"Limit: {args.limit}")
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()