import requests
from bs4 import BeautifulSoup
import csv  # 1. We open our toolbox and take out the built-in CSV tool

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

article_tags = soup.find_all("span", class_="titleline")

# 2. Open a blank ledger book and get ready to write
with open("hacker_news.csv", "w", newline="", encoding="utf-8") as file:
    # 3. Grab our special CSV formatting pen
    writer = csv.writer(file)

    # 4. Write the title names at the very top of our columns
    writer.writerow(["Headline", "Link"])

    # 5. Loop through our stack of folders just like before
    for article in article_tags:
        headline = article.text
        link_tag = article.find("a")

        # A quick safety check: Make sure an envelope actually exists inside the folder
        if link_tag:
            link = link_tag.get("href")

            # 6. Write the headline and link side-by-side into the ledger book
            writer.writerow([headline, link])

print("Scraping complete! Check your folder for the CSV file.")