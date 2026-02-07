import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timezone, timedelta

# =========================
# App Configuration
# =========================
st.set_page_config(page_title="Weather App", page_icon="🌦️")
st.title("🌦️ Weather Checker App")

# =========================
# API Key (Safe handling)
# =========================
if "api_key" in st.secrets:
    API_KEY = st.secrets["api_key"]
else:
    st.error("API key is missing. Please configure Streamlit Secrets.")
    st.stop()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# =========================
# Personalization
# =========================
st.subheader("👋 Welcome")
name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}! 😊 Welcome to the Weather App")

st.divider()

# =========================
# Functions
# =========================
def get_weather(city, api_key, units="metric"):
    params = {
        "q": city,
        "appid": api_key,
        "units": units
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"],
        "timezone": data["timezone"],
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"]
    }


def get_location_time(timezone_offset):
    utc_time = datetime.now(timezone.utc)
    location_time = utc_time + timedelta(seconds=timezone_offset)
    return location_time.strftime("%A, %d %B %Y, %H:%M")


def packing_recommendations(temp, condition):
    items = []

    if temp < 10:
        items += ["Warm jacket", "Scarf", "Closed shoes"]
    elif 10 <= temp < 20:
        items += ["Light jacket", "Long pants"]
    else:
        items += ["T-shirts", "Sunglasses", "Sunscreen"]

    condition = condition.lower()
    if "rain" in condition:
        items += ["Umbrella", "Raincoat"]
    if "snow" in condition:
        items += ["Winter boots"]

    return list(set(items))

# =========================
# UI
# =========================
city = st.text_input("🌍 Enter city name")

if st.button("Get Weather") and city:
    try:
        weather_data = get_weather(city, API_KEY)

        st.subheader(f"📍 Weather in {weather_data['city']}")
        st.write(f"🌡️ **Temperature:** {weather_data['temperature']} °C")
        st.write(f"💧 **Humidity:** {weather_data['humidity']}%")
        st.write(f"🌥️ **Condition:** {weather_data['condition']}")

        # Weather alerts
        if weather_data["temperature"] > 35:
            st.warning("⚠️ Extreme heat – stay hydrated!")
        elif weather_data["temperature"] < 5:
            st.warning("⚠️ Very cold weather – dress warmly!")

        # Date & Time
        st.subheader("🕒 Local Date & Time")
        location_time = get_location_time(weather_data["timezone"])
        st.write(location_time)

        # Map
        st.subheader("🗺️ Location on Map")
        map_df = pd.DataFrame({
            "lat": [weather_data["lat"]],
            "lon": [weather_data["lon"]]
        })
        st.map(map_df)

        # Packing recommendations
        st.subheader("🎒 Recommended items to pack")
        items = packing_recommendations(
            weather_data["temperature"],
            weather_data["condition"]
        )
        for item in items:
            st.write(f"• {item}")

    except requests.exceptions.HTTPError:
        st.error("❌ City not found. Please check the name and try again.")

    except Exception as e:
        st.error("⚠️ Something went wrong.")
