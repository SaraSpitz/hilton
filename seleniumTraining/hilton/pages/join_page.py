from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class joinPage():

    def __init__(self,driver):
        self.driver = driver

    def join_new_user(self, example_first_name, example_last_name, example_index_phone_number,example_phone_number ):
        # join = self.driver.find_element(By.CLASS_NAME,"h-fit")
        # join.click()
        # print

        first_name = self.driver.find_element(By.NAME,"name.firstName")
        first_name.click()
        first_name.send_keys(example_first_name)

        last_name = self.driver.find_element(By.NAME,"name.lastName")
        last_name.click()
        last_name.send_keys(example_last_name)

        dropdown_phone_country = self.driver.find_element(By.NAME,"phone.phoneCountry")
        phone_country = Select(dropdown_phone_country)
        phone_country.select_by_index(1)

        phone_number = self.driver.find_element(By.NAME,"phone.phoneNumber")
        phone_number.click()
        phone_number.send_keys(example_phone_number)



