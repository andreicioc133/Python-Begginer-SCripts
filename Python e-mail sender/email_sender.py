import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 


html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "andrei Cioc"
email["to"] = "andrei@zerotomastery.io" 
email['subject'] = "You won 1,000,000 dollars!"

email.set_content(html.substitute({"name" : "tintin"}), "html")

with smtplib.SMTP(host = "smtp.gmail.com" , port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login("dummyandrei123@gmail.com" , "dummy134")
	smtp.send_message(email)
	print("all good boss!")

