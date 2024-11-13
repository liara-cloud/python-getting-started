import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# # uncomment in development mode: 
# from dotenv import load_dotenv # pip install python-dotenv

# # Load environment variables from .env file
# load_dotenv()


# Read email configuration from environment variables
MAIL_HOST = os.getenv('MAIL_HOST')
MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
MAIL_USER = os.getenv('MAIL_USER')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_FROM_ADDRESS = os.getenv('MAIL_FROM_ADDRESS')

def send_email(to_address, subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = MAIL_FROM_ADDRESS
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(MAIL_HOST, MAIL_PORT)
        server.starttls()  # Secure the connection with TLS
        server.login(MAIL_USER, MAIL_PASSWORD)  # Login to the SMTP server
        server.send_message(msg)  # Send the email
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", e)
    finally:
        server.quit()  # Close the connection to the server

# Send an email to the specified recipient
to_address = 'recipient@example.com'
subject = 'Test Email'
body = 'This is a test email sent from Python using environment variables.'

send_email(to_address, subject, body)
