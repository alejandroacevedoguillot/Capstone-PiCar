import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
from time import sleep
#account info
sleep(35)
to = 'your_email@gmail.com' #Fill in your_email@gmail.com with your actual gmail account
gmail_user = 'your_email@gmail.com' #Fill in your_email@gmail.com with your actual gmail account
gmail_password = 'your_password!' #Fill in your_password with the appropriate password of your gmail account
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data=p.communicate()
split_data=data[0].split()
ipaddr=split_data[split_data.index('src')+1]
my_ip='Good day human overlord. This is your humble pi. My ip today is %s' % ipaddr
msg=MIMEText(my_ip)
msg['Subject']= 'RPi4 Reporting in!'
msg['From']= gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
