# Weather Information App

## Overview

This is a simple Python-based weather application that fetches current weather information for a given location. The program first converts the location name into latitude and longitude using the Geopy library. It then uses these coordinates to request live weather data from the OpenWeatherMap API.

## Features

* Takes a location name as input.
* Finds the latitude and longitude of the location.
* Fetches current weather data using OpenWeatherMap.
* Displays the summarized weather condition.
* Displays the detailed weather description.
* Shows the nearest location used by the weather API.

## Technologies Used

* Python
* Geopy
* Nominatim Geocoder
* Requests Library
* OpenWeatherMap API
* JSON

## Requirements

Before running the project, install the required Python libraries:

```bash
pip install geopy requests
```

## How the Code Works

1. The program imports the required libraries: `geopy`, `json`, and `requests`.
2. It creates a Nominatim geocoder object.
3. The location name, such as `"Delhi"`, is passed to the geocoder.
4. The geocoder returns the complete address, latitude, and longitude.
5. These coordinates are added to the OpenWeatherMap API URL.
6. A request is sent to the API.
7. The API response is converted into JSON format.
8. The program prints the weather condition and description.

## Sample Output

```text
You requested for weather around the following area Delhi, India

The summarised weather is Clouds, and the descriptive aspect of the weather is scattered clouds.

The weather shown was of this location Delhi which is the nearest to the location you mentioned i.e Delhi, India
```

## API Used

This project uses the OpenWeatherMap Current Weather Data API to fetch live weather details based on latitude and longitude.

## Conclusion

This project demonstrates how Python can be used to combine geolocation and weather APIs. It is useful for understanding API requests, JSON data handling, and real-time data fetching in Python.
