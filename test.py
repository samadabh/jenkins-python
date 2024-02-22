import smtplib
import ssl
from email.message import EmailMessage

def send_email(body):

    email_sender = 'saaketh9616@gmail.com'
    email_password = 'ubglzrjydzemnhgt'
    email_receiver = 'saaketh89@gmail.com'
    email_receiver2 = 'howf163@gmail.com'
    subject = 'Testing scripts'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_sender, email_password)
        server.sendmail(
            email_sender,
            email_receiver,
            body
        )
        server.quit()



send_email("Testing scripts")
