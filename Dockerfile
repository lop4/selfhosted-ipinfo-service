FROM python
MAINTAINER Sam <unclesamwk@googlemail.com>

RUN apt update \
 && apt upgrade -y

RUN pip install geoip2 Flask-HTTPAuth flask

RUN wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz \
 && tar xvfz GeoLite2-City.tar.gz

ADD api.py .
CMD python api.py
