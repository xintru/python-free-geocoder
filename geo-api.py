
from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/get_geocoder_data', methods=['POST'])
def get_geocoder_data():
    data = request.get_json()
    address = data.get('address', "")
    geolocator = Nominatim(user_agent="random_agent")
    location = geolocator.geocode(address, addressdetails=True)
    print(location.raw)
    return jsonify(location=location.raw, lat=location.latitude, lng=location.longitude)