from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
print(largest_number)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])




















#----------------------------------------- Scraping website from local

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# class_is_heading = soup.find_all(class_="heading")
#
# h3_heading = soup.find(name="h3", class_="heading")
# print(h3_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)