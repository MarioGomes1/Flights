# This class is responsible for talking to the Flight Search API.
import requests
from decouple import config
from datetime import date
import json

today = date.today().strftime("%d/%m/%Y")
FLIGHT_SEARCH_API = config('FLIGHT_SEARCH_API')


class FlightSearch:
    def __init__(self, search_obj, from_date=today) -> dict:
        self.search = search_obj

    def searchFlights(self):
        API_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        header = {
            "apikey": FLIGHT_SEARCH_API
        }
        booking_token = {
            "fly_from": "CHS",
            "fly_to": self.search['iataCode'],
            # dateFrom-dateTo are the departure window
            "dateFrom": today,
            "dataTo": "25/12/2021",  # dateFrom-dateTo are the departure window
            # min return date of the whole trip (dd/mm/yyyy)
            # "return_from": "",
            # max return date of the whole trip (dd/mm/yyyy)
            # "return_to": "",
            # the minimal length of stay in the destination given in the fly_to parameter.
            "nights_in_dst_from": 4,
            "nights_in_dst_to": 10,
            "curr": "USD",
            "price_to": self.search["lowestPrice"],
            "limit": 5
            # "flight_type": "round"

        }
        response = requests.get(
            url=API_ENDPOINT, headers=header, params=booking_token)
        return response.json()
        with open('flight_data.txt', 'w') as file:
            file.write(json.dumps(response.json()))


# search flights from this date (dd/mm/yyyy). Use parameters date_from and date_to as a date range for the flight departure.
# Parameters 'date_from=01/04/2021' and 'date_to=01/04/2021' mean that the departure can be anytime between the specified dates.
# For the dates of the return flights, use the 'return_to' and 'return_from' or 'nights_in_dst_from' and 'nights_in_dst_to' parameters.
