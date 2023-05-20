from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'araizzahid45@gmail.com'
email_password = 'cmyrdvmsiredurlo'
email_reciever = 'bowof72334@carpetra.com'
email_subject = 'Please help !'
email_body = """
Hello Friends,

I am glad to see you in this place, 
from here your test has been started from the beginning of the china to end of russia



"""

email_message = EmailMessage()
email_message['From'] = email_sender
email_message['To'] = email_reciever
email_message['subject'] = email_subject
email_message.set_content(email_body)

ssl_context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl_context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, email_message.as_string())