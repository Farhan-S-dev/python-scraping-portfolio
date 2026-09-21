import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

article_tags = soup.find_all("span", class_="titleline")

with open("hacker_news.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline", "Link"])

    for article in article_tags:
        headline = article.text
        link_tag = article.find("a")

        if link_tag:
            link = link_tag.get("href")
            writer.writerow([headline, link])

print("Scraping complete! Check your folder for the CSV file.")
