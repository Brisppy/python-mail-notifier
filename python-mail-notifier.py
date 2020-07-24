# Takes the following arguments: smtp_server, smtp_port, user_address, user_password, sendto_address, subject, body
import smtplib
import ssl
import sys
from email.mime.text import MIMEText

# Set the number of attempts to make
retrycount = 10
timeout_secs = 10

context = ssl.create_default_context()
for i in range(1, retrycount):
	try:
		print("Attempt", i)
		server = smtplib.SMTP(sys.argv[1], sys.argv[2], timeout=timeout_secs)
		server.starttls(context=context)
		# server.set_debuglevel(1) # Uncomment to view SMTP communication.
		server.login(sys.argv[3], sys.argv[4])
		message = MIMEText(sys.argv[7])
		message['Subject'] = sys.argv[6]
		message['From'] = sys.argv[3]
		message['To'] = sys.argv[5]
		server.sendmail(sys.argv[3], sys.argv[5], message.as_string())
	except smtplib.SMTPException as e:
		print(e)
		break
	except smtplib.socket.error as e:
		print(e)
		continue
	else:
		server.quit
		break
