#!/usr/bin/env python

from flask import Flask, request, abort
import IP2Location
import json
import re
import urllib.request
import os
import zipfile

# Get latest ipinfo db
TOKEN = os.environ['DOWNLOAD_TOKEN']
DB = "DB11LITE.zip"
urllib.request.urlretrieve("http://www.ip2location.com/download/?token=" + TOKEN + "&file=DB11LITEBIN", DB)
SIZE = os.path.getsize(DB)

if SIZE < 10000:
    print("Download-limit exceeded")
    exit()
else:
    zip_ref = zipfile.ZipFile(DB, 'r')
    zip_ref.extractall('/')
    zip_ref.close()

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

    IP2LocObj = IP2Location.IP2Location()
    IP2LocObj.open("./IP2LOCATION-LITE-DB11.BIN")
    response = IP2LocObj.get_all(ip)

    dict = {}
    dict["statusCode"] = "OK"
    dict["statusMessage"] = ""
    dict["ipAddress"] = ip
    dict["countryCode"] = response.country_short.decode("utf-8")
    dict["countryName"] = response.country_long.decode("utf-8")
    dict["cityName"] = response.city.decode("utf-8")
    dict["zipCode"] = response.zipcode.decode("utf-8")
    dict["latitude"] = response.latitude
    dict["longitude"] = response.longitude
    dict["timeZone"] = response.timezone.decode("utf-8")

    jsonarray = json.dumps(dict)

    return jsonarray

if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded='true')
