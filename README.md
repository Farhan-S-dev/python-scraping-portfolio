# Hacker News Web Scraper

A simple Python web scraper that collects headlines and links from the Hacker News front page and saves them to a CSV file.

## What It Does

- Sends a request to the Hacker News front page
- Parses the HTML with BeautifulSoup
- Extracts article headlines and URLs
- Saves the results to `hacker_news.csv`

## Project Files

```text
Scraper.py
hacker_news.csv
requirements.txt
README.md
```

## Requirements

- Python 3
- requests
- beautifulsoup4

Install the required packages with:

```bash
pip install -r requirements.txt
```

## How to Run

Run:

```bash
python Scraper.py
```

After the script finishes, it creates:

```text
hacker_news.csv
```

The CSV contains:

```text
Headline | Link
```

## Purpose

This project was built to practice basic HTML web scraping with Python, BeautifulSoup, loops, element selection, and CSV export.

## Limitations

- It scrapes only the Hacker News front page.
- It depends on the current HTML structure of Hacker News.
- It does not currently include request retries or advanced error handling.
