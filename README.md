# flight-price-monitor
# Flight Price Monitor  

A simple script to monitor commercial flight prices for same-day round trips from Berlin to any EU destination.  

## ✈️ Features  
- Finds flights departing from **Berlin (BER)** before **10:00 AM**  
- Ensures return flight is the **same day before 8:00 PM**  
- Filters trips that cost **≤ 100 EUR**  
- Ensures minimum **5 hours** at the destination  

## 🔧 Setup & Usage (GitHub Web Version)  
1. Add your **API Key** in `config.py`.  
2. Run the script using an online Python executor or GitHub Actions.  
3. Check filtered flight results in the output.  

## 📂 File Structure  
- `config.py` → Stores API key & flight search parameters  
- `fetch_flights.py` → Fetches flight data from API  
- `filter_flights.py` → Filters flights based on conditions  
- `main.py` → Runs the script and displays results  
- `requirements.txt` → Lists dependencies  

## 🚀 Future Improvements  
- Automate via GitHub Actions  
- Add email notifications  
- Integrate with a web dashboard  

---

✉️ Created by **[Your GitHub Username]**  
