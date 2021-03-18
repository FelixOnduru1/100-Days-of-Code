from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os

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
sheety_headers = {
    "Authorization": f"Basic {SHEETY_KEY}"
}


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
    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

