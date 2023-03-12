import smtplib
import datetime as dt
import random
import pandas
from config import *
import os

data = pandas.read_csv('birthdays.csv')


def get_emails_send_to():
    random_date = dt.datetime(year=2001, month=2, day=3)
    now = random_date.now()
    cur_day = now.day
    cur_month = now.month
    queried_df = data[(data['month'] == cur_month) & (data['day'] == cur_day)]
    emails_to_send_to = queried_df['email'].to_list()
    return emails_to_send_to


def letter_contents():
    letter_names = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
    letter = random.choice(letter_names)
    with open(f'./letter_templates/{letter}', 'r+') as file:
        contents = file.read()
    return contents


def send_email(recipients, text):
    test_email = "shivamaeryy08@gmail.com"
    prev_email = recipients[0]
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=test_email, password=os.getenv('password'))
        for email in recipients:
            if email == prev_email:
                text = text.replace('[NAME]', email.split('@')[0])
                connection.sendmail(from_addr=test_email, to_addrs=email,
                                    msg=f"Subject:Happy Birthday\n\n{text}", )
            else:
                text = text.replace(prev_email.split('@')[0], email.split('@')[0])
                connection.sendmail(from_addr=test_email, to_addrs=email,
                                    msg=f"Subject:Happy Birthday\n\n{text}", )
                prev_email = email


emails = get_emails_send_to()
letter_to_send = letter_contents()
send_email(emails, letter_to_send)
