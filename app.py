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

url = "ise.com/partner"
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

        email_sender = 'saaketh9616@gmail.com'
        email_password = 'ubglzrjydzemnhgt'
        email_receiver = 'howf163@gmail.com'


        subject = 'Status of ISE Partner Portal'
        body = """
        Partner Portal is not working
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

check_ise_partner_portal_status()
