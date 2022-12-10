import os
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content(input("Enter email message:\n"))

msg['Subject'] = input("Enter subject:\n")
msg['From'] = os.environ['Username']

msg['To'] = input("enter destination email address:\n")

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(os.environ['Username'], os.environ['App'])
server.send_message(msg)
server.quit()
