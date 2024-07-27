import streamlit as st
import time
import requests
import plotly.graph_objects as go

# Streamlit app
st.title("ESP32 DHT Server!")
st.markdown("### Temperature and Humidity Monitoring")

# Create placeholders for the charts
bar_chart_placeholder = st.empty()
pie_chart_placeholder = st.empty()

def create_bar_chart(temp, hum):
    fig = go.Figure(data=[
        go.Bar(name='Temperature', x=['Temperature'], y=[temp], marker_color='orange'),
        go.Bar(name='Humidity', x=['Humidity'], y=[hum], marker_color='blue')
    ])
    fig.update_layout(barmode='group', title="Temperature and Humidity Bar Chart")
    return fig

def create_pie_chart(temp, hum):
    fig = go.Figure(data=[
        go.Pie(labels=['Temperature', 'Humidity'], values=[temp, hum], hole=.3)
    ])
    fig.update_layout(title="Temperature and Humidity Pie Chart")
    return fig

# Function to fetch data from Flask API
def fetch_data():
    try:
        response = requests.get('http://localhost:8000/data')
        if response.status_code == 200:
            data = response.json()
            return data['temperature'], data['humidity']
    except Exception as e:
        st.error(f"Error fetching data: {e}")
    return 0.0, 0.0

# Continuously update the data displayed in the Streamlit app
while True:
    temperature, humidity = fetch_data()
    bar_chart_placeholder.plotly_chart(create_bar_chart(temperature, humidity))
    pie_chart_placeholder.plotly_chart(create_pie_chart(temperature, humidity))
    
    time.sleep(1)
