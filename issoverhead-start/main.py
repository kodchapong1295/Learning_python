import time

import requests
from datetime import datetime
import smtplib
import math

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
MY_EMAIL = "best.testsmtp@gmail.com"
MY_PASSWORD = "Best*1234"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (math.fabs(MY_LAT - iss_latitude) <= 5 and math.fabs(MY_LONG - iss_longitude) <= 5):
        return True

    # if(time_now<sunrise or time_now>sunset):
    #     print("dark")
    #     if(math.fabs(MY_LAT-iss_latitude) <=5 and math.fabs(MY_LONG-iss_longitude) <=5):
    #         with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #             connection.starttls()
    #             connection.login(MY_EMAIL, MY_PASSWORD)
    #             connection.sendmail(
    #                 from_addr=MY_EMAIL,
    #                 to_addrs=MY_EMAIL,
    #                 msg="Reminder\n\nlook up for iss now"
    #             )
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if (time_now <= sunrise or time_now >= sunset):
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject: Look Up\n\nThe ISS is above you in the sky."
                )
                break

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




