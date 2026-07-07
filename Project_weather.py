# importing geopy library and Nominatim class
from geopy.geocoders import Nominatim
import json
import requests
try:
  # calling the Nominatim tool and create Nominatim class
  loc = Nominatim(user_agent="Geopy Library")
  # entering the location name
  getLoc = loc.geocode("Delhi")
  # printing address
  print("you requested for weather around the following area {} ".format(getLoc.address))
  # printing latitude and longitude
  #print(type(getLoc.latitude)) float values
  #print("Latitude = ", getLoc.latitude, "\n")
  #print("Longitude = ", getLoc.longitude)
  lattitude=str(getLoc.latitude)
  longitude=str(getLoc.longitude)
  url="https://api.openweathermap.org/data/2.5/weather?lat="+lattitude+"&lon="+longitude+"&appid=<insert your api key from open weather app here>"
  #print(url)
  response = requests.get(url)
  #print(response.json())
  final_dict=response.json()
  print(f"the summarised weather is {final_dict['weather'][0]['main']}, and the descriptive aspect of the weather is {final_dict['weather'][0]['description']}") #summarised weather with detailed weather description
  print("the weather shown was of this location {} which is the nearest to the location you mentioned i.e {}".format(final_dict['name'],getLoc.address)) #location where it picked it up
except Exception as e:
     print(f"An unexpected error occurred: {e}")
