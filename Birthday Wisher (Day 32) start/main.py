import smtplib

my_email = "best.testsmtp@gmail.com"
password = "Best*1234"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="best.testsmtp@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )