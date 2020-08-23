import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def mail():
        os.system('sudo rm -r photo.jpg')
        os.system('raspistill -o photo.jpg')
        email_user='Your gmail'
        email_send=('the reciever mail')
        subject='Hall Agent'

        msg=MIMEMultipart()
        msg['From']=email_user
        msg['To']=email_send
        msg['Subject']=subject

        body='Hi Boss, Your Home is under attack!'
        msg.attach(MIMEText(body,'plain'))

        filename='image.jpg'
        attachment=open(filename,'rb')

        part =MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text=msg.as_string()
        server =smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,'your password')

        server.sendmail(email_user,email_send,text)
        server.quit()
mail()
