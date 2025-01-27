import time

from selenium.webdriver.common.by import By

from seleniumTraining.hilton.pages.join_page import joinPage
from seleniumTraining.hilton.tests.selenuimBaseHilton import seleniumBaseHilton


class join_new_user():
    base = seleniumBaseHilton()
    driver = base.selenium_start()
    join_page = joinPage(driver)

    driver.get("https://www.hilton.com/en/")
    time.sleep(3)
    free_join = driver.find_element(By.LINK_TEXT,"Join for Free")
    free_join.click()
    # search

    join_page.join_new_user("sara","spitz","02-9999999", "02-9999999")