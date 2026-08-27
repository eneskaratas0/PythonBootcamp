import sys
import requests
from bs4 import BeautifulSoup


url = "https://news.ycombinator.com/"

try:

    response = requests.get(url,timeout=60)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Hata: {e}")
    sys.exit(1)


response_text = response.text

soup = BeautifulSoup(response_text,"html.parser")

lines = soup.find_all("tr", class_="athing submission")


for number, l in enumerate(lines,1):
    news = l.find_all("a")
    news_text = news[1].text
    news_links = news[1]["href"]
    print(f"{number}. LINK -> {news_links}, HEADER -> {news_text}")



