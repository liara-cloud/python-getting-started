import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# # uncomment in development mode: 
# from dotenv import load_dotenv # pip install dotenv
# load_dotenv()

MAIL_HOST = os.getenv('MAIL_HOST')
MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
MAIL_USER = os.getenv('MAIL_USER')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_FROM_ADDRESS = os.getenv('MAIL_FROM_ADDRESS')

def send_email(to_address, subject, body):
    msg = MIMEMultipart()
    msg['From'] = MAIL_FROM_ADDRESS
    msg['To'] = to_address
    msg['Subject'] = subject
    # msg['CC'] = 'test.one@example.com, test.two@example.com'
    # msg['BCC'] = 'test.three@example.com,'
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(MAIL_HOST, MAIL_PORT)
        server.starttls()  
        server.login(MAIL_USER, MAIL_PASSWORD)  
        server.send_message(msg)  
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", e)
    finally:
        server.quit() 

to_address = 'test@example.com'
subject    = 'Test Email'
body       = 'This is a test email sent from Python using environment variables.'

send_email(to_address, subject, body)
