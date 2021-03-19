from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os
import requests

ORIGIN_CITY_IATA = "LON"

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

TEQUILA_API_KEY = os.environ['TEQUILA_API_KEY']
TEQUILA_LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
tequila_headers = {
    "apikey": TEQUILA_API_KEY
}

SHEETY_KEY = os.environ["SHEETY_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
USERS_SHEETY_ENDPOINT = "https://api.sheety.co/7b44dd980a12b66468da9389dae95414/flightDeals/users"
sheety_headers = {
    "Authorization": f"Basic {SHEETY_KEY}"
}

print("Welcome to the Flight Club.\nWe find the best flight and email you.")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_confirm = input("Type your email again:\n")

new_user_parameters = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}

if email == email_confirm:
    print("You're in the club!!")
    user_update = requests.post(url=USERS_SHEETY_ENDPOINT, json=new_user_parameters, headers=sheety_headers)
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    if sheet_data[0]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in sheet_data:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        if flight is None:
            continue
        if flight.price < destination["lowestPrice"]:
            users = data_manager.get_customer_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]

            message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            notification_manager.send_sms(
                message=message
            )
            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
                   f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

            notification_manager.send_emails(emails=emails, message=message, google_flight_link=link)
else:
    print("The emails do not match.")
