# Twitter Automation using Selenium

This project automates the process of logging into Twitter, posting a tweet, liking a tweet, and quote retweeting using Selenium WebDriver and Python. It interacts with the Twitter website by simulating user actions like logging in, posting a tweet, liking specific tweets, and reposting tweets (quote retweet).

## Features
- **Automated Twitter Login**: Logs into Twitter using stored credentials.
- **Post a Tweet**: Automatically posts a tweet with a given message.
- **Like a Tweet**: Likes a specific tweet using its URL.
- **Quote Retweet a Tweet**: Quote retweets a specific tweet with a custom message.

## Prerequisites
Before running the project, make sure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- Chrome browser
- ChromeDriver (ensure it's installed and compatible with your Chrome version)

## Installation Steps

### 1. Clone the Repository
Clone the repository using Git:

```bash
git clone https://github.com/varun-al/Twitter-Automation-using-Selenium.git
cd twitter-automation-selenium
```

### 2. Install Dependencies
Install the required Python packages using pip:
```bash
pip install selenium python-dotenv
```

### 3. Install chromedriver:

To run Selenium with Chrome, you'll need to install chromedriver. You can install it using the following command:
```bash
pip install chromedriver-autoinstaller
```

### 4. Set up .env File
In the root directory of the project, create a .env file and add your Twitter credentials:
```bash
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password
```
Replace your_twitter_username and your_twitter_password with your actual Twitter login credentials.

### 5. Run the Script
After setting up your environment, run the Python script to start the automation:
```bash 
python twitter_automation.py
```


## How It Works

- **Selenium WebDriver** is used to interact with the Twitter web interface.
- **Python-dotenv** is used to load sensitive credentials securely from the `.env` file.
- The script first logs into Twitter, waits for the login process to complete, then performs actions like posting a tweet, liking a tweet, and reposting a tweet.

## Example Usage

The script includes the following functionalities:

1. **Post a Tweet**: The script posts a tweet with the text `"Automated Tweet using Selenium."`
2. **Like a Tweet**: A specific tweet is liked using its URL.
3. **Quote Retweet**: The script performs a quote retweet with a custom message ("Check this out! - Automated Message").

You can modify the tweet text, URLs, and other configurations as per your requirement.

## Troubleshooting

- **ChromeDriver Not Found**: Ensure that ChromeDriver is installed and compatible with your Chrome version. You can download it from [here](https://googlechromelabs.github.io/chrome-for-testing/).
- **Login Issues**: If you encounter issues with login, ensure that your Twitter credentials in the `.env` file are correct.