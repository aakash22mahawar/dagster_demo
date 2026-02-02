# weather_assets.py
from dagster import asset
from dag_weather.weather_api.weather import fetch_weather
from dag_weather.weather_api.load import load_to_snowflake


@asset
def weather_raw():
    """Fetch raw weather data from API."""
    data = fetch_weather()
    return data  # This output will feed into downstream assets


@asset
def weather_loaded(weather_raw):
    """Load the raw weather data into Snowflake."""
    load_to_snowflake(weather_raw)
    
    # Return a simple status dict to signal completion
    return {"status": "loaded", "num_records": len(weather_raw) if hasattr(weather_raw, "__len__") else 1}
