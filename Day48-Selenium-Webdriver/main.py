# auto-playing a cookie clicker game
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# keep Chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url="https://orteil.dashnet.org/cookieclicker/")

# close the language option
sleep(4)
driver.find_element(By.ID, value="langSelect-EN").click()

cookie_button = driver.find_element(By.ID, value="bigCookie")
while True:
    cookie_button.click()

