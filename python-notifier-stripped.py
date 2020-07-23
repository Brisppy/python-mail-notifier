# Takes the following arguments: smtp_server, smtp_port, user_address, user_password, sendto_address, subject, body
import smtplib
import ssl
import sys
from email.mime.text import MIMEText

context = ssl.create_default_context()
try:
	server = smtplib.SMTP(sys.argv[1], sys.argv[2])
	server.starttls(context=context)
	server.login(sys.argv[3], sys.argv[4])
	message = MIMEText(sys.argv[7])
	message['Subject'] = sys.argv[6]
	message['From'] = sys.argv[3]
	message['To'] = sys.argv[5]
	server.sendmail(sys.argv[3], sys.argv[5], message.as_string())
except Exception as e:
	print(e)
finally:
	server.quit
