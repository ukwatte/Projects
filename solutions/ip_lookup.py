from geoip import geolite2
from urllib2 import urlopen
import json


def getplace(lat, lon):
    maps_url = "http://maps.googleapis.com/maps/api/geocode/json?"
    maps_url += "latlng=%s,%s&sensor=false" % (lat, lon)
    cont = urlopen(maps_url).read()
    data = json.loads(cont)
    # result number zero contains maximum information
    components = data['results'][0]['formatted_address']
    return components


def main():
    ip = raw_input("Enter IP : ")
    match = geolite2.lookup(ip)
    lat, lon = match.location
    print "lat,long =", lat, lon
    print "address  =", getplace(lat, lon)


if __name__ == '__main__':
    main()
