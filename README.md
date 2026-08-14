# Hacker News Web Scraper 🚀

A lightweight Python script designed to extract the latest tech headlines and their corresponding URLs from the Hacker News front page, exporting them directly into a structured CSV file.

## Features
- Fetches live data from the web using the `requests` library.
- Parses HTML structure efficiently using `BeautifulSoup`.
- Automatically formats and outputs data into a clean, spreadsheet-ready `hacker_news.csv` file with UTF-8 encoding.

## Technologies Used
- Python 3
- `requests`
- `BeautifulSoup4`
- `csv` (Python built-in)

## How to Run
1. Ensure you have the required libraries installed:
   ```bash
   pip install requests beautifulsoup4