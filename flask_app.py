from flask import Flask, request, jsonify

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
    return jsonify({"message": "Data received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
