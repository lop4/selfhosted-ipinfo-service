### selfhosted ipinfo service

An quick & dirty dockerized compatible ipinfodb service with maxmind database.

Start container
```
docker-compose build
docker-compose up -d
```
Test the service with curl or in a browser
```
curl "http://localhost:5000/ipinfo?ipaddress=8.8.8.8"
```
Output:
```
{
  "statusCode": "OK",
  "statusMessage": "",
  "ipAddress": "8.8.8.8",
  "countryCode": "US",
  "countryName": "United States",
  "cityName": null,
  "zipCode": null,
  "latitude": 37.751,
  "longitude": -97.822
}
```

### Bugs

Pull requests are welcome :-)
