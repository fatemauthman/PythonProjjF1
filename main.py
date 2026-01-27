
import streamlit as st

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

    st.title("🌦️ Weather Checker App")

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

            st.write(f"🌡️ Temperature: {temp} °C")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"☁️ Condition: {condition}")

            df = pd.DataFrame({
                "Metric": ["Temperature", "Humidity"],
                "Value": [temp, humidity]
            })

            fig = px.bar(df, x="Metric", y="Value", title=f"Weather in {city}")
            st.plotly_chart(fig)
        else:
            st.error("City not found or API error")