# create a dictionary of the items in the latest news from the python website
# {index: {time, name}
from selenium import webdriver
from selenium.webdriver.common.by import By

# create a new driver
driver = webdriver.Chrome()
driver.get("https://www.python.org/")

menu = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# for i in range(5):
events_list = menu.text.split("\n")
# print(events_list)
dates = [date for date in events_list[::2]]
names = [name for name in events_list[1::2]]

# print(dates)
# print(names)
events_dict = {}

for event_number in range(len(dates)):
    events_dict[event_number] = {
        "time": dates[event_number],
        "name": names[event_number]
    }

print(events_dict)
