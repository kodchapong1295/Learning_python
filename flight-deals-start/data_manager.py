import requests

SHEET_ENDPOINT = "https://api.sheety.co/302424d51f43453377ceccb76743d6d4/flightDeals/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in (self.destination_data):
            SHEET_PUT_ENDPOINT = f"{SHEET_ENDPOINT}/{city['id']}"
            new_data = {
                "price": {
                    "iataCode": "TESTING"
                }
            }
            response = requests.put(SHEET_PUT_ENDPOINT, json=new_data)
            print(response.text)


