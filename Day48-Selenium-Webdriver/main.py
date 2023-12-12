# auto-playing a cookie clicker game
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# keep Chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url="https://orteil.dashnet.org/cookieclicker/")

# close the language option
sleep(4)
driver.find_element(By.ID, value="langSelect-EN").click()
sleep(1)
# driver.implicitly_wait(2)
# wait = WebDriverWait(driver=driver, timeout=2)

cookie_button = driver.find_element(By.ID, value="bigCookie")
# cookie_button = wait.until(EC.element_to_be_clickable(()))
# cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))

# set a timeout for 5 minutes from the start of the loop
timeout = time.time() + 11

while True:
    pass
    # if time.time() < timeout:
        # every 5 seconds check for affordable upgrades
        # cookie_button.click()
    # else:
    #     driver.quit()
    #     break

