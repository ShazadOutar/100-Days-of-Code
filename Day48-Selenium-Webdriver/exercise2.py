# Use selenium to get the number of articles off the Wikipedia main page

from selenium import webdriver
from selenium.webdriver.common.by import By

# create a chrome webdriver
driver = webdriver.Chrome()

# open the website
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# get the value we are looking for
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
