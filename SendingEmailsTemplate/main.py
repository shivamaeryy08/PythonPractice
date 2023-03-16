# SMTP is simple mail transfer protocol and is usewd ot send emails bet the email server services

import smtplib
import datetime as dt
import random
import os
from config import *

dob = dt.datetime(year=2001, month=9, day=4, hour=7)
now = dob.now()
if now.weekday() == 6:
    with open('quotes.txt') as file:
        quotes = file.readlines()
        text_list = [quote.rstrip('\n') for quote in quotes]
        text = random.choice(text_list)

    test_email = os.environ['email']
    password = os.environ['password']
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        # connection.starttls()  # tls is way of securing connection to email server so no one can intercept
        connection.login(user=test_email, password=password)
        connection.sendmail(from_addr=test_email, to_addrs=test_email,
                            msg=f"Subject:Motivational Quote Sunday\n\n{text}", )
