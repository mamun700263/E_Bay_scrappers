# eBay Scraper - Searching Items

This folder contains the implementation of a web scraper that searches for specific items on eBay.

## Features
- Scrapes eBay for items based on a search query.
- Extracts relevant details such as:
  - Item name
  - Price
  - Item link
- Outputs the data in a structured CSV format for further use or analysis.

## Requirements
- Python 3.x
- Required libraries (install via `pip`):
    - `requests`: For sending HTTP requests (though not directly used in the script).
    - `beautifulsoup4`: For parsing HTML data.
    - `pandas`: For handling and saving data in a CSV format.
    - `selenium`: For automating the browser to scrape dynamic content.
    - `lxml`: For fast and efficient HTML parsing with BeautifulSoup.

## Setup and Usage

1. **Clone the repository** and navigate to this folder:
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the scraper script**:
    ```bash
    python scraper.py
    ```

4. When prompted, **provide the search query** (e.g., "laptop") for which you want to search on eBay.

## Output
The scraper will generate a CSV file called `ebay_laptops.csv` containing the scraped data.

## Disclaimer
This project is for educational purposes only. Scraping websites may violate their terms of service. Use responsibly and ensure you're in compliance with eBay's terms before running the scraper.

## Notes
- Make sure you have the appropriate **web driver** (e.g., ChromeDriver or GeckoDriver) installed for Selenium to work with your browser. The driver should match the browser version you're using.
- If you want to extend this scraper, consider adding **pagination support** to collect results from multiple pages.

