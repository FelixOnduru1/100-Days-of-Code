import requests
import os
from flight_data import FlightData
TEQUILA_API_KEY = os.environ['TEQUILA_API_KEY']
TEQUILA_LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
headers = {"apikey": TEQUILA_API_KEY}


class FlightSearch:


    def get_destination_code(self, city_name):

        location_endpoint = TEQUILA_LOCATION_ENDPOINT
        parameters = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint,
                                params=parameters,
                                headers=headers)
        data = response.json()["locations"]
        code = data[0]["code"]
        return code

    def check_flights(self, origin_city_code,
                     destination_city_code,
                     from_time,
                     to_time):
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "dates_from": from_time.strftime("%d/%m/%Y"),
            "dates_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0,
            "one_for_city": 1
        }

        response = requests.get(url=TEQUILA_FLIGHT_ENDPOINT,
                                        params=parameters,
                                        headers=headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
