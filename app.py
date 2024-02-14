from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
import smtplib
import ssl
from email.message import EmailMessage

useremail = "saaketh9616@gmail.com"
password = "Cristiano@cr7"


def send_email(body):

    email_sender = 'saaketh9616@gmail.com'
    email_password = 'ubglzrjydzemnhgt'
    email_receiver = 'howf163@gmail.com'
    subject = 'Status of ISE Partner Portal'
    # body = """
    
    # """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

        # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def check_ise_partner_portal_status():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://ise.cisco.com/partner")
    time.sleep(5)
    driver.find_element(By.ID,"idp-discovery-username").send_keys(useremail)
    time.sleep(5)
    element1 = driver.find_element(By.ID,"idp-discovery-submit")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(5)
    driver.find_element(By.ID,"okta-signin-password").send_keys(password)
    time.sleep(5)
    element2 = driver.find_element(By.ID,"okta-signin-submit")
    driver.execute_script("arguments[0].click();", element2)
    time.sleep(30)

    def feed_server_header_exists():
        try:
            driver.find_element(By.CSS_SELECTOR,"div.regHeader15")
        except NoSuchElementException:
            return False
        return True

    if feed_server_header_exists:
        print("Partner Portal is working")
        driver.get("https://ise.cisco.com/partner/#pageId=com_cisco_fsm_download_offline_update_page")
        time.sleep(20)

        def generate_button_exists():
            try:
                driver.find_element(By.ID,"generateBtn")
            except NoSuchElementException:
                return False
            return True

        if generate_button_exists:
            print("Generate Package is working")
            driver.find_element(By.ID,"generateBtn").click()
            time.sleep(10)
        else:
            print("Generate Package not avaiialbe")
            send_email("Generate Package is not working")

        def download_button_exists():
            try:
                driver.find_element(By.ID,"downloadBtn")
            except NoSuchElementException:
                return False
            return True

        # if download_button_exists:
        #     # driver.find_element(By.ID,"downloadBtn").click()
        #     time.sleep(10)
        if not download_button_exists:
            print("Download Package not avaiialbe")
        
        # while True:
            # pass
    else:
        print("Partner Portal is not working")
        send_email("Partner Portal is not working")

        

check_ise_partner_portal_status()
