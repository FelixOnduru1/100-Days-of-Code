import requests
import os
SHEETY_KEY = os.environ["SHEETY_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
headers = {
            "Authorization": f"Basic {SHEETY_KEY}"
        }
USERS_SHEETY_ENDPOINT = "https://api.sheety.co/7b44dd980a12b66468da9389dae95414/flightDeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                    "price": {
                        "iataCode": city["iataCode"],

                    }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",
                                    json=new_data,
                                    headers=headers)
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=USERS_SHEETY_ENDPOINT, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

