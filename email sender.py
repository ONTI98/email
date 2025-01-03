#this is a basic email sending script
#It has minimal security
#A lot has changed with regards to  Google security
#In order to usethis script you will need to make sure the following are in check:
#Ensure that Google that two-factor authentication is turned on
#Go to app passwords by interting ,"apppasswords" at the end of the link
#create a new app name (any name)
#click "create"
# A 16 -digit key passsword will be created. 
#Use this password to send emails




import smtplib
from email.message import EmailMessage  
import ssl  #secure sockets locks for extra security


#email handlers
sender = "leinaAno54@gmail.com"
receiver="Tjumpre@gmail.com"
password= "enter password obtained from app passwords"
subject=  ""
body= ""

#variable name change for ease of access

EM= EmailMessage()

#secure sockets
EM["from"] =sender
EM["to:"]
EM. set_content(subject)
EM.set_content(body) #contents housed in the email body

#Adding a security layer

sockets=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",port=465,context=sockets) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver, EM.as_string())
