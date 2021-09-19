import json
import requests
sample_data = {'prices': [
    {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 1000, 'id': 2},
    {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 41000, 'id': 4},
    {'city': 'OSAKA', 'iataCode': 'ITM', 'lowestPrice': 1000, 'id': 6},
    {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 41000, 'id': 7},
    {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 21000, 'id': 8},
    {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 21000, 'id': 9},
    {'city': 'Sao Paulo', 'iataCode': 'SAO', 'lowestPrice': 31000, 'id': 10}]}


class DataManager:
    def __init__(self) -> dict:
        pass

    def get_data(self):
        # response = requests.get(
        #     "https://api.sheety.co/dce98772cf0b4c06ebaa731803518c2d/copyOfFlightDeals/prices")
        return sample_data["prices"]
        return response.json()
