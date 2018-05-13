import urllib.request
import json

url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=140010'
html = urllib.request.urlopen(url)
jsonfile = json.loads(html.read().decode('utf-8'))
print(jsonfile['forecasts'])