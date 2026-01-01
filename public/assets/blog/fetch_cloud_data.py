"""
Fetch Cloud Cover Data from Open-Meteo API

This script downloads historical cloud cover data for any location.
Customize the parameters below for your city and date range.

Requirements:
    pip install openmeteo-requests requests-cache retry-requests pandas
"""

import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Configure your location and date range
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 51.1,           # Wrocław, Poland latitude
    "longitude": 17.0333,       # Wrocław, Poland longitude
    "hourly": ["cloud_cover", "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high"],
    "timezone": "auto",
    "start_date": "2000-01-01",  # Adjust your start date
    "end_date": "2025-12-31",    # Adjust your end date
}

print("Fetching cloud cover data...")
print(f"Location: {params['latitude']}°N, {params['longitude']}°E")
print(f"Date range: {params['start_date']} to {params['end_date']}")

responses = openmeteo.weather_api(url, params=params)

# Process first location
response = responses[0]
print(f"\nCoordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone: {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

# Process hourly data
hourly = response.Hourly()
hourly_cloud_cover = hourly.Variables(0).ValuesAsNumpy()
hourly_cloud_cover_low = hourly.Variables(1).ValuesAsNumpy()
hourly_cloud_cover_mid = hourly.Variables(2).ValuesAsNumpy()
hourly_cloud_cover_high = hourly.Variables(3).ValuesAsNumpy()

hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )
}

hourly_data["cloud_cover"] = hourly_cloud_cover
hourly_data["cloud_cover_low"] = hourly_cloud_cover_low
hourly_data["cloud_cover_mid"] = hourly_cloud_cover_mid
hourly_data["cloud_cover_high"] = hourly_cloud_cover_high

hourly_dataframe = pd.DataFrame(data=hourly_data)

# Save to CSV
output_file = "cloud_data.csv"
hourly_dataframe.to_csv(output_file, index=False)

print(f"\n✓ Data saved to: {output_file}")
print(f"✓ Total records: {len(hourly_dataframe):,}")
print("\nFirst few rows:")
print(hourly_dataframe.head())
print("\nLast few rows:")
print(hourly_dataframe.tail())
