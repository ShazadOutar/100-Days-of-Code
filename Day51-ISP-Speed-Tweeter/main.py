from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def create_driver(self):
        pass

    def get_internet_speed(self):
        # open the website
        # self.driver.get(url="https://www.speedtest.net/")
        # self.driver.get(url="https://www.speedtest.net/result/15892368818")
        self.driver.get(url="https://fast.com/")
        # There were issues with the speedtest site loading so switched sites
        # give the site a few seconds to load in
        sleep(3)

        # first press the go button to start the test
        # make sure to wait a few seconds to make sure the button is loaded in
        # self.driver.implicitly_wait(3) I never told it what to wait on
        # go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        # go_button.click()

        # after the go button is pressed, get the download and upload speeds
        # wait for the tests to be completed
        # self.driver.implicitly_wait(3)
        # download speed
        # speed = driver.find_element(By.CLASS_NAME, value="result-data").find_element(By.CLASS_NAME, value="result-data-large").text
        # self.driver.implicitly_wait(3)
        sleep(7)

        # press the show more info button to get the upload and download speeds
        show_more_button = self.driver.find_element(By.ID, value="show-more-details-link")
        show_more_button.click()
        # get the download speed
        download_speed = self.driver.find_element(By.ID, value="down-mb-value").text
        print(f"Download speed: {download_speed}")
        self.up = download_speed

        # get the upload speed
        # wait for it to test the upload speed
        sleep(13)
        upload_speed = self.driver.find_element(By.ID, value="up-mb-value").text
        print(f"Upload speed: {upload_speed}")
        self.down = upload_speed

    def tweet_at_provider(self):
        # Handle the sign-in steps
        self.driver.get(url="https://twitter.com/?lang=en")
        # press the sign-in button
        self.driver.implicitly_wait(2)
        # sleep(2)
        sign_in_button = self.driver.find_element(By.XPATH,
                                                  value="/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span")
        sign_in_button.click()
        # self.driver.implicitly_wait(2)
        # sleep(2)
        email_form = self.driver.find_element(By.XPATH,
                                              value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        # Fill in the twitter email
        email_form.send_keys(TWITTER_EMAIL)
        email_form.send_keys(Keys.ENTER)

        # enter the twitter password
        password_form = self.driver.find_element(By.XPATH,
                                                 value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_form.send_keys(TWITTER_PASSWORD)
        password_form.send_keys(Keys.ENTER)

        # handle the making the post
        post_box = self.driver.find_element(By.XPATH,
                                            value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        post_box.send_keys(TWITTER_EMAIL)
        post_text = f"My internet speed is {self.up} up and {self.down} down"
        print(post_text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myInternetSpeedTwitterBot = InternetSpeedTwitterBot()
    # driver = myInternetSpeedTwitterBot.create_driver()
    myInternetSpeedTwitterBot.get_internet_speed()
    myInternetSpeedTwitterBot.tweet_at_provider()
