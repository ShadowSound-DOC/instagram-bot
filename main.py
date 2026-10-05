import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

class Instagram_bot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36)")
        self.chrome_options.add_experimental_option("detach", True)
        # Initialize Selenium WebDriver (e.g., Chrome)
        self.driver = webdriver.Chrome(options=self.chrome_options)  # Make sure to have the appropriate driver installed
        # Initialize properties to store speeds

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.login_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        self.login_box.send_keys(EMAIL)
        self.decline_cookies = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        self.decline_cookies.click()
        self.password_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        self.password_box.send_keys(PASSWORD)
        self.password_box.send_keys(Keys.ENTER)
        time.sleep(6)

    def find_followers(self):
        self.user = input("What account do you want to follow bot?")
        self.driver.get(f"https://www.instagram.com/{self.user}/")
        time.sleep(3)
        self.followers_list_url = self.driver.get(f"https://www.instagram.com/{self.user}/followers/")

    def follow(self):
        following = True
        while following is True:
            self.followers_list_element = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div')
            self.followers = self.followers_list_element.find_elements(By.CSS_SELECTOR, '[style="display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px; position: relative;"]')
            followers_list = [element for element in self.followers]
            for item in followers_list:
                self.follow_button = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]')
                self.follow_button.click()
                if item in followers_list:
                    pass
                else:
                    followers_list.append(item)

bot = Instagram_bot()
bot.login()
bot.find_followers()
bot.follow()