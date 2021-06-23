from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 300
PROMISED_UP = 300
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
CHROME_DRIVER_PATH = "/Users/best/Developer/chromedriver"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.download = 0
        self.upload = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_btn = self.driver.find_element_by_css_selector(".start-button a")
        go_btn.click()
        time.sleep(75)

        self.download = self.driver.find_element_by_class_name("download-speed").text
        self.upload = self.driver.find_element_by_class_name("upload-speed").text
        print(f"{self.download} / {self.upload}")

        # self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element_by_name("session[username_or_email]")
        password = self.driver.find_element_by_name("session[password]")
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

internet_speed_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
internet_speed_bot.get_internet_speed()
internet_speed_bot.tweet_at_provider()