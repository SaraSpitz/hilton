import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from seleniumTraining.hilton.tests.selenuimBaseHilton import seleniumBase

base = seleniumBase()
driver = base.selenium_start()
driver.get("https://www.hilton.com/en/")

search_where_to = driver.find_element(By.CSS_SELECTOR,'input[class*="form-input"]')
search_where_to.click()
search_where_to.send_keys("Miami")
search_where_to.send_keys(Keys.ENTER)

time.sleep(3)
price_first_hotel = driver.find_element(By.CSS_SELECTOR,'span[data-testid="rateItem"]')
price_first_hotel_text = price_first_hotel.text
print(f"the low price to night in hotel in miami is {price_first_hotel_text}")

time.sleep(3)
search_after_search = driver.find_element(By.CLASS_NAME,"btn-primary-link")
search_after_search.click()
search_where_to.click()
search_where_to.clear()
search_where_to.send_keys("Tel Aviv")
search_where_to.send_keys(Keys.ENTER)

# check_number_of_room_guest = driver.find_element(By.CLASS_NAME,"shop-form-btn.btn.btn-lg.relative.w-full.px-2.motion-safe:transition.lg:px-4")
# check_special_rates = driver.find_element(By.CLASS_NAME,"shop-form-btn btn.btn-lg relative.w-full.px-2.motion-safe:transition.lg:px-4")
# find_a_hotel = driver.find_element(By.CLASS_NAME,"shop-form-btn-submit btn.btn-lg w-full.px-4.motion-safe:transition.md:w-auto.md:flex-1").click()

base.selenium_end(driver)