import requests
import os
from pprint import pprint
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

sheety_get_endpoint = "YOUR_SHEETY_ENDPOINT"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._token = os.environ["TOKEN"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.header = {
        "Authorization": f"Basic {self._token}"
        }  

    def get_destination_data(self):
        response = requests.get(url=sheety_get_endpoint, headers=self.header)
        data = response.json()
        # pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {"iataCode": city["iataCode"]}
            }
            response = requests.put(f"{sheety_get_endpoint}/{city['id']}", json=new_data, headers=self.header)
            print(response.text)