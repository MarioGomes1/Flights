# This class is responsible for structuring the flight data.

class FlightData:
    def __init__(self, flight_search_data) -> None:
        self.flights = flight_search_data
        self.city_from = ""
        self.city_to = ""
        self.country_from = ""
        self.country_to = ""
        self.clean_data()

    def clean_data(self):
        for flights in self.flights:
            self.city_from = flights["cityFrom"]
            self.city_to = flights["cityTo"]
            self.country_from = flights['countryFrom']['name']
            print(self.city_from)
            self.country_to = flights['countryTo']['name']
            print(self.city_to)
            print(self.country_from)
            print(self.country_to)
            print("--------------------------------------------------------")
            # it's printing 5 times because of the amount of flight limit currently in "FlightSearch.py"
