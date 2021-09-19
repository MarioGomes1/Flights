# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

text_message = NotificationManager(twilio_phone_number='This is my nubmer')
text_message.send()

# data_manager = DataManager()
# search_data = data_manager.get_data()


# for flight in search_data:
#     # itirates through each row and passes it as argument(dict) to FlightSearch for the API call
#     available_flights = FlightSearch(flight).searchFlights()
#     # FlightData checks over the returned api call...add more notes
#     if len(available_flights) > 0:
#         FlightData(available_flights['data'])
