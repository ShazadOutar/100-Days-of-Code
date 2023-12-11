# fill in this form automatically
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

first_name = "First"
last_name = "Second"
email = f"{first_name}{last_name}@email.com"

# keep Chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")

first_name_form = driver.find_element(By.NAME, value="fName")
# print(first_name_form.get_attribute("placeholder"))
first_name_form.send_keys(first_name)

last_name_form = driver.find_element(By.NAME, value="lName")
last_name_form.send_keys(last_name)

email_form = driver.find_element(By.NAME, value="email")
email_form.send_keys(email)

sleep(1)
email_form.send_keys(Keys.ENTER)
