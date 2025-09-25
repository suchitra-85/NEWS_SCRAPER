# news_scraper.py
# Task: Scrape top headlines from a news website
# Tools: Python, requests, BeautifulSoup
# Deliverable: Python script + headlines.txt file

import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    # Step 1: Choose a website (BBC News used here as example)
    url = "https://www.bbc.com/news"

    try:
        # Step 2: Send GET request to fetch page content
        response = requests.get(url)
        response.raise_for_status()  # raise error if request failed
    except requests.exceptions.RequestException as e:
        print("Error fetching the website:", e)
        return

    # Step 3: Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 4: Extract headlines (BBC uses <h2> for many news headlines)
    headlines = []
    for h in soup.find_all("h2"):
        text = h.get_text(strip=True)
        if text and text not in headlines:  # avoid duplicates
            headlines.append(text)

    # Step 5: Save headlines into a .txt file
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for i, headline in enumerate(headlines, start=1):
            f.write(f"{i}. {headline}\n")

    print(f"✅ Scraping completed! {len(headlines)} headlines saved to 'headlines.txt'")

if __name__ == "__main__":
    scrape_headlines()
