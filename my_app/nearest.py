from time import sleep
import pandas as pd
import selenium
from selenium import webdriver


class nearest_5:
    def __init__(self,latitude,longitude):
        # self.driver = self.web_driver()
        # self.driver1 = self.web_driver()
        print("driver load")
        self.latitude = latitude
        self.longitude = longitude
        # self.latitude = 28.63388895172476 
        # self.longitude = 77.19895700656642

    def web_driver(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--verbose")
        # options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--window-size=1920,1200')
        # options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()
        return driver

    def test(self):
        print("hello")
        return "hello"
    def main_fun(self):
        link = "https://www.google.co.in/maps"
        self.driver.get(link)
        print("driver",self.driver)

        try:

            input_search = self.driver.find_element('id','searchboxinput')
            search_button = self.driver.find_element('xpath',"(//button[@id='searchbox-searchbutton'])[1]")

            user_search = f"{self.latitude},{self.longitude}"
            input_search.send_keys(user_search)
            sleep(1)
            search_button.click()
            sleep(2)
            top = self.driver.find_elements('xpath',"(//span[@class='DkEaL'])")
            new_search=top[1].text
            input_search.clear()
            sleep(1)
            user_search = "cake shop in {x}".format(x =f"{new_search}")
            input_search.send_keys(user_search)
            sleep(1)
            search_button.click()
            sleep(2)

            final_info = []

            top = self.driver.find_elements('xpath',"(//a[@class='hfpxzc'])")
            print("top",top)
            links = []
            for i in top[0:4]:
                single_link = i.get_attribute("href")
                links.append(single_link)
            self.driver.quit()
            for single_link in links:
                location_info = []
                driver1 = self.web_driver()
                driver1.get(single_link)
                h1=self.driver1.find_element("tag name", "h1")
                locate = self.driver1.find_elements('xpath',"(//div[@class='Io6YTe fontBodyMedium kR99db '])")
                location_info.append(h1.text)
                # for i in locate:
                #     location_info.append(i.text)
                location_info.append(locate[0].text)
                # location_info.append(locate[1].text)
                final_info.append(location_info)
                print(final_info)
                sleep(3)
            return final_info
        finally:
            # self.driver.quit()
            driver1.quit()

    

    
