import csv
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://books.toscrape.com/"
START_URL = BASE_URL + "catalogue/page-1.html"
OUTPUT_FILE = "books.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BookScraper/1.0)"
}


def scrape_books():
    """Scrape book information from all catalog pages."""

    books = []
    url = START_URL
    page_number = 1

    session = requests.Session()
    session.headers.update(HEADERS)

    while url:
        print(f"Scraping page {page_number}: {url}")

        try:
            response = session.get(url, timeout=15)
            response.raise_for_status()
        except requests.RequestException as error:
            print(f"Error requesting page: {error}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        # Find every book on the current page
        products = soup.select("article.product_pod")

        for product in products:
            # Title
            title_element = product.select_one("h3 a")
            title = title_element.get("title", "").strip()

            # Product URL
            product_url = urljoin(url, title_element.get("href", ""))

            # Price
            price_element = product.select_one("p.price_color")
            price = price_element.get_text(strip=True)

            # Availability
            availability_element = product.select_one("p.availability")
            availability = availability_element.get_text(" ", strip=True)

            # Rating
            rating_element = product.select_one("p.star-rating")
            rating_classes = rating_element.get("class", [])

            rating = ""
            if len(rating_classes) > 1:
                rating = rating_classes[1]

            # Image URL
            image_element = product.select_one("img")
            image_url = ""

            if image_element:
                image_url = urljoin(
                    url,
                    image_element.get("src", "")
                )

            books.append({
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "product_url": product_url,
                "image_url": image_url
            })

        # Find the "next" page
        next_button = soup.select_one("li.next a")

        if next_button:
            url = urljoin(url, next_button.get("href"))
            page_number += 1
            time.sleep(1)  # Be polite to the server
        else:
            url = None

    return books


def save_to_csv(books):
    """Save scraped books to a CSV file."""

    fieldnames = [
        "title",
        "price",
        "availability",
        "rating",
        "product_url",
        "image_url"
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(books)


if __name__ == "__main__":
    print("Starting book scraper...\n")

    books = scrape_books()

    save_to_csv(books)

    print("\nScraping completed!")
    print(f"Books scraped: {len(books)}")
    print(f"CSV file created: {OUTPUT_FILE}")

