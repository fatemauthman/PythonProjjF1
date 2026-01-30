
import streamlit as st
from datetime import datetime
from weather_logic import get_weather, get_location_time

st.title('Weather App')

name = st.text_input('Enter your name', '')
if name:
    st.write(f'Hello {name}, welcome to the weather app!')


    import streamlit as st
    import requests
    import plotly.express as px
    import pandas as pd

    API_KEY = "631e6df9a39414ae72d5ad878b96c13e"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    st.title(" Weather Checker App")

    city = st.text_input("Enter city name")

    if st.button("Get Weather"):
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]

            st.write(f" Temperature: {temp} °C")
            st.write(f" Humidity: {humidity}%")
            st.write(f" Condition: {condition}")

            df = pd.DataFrame({
                "Metric": ["Temperature", "Humidity"],
                "Value": [temp, humidity]
            })

            fig = px.bar(df, x="Metric", y="Value", title=f"Weather in {city}")
            st.plotly_chart(fig)
        else:
            st.error("City not found or API error")

            import streamlit as st

            # ---------- Title ----------
            st.title(" Weather App – Local Demo")

            # ---------- User Input ----------
            st.header("User Input")
            city = st.text_input("Enter a city name")

            temperature = st.slider(
                "Select a sample temperature (°C)",
                min_value=-10,
                max_value=40,
                value=20
            )

            # ---------- Processing ----------
            st.header("Processing")
            if city:
                message = f"The selected city is {city}."
            else:
                message = "No city entered yet."

            # ---------- Output ----------
            st.header("Output")
            st.write(message)
            st.write(f"Sample temperature: {temperature} °C")


from datetime import datetime

local_time = datetime.now().strftime("%A, %d %B %Y, %H:%M")




st.subheader("Date & Time")

st.write(f"**Your local time:** {local_time}")
st.write(
    f"**Local time in {weather['city']}:** "
    f"{get_location_time(weather['timezone'])}"
)