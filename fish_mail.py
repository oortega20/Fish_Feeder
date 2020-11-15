import smtplib, ssl
import emoji
import sys
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.path.append('/home/pi/Desktop/.info')

from info import retrieve_info


port = 465
email, password = retrieve_info('gmail')
sender_email, receiver_email = email, email
num_fish = 20

message = MIMEMultipart("alternative")
message["Subject"] = "Fish Feeder v.0.0.1 copyright 2020"
message["From"] = sender_email
message["To"] = receiver_email


text = ''

for _ in range(num_fish):
    text += emoji.emojize(':fish:')
text += """\n\n
Hi Oscar, 
This is your daily reminder to feed your fish.


Stats:
Ammonia : N/A
Nitrite : N/A
Nitrate : N/A
Ph      : N/A

Please note that Fish Feeder Program v.0.0.1 is in beta.
Future versions will include vital fish stats + feeding.
\n
"""
for _ in range(num_fish):
    text += emoji.emojize(':fish:')


text = MIMEText(text, 'plain')
message.attach(text)

while True:
    with smtplib.SMTP_SSL('smtp.gmail.com', port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    time.sleep(86400)
