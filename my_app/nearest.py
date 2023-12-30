from time import sleep
import pandas as pd
import selenium
from selenium import webdriver


class nearest_5:
    def __init__(self,latitude,longitude):
        self.driver = self.web_driver()
        self.driver1 = self.web_driver()
        self.latitude = latitude
        self.longitude = longitude

    def web_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1200')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        return driver

    
    def main_fun(self):
        link = "https://www.google.co.in/maps"
        self.driver.get(link)
        print("driver",self.driver)

        input_search = self.driver.find_element('id','searchboxinput')
        search_button = self.driver.find_element('xpath',"(//button[@id='searchbox-searchbutton'])[1]")

        user_search = f"{self.latitude},{self.longitude} cake shop"
        input_search.send_keys(user_search)
        sleep(1)
        search_button.click()
        sleep(2)

        final_info = []

        top = self.driver.find_elements('xpath',"(//a[@class='hfpxzc'])")
        print("top",top)
        for i in top[0:5]:
            location_info = []
            single_link = i.get_attribute("href")
            self.driver1.get(single_link)
            h1=self.driver1.find_element("tag name", "h1")
            locate = self.driver1.find_elements('xpath',"(//div[@class='Io6YTe fontBodyMedium kR99db '])")
            location_info.append(h1.text)
            for i in locate:
                location_info.append(i.text)
            final_info.append(location_info)
            #   print(final_info)
            sleep(3)
        return final_info

    

    
