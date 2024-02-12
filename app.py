from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time

useremail = "saaketh9616@gmail.com"
password = "Cristiano@cr7"

url = "ise.com/partner"
def func():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://ise.cisco.com/partner")
    time.sleep(5)
    driver.find_element(By.ID,"idp-discovery-username").send_keys(useremail)
    driver.find_element(By.ID,"idp-discovery-submit").click()
    time.sleep(5)
    driver.find_element(By.ID,"okta-signin-password").send_keys(password)
    driver.find_element(By.ID,"okta-signin-submit").click()
    time.sleep(5)
    def element_exists():
        try:
            driver.find_element(By.CSS_SELECTOR,"div.regHeader15")
        except NoSuchElementException:
            return False
        return True

    
    if element_exists:
        print("Partner Portal is working")
    else:
        print("Partner Portal is not working")

func()
