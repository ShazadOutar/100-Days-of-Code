from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a new driver
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()

# open a page
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
# driver.get("https://www.python.org/")
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# get the price of an item on amazon
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# finding the search bar on the python website
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar)
# returns a selenium element
# get the tag type
# print(search_bar.tag_name)
# get a specific attribute from the search bar
# print(search_bar.get_attribute("placeholder"))

# Finding the search button on the python website
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# Find element by CSS selector
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# Finding element by xcode path
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_property("href"))

# close a page
# close just 1 tab
# driver.close()

# finding a link by link text
# content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()

# quit the entire driver
# driver.quit()
