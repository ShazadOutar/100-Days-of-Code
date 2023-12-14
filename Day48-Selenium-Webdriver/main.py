# auto-playing a cookie clicker game
import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# # keep Chrome open after the program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(chrome_options)
# # driver.get(url="https://orteil.dashnet.org/cookieclicker/")
# driver.get(url="https://orteil.dashnet.org/experiments/cookie/")
#
# # close the language option
# sleep(4)
# driver.find_element(By.ID, value="langSelect-EN").click()
# sleep(1)
# # driver.implicitly_wait(2)
# # wait = WebDriverWait(driver=driver, timeout=2)
#
# cookie_button = driver.find_element(By.ID, value="bigCookie")
# # cookie_button = wait.until(EC.element_to_be_clickable(()))
# # cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
#
# # set a timeout for 5 minutes from the start of the loop
# starting_time = time.time()
# timeout = starting_time + 11
# # upgrades = driver.find_elements(By.CLASS_NAME, value="products")
# # print("upgrades\n\n")
# # print(upgrades)
# num_of_cookies = driver.find_element(By.ID, value="cookies").text
# while True:
#     print(round(time.time() - starting_time))
#     if (round(time.time() - starting_time) % 5) == 0:
#         print("5 second interval")
#         # buy upgrades
#         print(f"cookies: {num_of_cookies}")
#     if time.time() < timeout:
#         print(time.time())
#         cookie_button.click()
#     else:
#         print("after time")
#         upgrades = driver.find_elements(By.CLASS_NAME, value="products")
#         for upgrade in upgrades:
#             # print(upgrade.find_element(By.CLASS_NAME, value="price").get_property("id"))
#             print(upgrade.find_element(By.CSS_SELECTOR, value=".content .price").text)
#         # print(driver.find_element(By.ID, value="cookies").text)
#         break
#     # pass
#     # if time.time() < timeout:
#         # every 5 seconds check for affordable upgrades
#         # cookie_button.click()
#     # else:
#     #     driver.quit()
#     #     break
#

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_current_balance(driver) -> int:
    # find current balance
    balance = int(driver.find_element(By.ID, value="money").text)
    # print(balance)
    return balance


def buy_upgrade(driver):
    # buy the most expensive upgrade
    # get the store section
    # store = driver.find_elements(By.CSS_SELECTOR, "#store div")
    # store.pop()

    # print(len(store))
    # for i in store:
    #     print(i.text)
    #     price = i.text.strip().split()
    #     print(price[3])

    # TODO: Try moving this to the main function and passing the store page as a input parameter instead
    # get the store items
    store_divs = driver.find_elements(By.CSS_SELECTOR, "#store div")
    # store_divs.pop()
    item_ids = [div.get_attribute("id") for div in store_divs]

    balance = get_current_balance(driver)
    # loop through in reverse and try to buy the most expensive item
    for item in store_divs[::-1]:
        try:
            # print(item.text.strip().split("-"))
            cost = int(item.text.strip().split("-")[1].split("\n")[0].strip().replace(",", ""))
            # print(f"Cost is: {cost}")
            # balance = get_current_balance(driver)
            # print(f"Balance is: {balance}")
            if balance >= cost:
                # then buy item
                # print(item)
                # print(cost)
                item.click()
        except IndexError:
            # print("in except")
            # print(item.text)
            # print("after")
            pass


def main():
    print("Main")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    # open the website
    driver.get("http://orteil.dashnet.org/experiments/cookie/")

    # find the cookie to click on
    cookie = driver.find_element(By.ID, value="cookie")
    # cookie.click()

    # run for 5 minutes
    starting_time = time.time()
    ending_time = starting_time + 60*1

    # for i in range(50):
    for i in range(100):
        cookie.click()

    while ending_time > time.time():
        cookie.click()
        if round(time.time() - starting_time) % 5 == 0:
            get_current_balance(driver)
            buy_upgrade(driver)

    # get_current_balance(driver)
    # buy_upgrade(driver)


if __name__ == "__main__":
    main()
