# fetch_flights.py - Fetch flight data from API

import requests
import config

def get_flights():
    params = {
        "apiKey": config.API_KEY,
        "origin": config.DEPARTURE_AIRPORT,
        "destinationRegion": config.DESTINATION_REGION,
        "maxPrice": config.MAX_PRICE,
        "departureTimeFrom": config.EARLIEST_DEPARTURE,
        "departureTimeTo": config.LATEST_DEPARTURE,
        "returnTimeTo": config.LATEST_RETURN,
        "currency": "EUR"
    }

    response = requests.get(config.FLIGHT_API_URL, params=params)
    
    if response.status_code == 200:
        return response.json().get("flights", [])
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

if __name__ == "__main__":
    flights = get_flights()
    print(flights)  # For testing
