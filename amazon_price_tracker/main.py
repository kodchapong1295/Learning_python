import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from decouple import config

URL = "https://www.amazon.com/dp/B084F4KQYN/ref=sbl_dpx_B08GC6PL3D_0"
MY_EMAIL = config('MY_EMAIL')
PASSWORD = config('PASSWORD')
BUY_PRICE = 150

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(URL, headers=headers)
website_html = response.content


soup = BeautifulSoup(website_html, "lxml")
price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

product_name = soup.find(id="productTitle").get_text()

if price_as_float <= BUY_PRICE:
    message = f"{product_name} is now {price_as_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{URL}"
        )
