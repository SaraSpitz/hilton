import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class welcomePage():
    def __init__(self,driver):
        self.driver = driver

    def search(self, place):
        self.place = place
        search_where_to = self.driver.find_element(By.CSS_SELECTOR, 'input[class*="form-input"]')
        search_where_to.click()
        search_where_to.send_keys(place)
        search_where_to.send_keys(Keys.ENTER)

    def price(self):
        time.sleep(3)
        price_hotel = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="rateItem"]')
        price_hotel_text = price_hotel.text
        print(f"the low price to night in hotel in {self.place} is {price_hotel_text}")
        return price_hotel_text