#!/bin/python

from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import requests
import smtplib

SMTP_SERVER = ''
SMTP_PORT = 587
SMTP_LOGIN = 'no-reply@valentin-deville.eu'
SMTP_PASSWORD = ''
TO_LIST = ['contact@valentin-deville.eu']


def alert_message():
    mail = MIMEText('Des serveurs dédiés LT 2017 sont disponibles https://www.online.net/fr/serveur-dedie/dedibox-lt')
    mail['Subject'] = 'DISPO LT2017 ONLINE.NET'
    mail['From'] = 'DISPONIBILITE ONLINE <no-reply@valentin-deville.eu>'
    s = smtplib.SMTP()
    s.connect(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(SMTP_LOGIN, SMTP_PASSWORD)
    s.sendmail(SMTP_LOGIN, TO_LIST, mail.as_string())
    s.quit()


res = requests.get('https://www.online.net/fr/serveur-dedie/dedibox-lt')
parsed_html = BeautifulSoup(res.content, "lxml")

button = parsed_html.find('button', attrs={'class': 'Orderbloc__submit btn btn--primary'})
try:
    stock = button['disabled']
    print("OUT OF STOCK")
except KeyError:
    print("STOCK OK")
    alert_message()

exit(0)
