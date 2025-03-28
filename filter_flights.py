# filter_flights.py - Filters flights based on conditions

import config
from fetch_flights import get_flights

def filter_flights(flights):
    valid_flights = []
    
    for flight in flights:
        outbound = flight["outbound"]
        inbound = flight["inbound"]
        
        departure_time = int(outbound["departure_time"][:2])  # Extract hour
        return_time = int(inbound["departure_time"][:2])  # Extract hour
        arrival_time = int(inbound["arrival_time"][:2])  # Extract hour
        
        time_at_destination = return_time - arrival_time  # Hours at destination
        
        if (departure_time <= int(config.LATEST_DEPARTURE[:2]) and
            return_time <= int(config.LATEST_RETURN[:2]) and
            time_at_destination >= config.MIN_DESTINATION_TIME):
            valid_flights.append(flight)
    
    return valid_flights

if __name__ == "__main__":
    flights = get_flights()
    filtered = filter_flights(flights)
    print(filtered)  # For testing
