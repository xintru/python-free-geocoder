from flask_api import FlaskAPI, status
from flask import request
from geopy.geocoders import Nominatim

app = FlaskAPI(__name__)


@app.route('/get_geocoder_data')
def get_geocoder_data():
    try: 
        address = request.args.get('address', "")
        geolocator = Nominatim(user_agent="agent")
        location = geolocator.geocode(address, addressdetails=True)
        address_data = location.raw.get('address')
        display_name = location.raw.get('display_name')

        return { 
            'address_data': address_data,
            'display_name': display_name,
            'lat': location.latitude, 
            'lng': location.longitude 
            }
    except : 
        return { 'message': 'Invalid query, data not found.' }, status.HTTP_404_NOT_FOUND

