from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Credentials from .env
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


def initialize_driver():
    """Initialize the Selenium WebDriver."""
    driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed and accessible
    driver.maximize_window()
    return driver


def twitter_login(driver):
    """Log into Twitter using the credentials from .env."""
    try:
        driver.get("https://twitter.com/login")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "text")))

        # Enter username
        username_field = driver.find_element(By.NAME, "text")
        username_field.send_keys(TWITTER_USERNAME)
        username_field.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the password field to load

        # Enter password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for the login process to complete
    except Exception as e:
        print("Error during login:", e)


def post_tweet(driver, tweet_text):
    """Post a tweet with the given text."""
    try:
        driver.get("https://twitter.com/compose/tweet")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Post text' and @role='textbox' and @data-testid='tweetTextarea_0']"))
        )

        # Enter tweet text
        tweet_box = driver.find_element(By.XPATH, "//div[@aria-label='Post text' and @role='textbox' and @data-testid='tweetTextarea_0']")
        tweet_box.send_keys(tweet_text)
        time.sleep(2)

        # Wait for the tweet button and click it
        tweet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1cwvpvk r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l' and @data-testid='tweetButton']"))
        )
        time.sleep(3)  # Wait for the tweet to be posted
        tweet_button.click()
        time.sleep(3)
    except Exception as e:
        print("Error during posting tweet:", e)


def like_tweet(driver, tweet_url):
    """Like a tweet at the given URL."""
    try:
        driver.get(tweet_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='css-175oi2r r-1777fci r-bt1l66 r-bztko3 r-lrvibr r-1loqt21 r-1ny4l3l' and @data-testid='like']"))
        )
        time.sleep(3)

        # Click on the like button
        like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='css-175oi2r r-1777fci r-bt1l66 r-bztko3 r-lrvibr r-1loqt21 r-1ny4l3l' and @data-testid='like']"))
        )
        like_button.click()
        time.sleep(3)
    except Exception as e:
        print("Error during liking tweet:", e)


def quote_retweet_tweet(driver, retweet_url):
    """Quote retweet a tweet at the given URL."""
    try:
        # Navigate to the tweet URL
        driver.get(retweet_url)
        
        # Wait until the retweet button is clickable (ensure the div is present and it's clickable)
        retweet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='retweet' and contains(@class, 'r-1loqt21')]"))
        )
        retweet_button.click()  # Click on the retweet button
        time.sleep(3)

        # Wait for the "Quote Tweet" option to be clickable
        quote_tweet_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/compose/post' and contains(@class, 'r-1loqt21') and .//span[text()='Quote']]"))
        )
        quote_tweet_option.click()  # Click on the Quote Tweet option
        time.sleep(3)

        # Wait for the text box to appear where you can add your quote text
        quote_textbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Post text' and @role='textbox' and @data-testid='tweetTextarea_0']"))
        )
        
        # Add your quote text (example: "Check this out!")
        quote_textbox.send_keys("Check this out! - Automated Message")  # You can replace this with your dynamic text
        time.sleep(3)

        # Wait until the "Tweet" button to send the quote retweet is clickable
        tweet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1cwvpvk r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l' and @data-testid='tweetButton']"))
        )
        tweet_button.click()  # Click the tweet button to post the quote retweet
        
        time.sleep(3)  # Optional: wait for the process to complete

    except Exception as e:
        print("Error during quote retweeting:", e)


if __name__ == "__main__":
    # Initialize the WebDriver
    driver = initialize_driver()

    try:
        # Log into Twitter
        twitter_login(driver)

        # Post a tweet
        post_tweet(driver, "Automated Tweet using Selenium.")

        # Like a specific tweet
        tweet_url = "https://x.com/varun_al/status/1449244545397374981"  # Replace with actual tweet URL
        like_tweet(driver, tweet_url)

        # Retweet a specific tweet
        retweet_url = "https://x.com/ValorantUpdated/status/1801265515647635812"
        quote_retweet_tweet(driver, retweet_url)

    finally:
        # Close the browser
        driver.quit()
        print("Automation Done")
