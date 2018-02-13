#!/usr/bin/env python

from flask import Flask, request, abort
import geoip2.database
import json
import re

ipregex = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is the ultimate ipinfo api!"

@app.route('/ipinfo', methods=['GET'])
def ipinfo():

    ip = request.args.get('ipaddress')

    if ip is None:
        return 'Please give an ipAddress in URL like http://0.0.0.0:5000/ipinfo?ipaddress=123.456.789.123'

    checkip = ipregex.match(ip)

    if not checkip:
        return "No valid ip address"

    reader = geoip2.database.Reader("/GeoLite2-City_20180206/GeoLite2-City.mmdb")
    response = reader.city(ip)

    dict = {}
    dict["statusCode"] = "OK"
    dict["statusMessage"] = ""
    dict["ipAddress"] = ip
    dict["countryCode"] = response.country.iso_code
    dict["countryName"] = response.country.name
    dict["cityName"] = response.city.name
    dict["zipCode"] = response.postal.code
    dict["latitude"] = response.location.latitude
    dict["longitude"] = response.location.longitude

    jsonarray = json.dumps(dict)

    return jsonarray

if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded='true')
