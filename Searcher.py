from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
import os


class DolarSearcher:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_driver_path = os.enciron.get("CHROME_DRIVER_PATH")

        self.driver = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout= 10,
            poll_frequency= 1,
            ignored_exceptions= [
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ]
        )
        self.dolarPrice = 0

    def Start(self):
        # openning link
        try:
            self.driver.get("https://www.google.com/search?rlz=1C1GCEU_pt-BRPT920PT920&ei=y_OFX9KLJcTMgweisqho&q=dolar+real&oq=dolar+real&gs_lcp=CgZwc3ktYWIQAzIHCAAQRhCCAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECAAQR1DFCVjBDWDWD2gAcAF4AIABVIgB7QGSAQEzmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwiSnZaam7LsAhVE5uAKHSIZCg0Q4dUDCA0&uact=5")
            self.wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,'//input[@type="number"]')))

            # getting dolar price
            NotFormatedDolar = self.GetPrice()
            
            # formating price
            self.dolarPrice = self.PriceFormater(NotFormatedDolar)
        
        except:
            print("could not reach the page")
        
    def PriceFormater(self,price):
        formatted = price.replace(",",".")
        return float(formatted)

    def GetPrice(self):
        sleep(2)
        price = 0
        try:
            return self.driver.find_element_by_class_name("DFlfde.SwHCTb").text
        except:
            print("could not reach the element of price")