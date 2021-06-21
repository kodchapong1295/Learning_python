import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100"
input_date = input("Which year do you want to travel to? Type the date in the format of YYYY-MM-DD: ")

response = requests.get(f"{URL}/{input_date}")
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

song_title_tags = soup.find_all(name="span", class_="chart-element__information__song")
song_titles = [tag.getText() for tag in song_title_tags]

print(song_titles)


