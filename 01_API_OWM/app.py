
import datetime
import json
import os
from pathlib import Path
from pprint import pprint

import requests

os.chdir(Path(__file__).parent)


LAT = 52.5244
LON = 13.4105
API_KEY = "a40d32d92994f36fbf31e815dc7b86"
LANG = "DE"

# Using LON / LAT for Berlin
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units=metric&lang={LANG}&appid={API_KEY}"



# Call the URL and get the response
response = requests.get(URL)

print(response) # Request Status 200 : OK , 401: Un-authorized 

# read the JSON data
data = response.json()

pprint(data)

# Save JSON to file
json_str = json.dumps(data)
with open("./result.json", mode= "w", encoding= "UTF-8") as file:
    file.write(json_str)



""" 
Required:
~~~~~~~~~~~~~
1. Temperature
2. Sunrise
3. Sunset
"""



temperature = data["main"]["temp"]

# Convert UTC (unix) 
sunrise = datetime.datetime.utcfromtimestamp(data["sys"]["sunrise"])
sunset  = datetime.datetime.utcfromtimestamp(data["sys"]["sunset"])

print(temperature, sunrise, sunset)