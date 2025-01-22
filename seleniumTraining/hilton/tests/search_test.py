import re
import time

from seleniumTraining.hilton.pages.welcom_page import welcomePage
from seleniumTraining.hilton.tests.selenuimBaseHilton import seleniumBaseHilton

class WelcomePage:
    base = seleniumBaseHilton()
    driver = base.selenium_start()
    welcome_page = welcomePage(driver)

    driver.get("https://www.hilton.com/en/")
    welcome_page.search("Miami")
    price_first_hotel = welcome_page.price()

    driver.get("https://www.hilton.com/en/")
    time.sleep(3)
    welcome_page.search("Tel Aviv")
    price_second_hotel = welcome_page.price()

    price_first_hotel_int = int(re.sub(r'\D', '', price_first_hotel))
    price_second_hotel_int = int(re.sub(r'\D', '', price_second_hotel))

    # assert price_second_hotel_int > price_first_hotel_int,"A vacation in Miami is more expensive than a vacation in Tel Aviv"
    # assert price_second_hotel_int < price_first_hotel_int, "A vacation in Tel Aviv is more expensive than a vacation in Miami "
    # assert price_second_hotel_int == price_first_hotel_int, "A vacation in Tel Aviv costs the same as a vacation in Miami"


    if price_second_hotel_int > price_first_hotel_int:
        print("A vacation in Tel Aviv is more expensive than a vacation in Miami.")
    elif price_second_hotel_int < price_first_hotel_int:
        print("A vacation in Miami is more expensive than a vacation in Tel Aviv.")
    else:
        print("A vacation in Tel Aviv costs the same as a vacation in Miami.")

    driver.quit()


