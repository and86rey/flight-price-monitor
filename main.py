# main.py - Runs the flight price monitoring script

from fetch_flights import get_flights
from filter_flights import filter_flights

def main():
    print("Fetching flights...")
    flights = get_flights()

    if not flights:
        print("No flights found.")
        return
    
    print("Filtering flights...")
    valid_flights = filter_flights(flights)

    if valid_flights:
        print("\nEligible Flights:")
        for flight in valid_flights:
            print(f"From {flight['outbound']['origin']} to {flight['outbound']['destination']} - €{flight['price']}")
            print(f"Departure: {flight['outbound']['departure_time']}, Return: {flight['inbound']['departure_time']}")
            print("-" * 40)
    else:
        print("No flights meet the criteria.")

if __name__ == "__main__":
    main()
