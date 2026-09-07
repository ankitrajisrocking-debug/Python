import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://news.ycombinator.com/"

# Send a request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all headline links
    headlines = soup.find_all("span", class_="titleline")

    print("News Headlines and Hyperlinks:\n")

    # Extract and display headline and URL
    for i, headline in enumerate(headlines, start=1):
        link = headline.find("a")

        if link:
            title = link.get_text(strip=True)
            href = link.get("href")

            print(f"{i}. {title}")
            print(f"   Link: {href}\n")

else:
    print("Failed to retrieve the webpage.")

