import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://www.moneycontrol.com/news/business/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("li", class_="clearfix")
    news_list = []

    for a in articles[:5]:
        news_list.append(a.find("h2").text.strip())

    return news_list
