from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import smtplib
import ssl
from email.message import EmailMessage
import pytest

useremail = "saaketh9616@gmail.com"
password = "Cristiano@cr7"

def generate_package(driver):
            
    driver.get("https://ise.cisco.com/partner/#pageId=com_cisco_fsm_download_offline_update_page")
    time.sleep(20)
            
    def generate_button_exists():
        try:
            driver.find_element(By.ID,"generateBtn")
            time.sleep(40)
        except NoSuchElementException:
            return 0
        return 1

    return generate_button_exists
        
def download_button_exists(driver):
    try:
        driver.find_element(By.ID,"downloadBtn")
    except NoSuchElementException:
        return False
    return True

def post_login_check(driver,number_of_reloads):
    
    def feed_server_header_exists():
        try:
            driver.find_element(By.XPATH,'//div[@title="Self/Saaketh Madabhushi"]')
        except NoSuchElementException:
            return False
        return True

    if feed_server_header_exists and driver.current_url == "https://ise.cisco.com/partner/#pageId=com_cisco_fsm_home_page":
        print("Partner Portal is working after ",end = '')
        print(number_of_reloads,end = ' ')
        print("number of reloads post login")

        number_of_attempts = 5
        generate_package_worked = 0

        for i in range(1,number_of_attempts + 1):
            current_attempt = generate_package(driver)
        
            if current_attempt:
                generate_package_worked = 1  
                driver.find_element(By.ID,"generateBtn").click()
                time.sleep(20)      
                if not download_button_exists and i == number_of_attempts:
                    print("Download Package not available")
                else:
                    print("Generate package is working on attempt ",end = '')
                    print(i)
                break
        
        if not generate_package_worked:
            print("Generate Package not working")
            pytest.fail("Generate Package not working")
    
    else:
        if number_of_reloads >= 3:
            print("Partner Portal is not working")
            pytest.fail("Partner Portal is not working")
            return 0
        else:
            driver.get("https:ise.cisco.com/partner")
            time.sleep(30)
            post_login_check(driver,number_of_reloads + 1)


def test_ise_partner_portal_status():

    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://ise.cisco.com/partner")
    except Exception:
        pytest.fail("Partner Portal is not loading")
    time.sleep(5)
    
    if str(driver.current_url).startswith('https://id.cisco.com/'):
        try:
            driver.find_element(By.ID,"input28").send_keys(useremail)
        except NoSuchElementException:
            pytest.fail("Login Page is not loaded")
    
    else:
        pytest.fail('Login Page is not loaded')

    driver.find_element(By.ID,"input28").send_keys(Keys.RETURN)
    time.sleep(8)

    try:
        driver.find_element(By.ID,"input64").send_keys(password)
    except NoSuchElementException:
        print("Next button has not redirected to Login Page")
        pytest.fail("Next button has not redirected to Login Page")
    
    driver.find_element(By.ID,"input64").send_keys(Keys.RETURN)
    time.sleep(5)

    if driver.current_url == "https://id.cisco.com/signin":
        print("Login button has not redirected to partner portal")
        pytest.fail("Login button has not redirected to partner portal")

    time.sleep(30)

    count_of_reloads = 0
    post_login_check(driver,0)
    assert True
