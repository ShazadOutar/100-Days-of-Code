from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


def sign_in(driver, email, password):
    """Sign in to your LinkedIn account from the home page"""
    time.sleep(2)
    # fill in the email
    username_field = driver.find_element(By.ID, value="session_key")
    username_field.send_keys(email)
    # fill in the password
    password_field = driver.find_element(By.ID, value="session_password")
    password_field.send_keys(password)
    # click submit
    button_field = driver.find_element(By.CLASS_NAME, value="sign-in-form__submit-btn--full-width")
    button_field.click()


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    # open the website
    driver.get(url="https://www.linkedin.com/")
    # Sign in to your LinkedIn account
    sign_in(driver=driver, email=EMAIL, password=PASSWORD)

    # do a search
    driver.get(url="https://www.linkedin.com/jobs/search/"
                   "?currentJobId=3706566866&geoId=102571732&keywords=python%20developer&"
                   "location=New%20York%2C%20New%20York%2C%20United%20States&"
                   "origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
   

if __name__ == "__main__":
    main()
