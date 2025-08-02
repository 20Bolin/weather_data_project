import requests
api_key = "a4ac9fc95286747d01950990b228e1ff"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching data from Weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully.")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        raise

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-07-02 05:21', 'localtime_epoch': 1751433660, 'utc_offset': '-4.0'}, 'current': {'observation_time': '09:21 AM', 'temperature': 22, 'weather_code': 143, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png'], 'weather_descriptions': ['Mist'], 'astro': {'sunrise': '05:30 AM', 'sunset': '08:31 PM', 'moonrise': '01:05 PM', 'moonset': '12:16 AM', 'moon_phase': 'First Quarter', 'moon_illumination': 42}, 'air_quality': {'co': '492.1', 'no2': '57.165', 'o3': '53', 'so2': '13.875', 'pm2_5': '16.465', 'pm10': '16.65', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 10, 'wind_degree': 263, 'wind_dir': 'W', 'pressure': 1012, 'precip': 0, 'humidity': 94, 'cloudcover': 50, 'feelslike': 25, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}