import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('index.html').read_text())
email = EmailMessage()
email['from']='Sornodeep Chandra'
email['to']='sornodeep91@gmail.com'
email['subject']='Be aware of CLICK-BAITS'

email.set_content(html.substitute({'name':'Blacky'}), 'html')

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('****************','*************')
	smtp.send_message(email)
	print("Everything amazing..")
