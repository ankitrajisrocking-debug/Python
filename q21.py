# --- 1. IMPORTS ---
import csv                      # Built-in module for reading and writing CSV spreadsheet files
import time                     # Built-in module used here to pause execution between page requests
from urllib.parse import urljoin # Helper function to safely combine a base URL with relative paths (e.g., "../book.html")

import requests                 # Third-party library for sending HTTP requests to fetch web pages
from bs4 import BeautifulSoup   # Third-party library for parsing HTML and extracting specific elements


# --- 2. CONFIGURATION CONSTANTS ---
BASE_URL = "https://books.toscrape.com/"              # Root domain of the target website
START_URL = BASE_URL + "catalogue/page-1.html"        # Exact URL of the first catalog page to start scraping
OUTPUT_FILE = "books.csv"                             # Name of the output CSV file to save results into

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BookScraper/1.0)" # Identifies the script as a browser/bot to the web server
}


# --- 3. SCRAPING FUNCTION ---
def scrape_books():
    """Scrape book information from all catalog pages."""

    books = []                  # Master list that will store a dictionary for each scraped book
    url = START_URL             # Tracks the current page URL being scraped; starts at page 1
    page_number = 1             # Counter to track and print which page number we are currently on

    session = requests.Session() # Creates a persistent HTTP session (reuses TCP connections for better speed)
    session.headers.update(HEADERS) # Applies our custom User-Agent header to every request made in this session

    # Loop continues as long as there is a valid 'url' to scrape (stops when 'url' becomes None)
    while url:
        print(f"Scraping page {page_number}: {url}") # Prints progress to the console

        try:
            response = session.get(url, timeout=15) # Sends an HTTP GET request; aborts if server takes > 15 seconds
            response.raise_for_status()             # Raises an error if the HTTP status is 4xx or 5xx (e.g., 404 Not Found)
        except requests.RequestException as error:  # Catches network errors, timeouts, or bad HTTP status codes
            print(f"Error requesting page: {error}") # Logs the error message
            break                                   # Exits the while loop early if a page fails to load

        # Parses the raw HTML text of the downloaded page into a searchable BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")

        # Selects all <article class="product_pod"> tags; each one represents a single book card on the page
        products = soup.select("article.product_pod")

        # Loops through every book card found on the current page
        for product in products:
            # --- Extract Title ---
            title_element = product.select_one("h3 a") # Finds the <a> link inside the <h3> tag
            # Reads the full title from the HTML 'title' attribute (since visible text is often truncated with '...')
            title = title_element.get("title", "").strip()

            # --- Extract Product URL ---
            # Gets the relative 'href' link and joins it with the current page URL to make a full clickable URL
            product_url = urljoin(url, title_element.get("href", ""))

            # --- Extract Price ---
            price_element = product.select_one("p.price_color") # Finds the <p class="price_color"> tag
            price = price_element.get_text(strip=True)          # Extracts the price string (e.g., "£51.77") and trims whitespace

            # --- Extract Availability ---
            availability_element = product.select_one("p.availability") # Finds <p class="availability">
            # Joins inner text pieces with a single space and removes extra newlines/whitespace (e.g., "In stock")
            availability = availability_element.get_text(" ", strip=True)

            # --- Extract Star Rating ---
            rating_element = product.select_one("p.star-rating") # Finds <p class="star-rating Three">
            rating_classes = rating_element.get("class", [])     # Returns a list of CSS classes, e.g., ["star-rating", "Three"]

            rating = ""                                          # Default empty string in case rating is missing
            if len(rating_classes) > 1:                          # Checks if a second class name (the rating word) exists
                rating = rating_classes[1]                       # Grabs the second class name (e.g., "One", "Two", "Three")

            # --- Extract Cover Image URL ---
            image_element = product.select_one("img")            # Finds the <img> tag inside the book card
            image_url = ""                                       # Default empty string if no image tag is found

            if image_element:
                image_url = urljoin(                             # Converts the relative image 'src' into a full URL
                    url,
                    image_element.get("src", "")
                )

            # Packages all 6 extracted fields into a dictionary and adds it to our master 'books' list
            books.append({
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "product_url": product_url,
                "image_url": image_url
            })

        # --- Pagination (Moving to the Next Page) ---
        next_button = soup.select_one("li.next a") # Looks for the "next" button link at the bottom of the page

        if next_button:                                          # If a "next" button exists...
            url = urljoin(url, next_button.get("href"))          # Updates 'url' to the next page's full address
            page_number += 1                                     # Increments our page counter by 1
            time.sleep(1)                                        # Pauses 1 second to avoid overloading the server
        else:                                                    # If there is no "next" button (we reached the last page)...
            url = None                                           # Sets 'url' to None, which terminates the 'while' loop

    return books                                                 # Returns the complete list of scraped book dictionaries


# --- 4. CSV EXPORT FUNCTION ---
def save_to_csv(books):
    """Save scraped books to a CSV file."""

    # Defines the exact column header names (must match the dictionary keys in 'books')
    fieldnames = [
        "title",
        "price",
        "availability",
        "rating",
        "product_url",
        "image_url"
    ]

    # Opens 'books.csv' in write mode ("w").
    # newline="" prevents blank rows between entries on Windows.
    # encoding="utf-8-sig" adds a UTF-8 BOM so Excel properly displays currency symbols like '£'.
    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as csv_file:

        # Creates a writer object that maps dictionary keys directly to CSV columns
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()    # Writes the first row containing the column headers
        writer.writerows(books) # Writes all book dictionaries as rows in the CSV file


# --- 5. ENTRY POINT ---
if __name__ == "__main__":      # Ensures the code below only runs when this file is executed directly (not imported)
    print("Starting book scraper...\n")

    books = scrape_books()      # Runs the scraper and stores the returned list of books

    save_to_csv(books)          # Saves the collected list of books into 'books.csv'

    print("\nScraping completed!")
    print(f"Books scraped: {len(books)}")        # Prints the total count of books collected (1,000 across 50 pages)
    print(f"CSV file created: {OUTPUT_FILE}")    # Confirms the output filename
