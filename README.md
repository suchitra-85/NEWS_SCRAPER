# NEWS_SCRAPER


## Objective
The objective of this project is to **automate the collection of top news headlines** from a public news website using Python. This allows users to quickly gather current headlines in a structured format.

## Tools Used
- **Python**: Main programming language
- **requests**: To fetch HTML content from the news website
- **BeautifulSoup**: To parse and extract news headlines from HTML
- **Git & GitHub**: For version control and repository hosting

## How It Works
1. The script uses the `requests` library to fetch the HTML of the news website (e.g., BBC News).
2. `BeautifulSoup` parses the HTML and extracts headlines, typically from `<h2>` tags.
3. All extracted headlines are saved into a text file `headlines.txt`.

## Deliverables
- `news_scraper.py`: Python script that scrapes news headlines
- `headlines.txt`: Text file containing scraped headlines

## Outcome
- Automated collection of news headlines from a public website
- Data can be used for analysis, tracking trends, or building further applications

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/suchitra-85/NEWS_SCRAPER.git
