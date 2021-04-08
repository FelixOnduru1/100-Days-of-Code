from internet_speed_bot import InternetSpeedBot
from tweet_bot import TweetBot
import os

PROMISED_DOWN = 2
PROMISED_UP = 0.2
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
TWITTER_URL = "https://twitter.com/"
CHROME_DRIVER_PATH = "C:/Users/WORLDCOLE/Documents/DEVELOPMENT/chromedriver.exe"

internet_speed_bot = InternetSpeedBot(driver_path=CHROME_DRIVER_PATH)
internet_speed_bot.get_internet_speed()
download_speed = float(internet_speed_bot.down)
upload_speed = float(internet_speed_bot.up)

if download_speed < PROMISED_DOWN and upload_speed < PROMISED_UP:
    tweet = f"Hey Internet Provider, why is my internet speed {download_speed}down/{upload_speed}up" \
            f" when I was promised {PROMISED_DOWN}down/{PROMISED_UP}up?"

    tweet_bot = TweetBot(driver_path=CHROME_DRIVER_PATH)
    tweet_bot.tweet(tweet=tweet)
