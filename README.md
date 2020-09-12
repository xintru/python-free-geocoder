# Python Geocoder

Api that helps you do geocoding for free independently from yandex or google

# Installing (MacOS)

You'll need to use pipenv. You can get it by running brew install pipenv in your console.

1. pipenv install
2. pipenv shell
3. export FLASK_ENV=development
4. export FLASK_APP=geo-api.py
5. flask run

# Endpoints

GET '/get_geocoder_data?address=string'

Response example with "London" query:

```
{
    "address_data": {
        "city": "London",
        "country": "United Kingdom",
        "country_code": "gb",
        "state": "England",
        "state_district": "Greater London"
    },
    "display_name": "London, Greater London, England, United Kingdom",
    "lat": 51.5073219,
    "lng": -0.1276474
}
```
