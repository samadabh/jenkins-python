from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
import smtplib
import ssl
from email.message import EmailMessage

useremail = "saaketh89@gmail.com"
password = "Cristiano@cr7"

def send_email(body,screenshot):

    email_sender = 'saaketh9616@gmail.com'
    email_password = 'ubglzrjydzemnhgt'
    email_receiver = 'howf163@gmail.com'
    subject = 'Status of ISE Partner Portal'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    em.add_attachment(screenshot,maintype='image',subtype='png')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def generate_package(driver):
            
    driver.get("https://ise.cisco.com/partner/#pageId=com_cisco_fsm_download_offline_update_page")
    time.sleep(20)
            
    def generate_button_exists():
        try:
            driver.find_element(By.ID,"generateBtn")
            print("Generate Package is working")
            driver.find_element(By.ID,"generateBtn").click()
            time.sleep(10)
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

def check_ise_partner_portal_status():

    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get("https://ise.cisco.com/partner")
    time.sleep(5)
    
    driver.find_element(By.ID,"idp-discovery-username").send_keys(useremail)
    time.sleep(5)
    
    next_button = driver.find_element(By.ID,"idp-discovery-submit")
    driver.execute_script("arguments[0].click();", next_button)
    time.sleep(5)

    try:
        driver.find_element(By.ID,"okta-signin-password").send_keys(password)
    except NoSuchElementException:
        print("Next button has not redirected to Login Page")
        screenshot = driver.get_screenshot_as_png()
        send_email("Next button has not redirected to Login Page",screenshot)
        return 0
    
    login_button = driver.find_element(By.ID,"okta-signin-submit")
    driver.execute_script("arguments[0].click();", login_button)
    time.sleep(5)


    if driver.current_url == "https://id.cisco.com/signin":
        print("Login did not work")
        screenshot = driver.get_screenshot_as_png()
        send_email("Login button has not redirected to partner portal",screenshot)
        return 0

    time.sleep(45)

    def feed_server_header_exists():
        try:
            driver.find_element(By.XPATH,'//div[@title="Self/Saaketh Madabhushi"]')
        except NoSuchElementException:
            return False
        return True

    if feed_server_header_exists and driver.current_url == "https://ise.cisco.com/partner/#pageId=com_cisco_fsm_home_page":
        print("Partner Portal is working")

        number_of_attempts = 5
        generate_package_worked = 0

        for i in range(1,number_of_attempts + 1):
            current_attempt = generate_package(driver)
        
            if current_attempt:
                print("Generate package is working on attempt ",end = '')
                print(i)
                generate_package_worked = 1        
                if not download_button_exists:
                    print("Download Package not available")
                break
        
        if not generate_package_worked:
            print("Generate Package not working")
            screenshot = driver.get_screenshot_as_png()
            send_email("Generate Package is not working",screenshot)
        
    else:
        print("Partner Portal is not working")
        screenshot = driver.get_screenshot_as_png()
        send_email("Partner Portal is not working",screenshot)

        

check_ise_partner_portal_status()
