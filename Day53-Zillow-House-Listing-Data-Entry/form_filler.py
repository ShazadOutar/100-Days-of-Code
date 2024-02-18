from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from listing_model import Listing

Form_link = ("https://docs.google.com/forms/"
             "d/e/1FAIpQLSfUw8vjdoyNsxhbt3JwSDSltWxNlxew6J4jVhF3djWIlwHTmQ/viewform?usp=sf_link")


def fill_forms(house_listings: list[Listing]):
    """
    Fill in the Google form 1 house listing at a time
    :param house_listings:
    :return:
    """
    # Create the driver to open the Google Form link
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # driver = webdriver.Chrome(options=chrome_options)
    # driver.get(url=Form_link)

    # fill in a new form for each listing
    for house in house_listings:
        # open a new form for each house
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url=Form_link)

        # give the page some time to load
        sleep(2)
        # fill in the input fields
        address_field = driver.find_element(By.CLASS_NAME, value="Xb9hP").find_element(By.XPATH,
                                                                                       value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_field.send_keys(house.address)

        price_per_month_field = driver.find_element(By.CLASS_NAME, value="Xb9hP").find_element(By.XPATH,
                                                                                               value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_per_month_field.send_keys(house.price_per_month)

        link_field = driver.find_element(By.XPATH,
                                         value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_field.send_keys(house.link)
        # link_field.send_keys(Keys.ENTER)

        # Press the submit button
        submit_button = driver.find_element(By.XPATH,
                                            value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
        submit_button.click()

        # Close the form when it's done
        driver.close()
