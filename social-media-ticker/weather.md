# Get current temperature

References:


```python
#Get current temperature

Using a service provided by our government that can take latitude and longitude as inputs

```python
import requests
import json
LAT = "35.7877"
LONG = "-78.6442"
url = "https://api.weather.gov/points/{0},{1}/forecast".format(LAT,LONG)
print (url)
response = requests.get(url) 
j = json.loads(response.text)
tf = (j["properties"]["periods"][0]["temperature"])
print('It is currently {0} °F'.format(tf))

```

References:
[API Doc](https://www.weather.gov/documentation/services-web-api#/)
[Example](https://rapidapi.com/theapiguy/api/national-weather-service/details)
```

