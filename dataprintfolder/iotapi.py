from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/submit_data', methods=['POST'])
def submit_data():
    # Get input data from the user or use defaults
    rfid = request.form.get('rfid', 'ABC123XYZ')  # Default RFID
    vehicle_number = request.form.get('vehicle_number', 'PY10VR2010')  # Default vehicle number
    vehicle_type = request.form.get('vehicle_type', 'truck')  # Default vehicle type
    weight = request.form.get('weight', '4600')  # Default weight

    # Construct JSON data
    data = {
        "rfid": rfid,
        "vehicleMumber": vehicle_number,
        "vehicleType": vehicle_type,
        "weight": weight
    }

    # Send the data to the API
    api_url = 'https://iot-api.hkrhc.ac.in/iot_receiver.php'
    response = requests.post(api_url, json=data)

    # Check the response from the API
    if response.status_code == 200:
        return jsonify({"message": "Data submitted successfully!", "response": response.json()}), 200
    else:
        return jsonify({"message": "Failed to submit data", "error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
