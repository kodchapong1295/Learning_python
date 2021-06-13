# import smtplib
#
# my_email = "best.testsmtp@gmail.com"
# password = "Best*1234"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="best.testsmtp@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# import datetime as dt
#
# #get data from datetime
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# #make datetime from scrach
# date_of_birth = dt.datetime(year= 2001, month= 6, day= 1)
# print(date_of_birth)

#------------ Challenge 1: Monday Motivation --------------------
import random
import smtplib
import datetime as dt

MY_EMAIL = "best.testsmtp@gmail.com"
MY_PASSWORD = "Best*1234"

now = dt.datetime.now()
weekday = now.weekday()
if(weekday==0):
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )