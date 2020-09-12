
from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
import json

app = Flask(__name__)


@app.route('/get_geocoder_data')
def get_geocoder_data():
    address = request.args.get('address', "")
    geolocator = Nominatim(user_agent="agent")
    location = geolocator.geocode(address, addressdetails=True)
    address_data = location.raw.get('address')
    display_name = location.raw.get('display_name')

    return jsonify(address_data=address_data, display_name=display_name, lat=location.latitude, lng=location.longitude)
