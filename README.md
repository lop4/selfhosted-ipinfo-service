### selfhosted ipinfo service

An quick & dirty dockerized compatible ipinfodb service.

Get Download Token from https://lite.ip2location.com/file-download

Start container
```
docker run -d -it -p 5000:5000 -e DOWNLOAD_TOKEN=<ip2location-download-token> unclesamwk/selfhosted-ipinfo-service
```
or with docker-compose
```
docker-compose pull
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
  "cityName": "Mountain View",
  "zipCode": "94043",
  "latitude": 37.751,
  "longitude": -97.822
}
```

### Bugs

Pull requests are welcome :-)
