import streamlit as st
import time
from flask import Flask, request
import threading
import plotly.graph_objects as go

# Flask app to handle POST requests from ESP32
app = Flask(__name__)

# Global variables to store temperature and humidity
temperature = 0.0
humidity = 0.0

@app.route('/data', methods=['POST'])
def update_data():
    global temperature, humidity
    data = request.get_json()
    temperature = data['temperature']
    humidity = data['humidity']
    return "Data received", 200

# Start Flask app in a separate thread
def run_flask():
    app.run(host='0.0.0.0', port=8000)

thread = threading.Thread(target=run_flask)
thread.start()

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

# Continuously update the data displayed in the Streamlit app
while True:
    bar_chart_placeholder.plotly_chart(create_bar_chart(temperature, humidity))
    pie_chart_placeholder.plotly_chart(create_pie_chart(temperature, humidity))
    
    time.sleep(1)
