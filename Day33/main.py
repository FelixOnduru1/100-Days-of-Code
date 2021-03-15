import requests
import smtplib
from datetime import datetime

MY_EMAIL = "pythonsmtp404@gmail.com"
PASSWORD = "EAUybinT3Dwespr"
MY_LAT = -1.276410
MY_LNG = 36.904331


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    position = data["iss_position"]
    iss_latitude = float(position["latitude"])
    iss_longitude = float(position["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG+5 <= iss_longitude <= MY_LNG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_data = response.json()
    sunrise_hr = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hr = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    now_hr = datetime.now().hour
    if sunrise_hr >= now_hr >= sunset_hr:
        return True


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:LOOK UP!!!\n\nThe ISS is passing over you.."
                            )
